import json, os, subprocess, sys, math
import numpy as np
from scipy.signal import stft

S='/tmp/claude-0/-home-claude/7a78a83e-d3e0-5061-9f25-1f78822d90c1/scratchpad'
ASSETS=f'{S}/bbsrc/assets'
SR=44100

def load(path):
    p=subprocess.run(['ffmpeg','-v','quiet','-i',path,'-ac','1','-ar',str(SR),'-f','f32le','-'],
                     capture_output=True)
    return np.frombuffer(p.stdout,dtype=np.float32).astype(np.float64)

def trim(x, thresh_db=-45):
    if len(x)==0: return x,0
    env=np.abs(x)
    # smooth
    w=int(SR*0.005)
    k=np.ones(w)/w
    env=np.convolve(env,k,mode='same')
    peak=env.max()
    if peak<=0: return x,0
    t=peak*(10**(thresh_db/20))
    idx=np.where(env>t)[0]
    if len(idx)==0: return x,0
    a,b=idx[0],idx[-1]
    return x[a:b+1], a/SR

LOGF_MIN, LOGF_MAX = 30.0, 16000.0
NB=56
edges=np.exp(np.linspace(math.log(LOGF_MIN),math.log(LOGF_MAX),NB+1))

def analyze(path):
    x=load(path)
    if len(x)<512: return None
    x=x/ (np.abs(x).max()+1e-12)
    xt,off=trim(x)
    if len(xt)<512: xt=x
    dur=len(xt)/SR
    n=1024 if len(xt)>=2048 else 256
    f,t,Z=stft(xt, fs=SR, nperseg=n, noverlap=n//2, window='hann')
    P=np.abs(Z)**2
    spec=P.mean(axis=1)
    spec[f<25]=0
    tot=spec.sum()+1e-20
    # band energies (log bands)
    bands=[]
    for i in range(NB):
        m=(f>=edges[i])&(f<edges[i+1])
        bands.append(float(spec[m].sum()/tot) if m.any() else 0.0)
    bands=np.array(bands)
    # cumulative freq percentiles
    c=np.cumsum(spec)/tot
    def pct(q):
        j=int(np.searchsorted(c,q)); j=min(j,len(f)-1); return float(f[j])
    f05,f25,f50,f75,f95=pct(.05),pct(.25),pct(.5),pct(.75),pct(.95)
    centroid=float((f*spec).sum()/tot)
    # spectral flatness (noisiness) on mean spectrum
    ps=spec[spec>0]
    flat=float(np.exp(np.log(ps+1e-20).mean())/ (ps.mean()+1e-20)) if len(ps)>8 else 0.0
    # --- F0: frame-wise normalised autocorrelation, median of voiced frames ---
    def frame_f0(seg):
        if len(seg) < 900: return 0.0, 0.0
        seg = seg - seg.mean()
        if np.abs(seg).max() < 1e-6: return 0.0, 0.0
        ac = np.correlate(seg, seg, mode='full')[len(seg)-1:]
        ac = ac / (ac[0] + 1e-20)
        lo, hi = int(SR/4000), min(int(SR/45), len(ac)-2)
        if hi <= lo + 2: return 0.0, 0.0
        # skip past the first descent so lag~0 side-lobes can't win
        z = 1
        while z < hi and ac[z] > 0: z += 1
        start = max(lo, z)
        if start >= hi - 2: return 0.0, 0.0
        reg = ac[start:hi]
        # true local maximum only
        k = int(np.argmax(reg))
        if k == 0 or k == len(reg)-1: 
            if reg[k] < 0.5: return 0.0, 0.0
        lag = start + k
        # parabolic refinement
        if 0 < k < len(reg)-1:
            y0,y1,y2 = reg[k-1],reg[k],reg[k+1]
            d = y0 - 2*y1 + y2
            if abs(d) > 1e-12: lag = lag + 0.5*(y0-y2)/d
        return float(SR/lag), float(reg[k])

    env = np.convolve(np.abs(xt), np.ones(int(SR*0.01))/int(SR*0.01), mode='same')
    pv0 = env.max() + 1e-20
    W = int(SR*0.05); H = int(SR*0.025)
    cands = []
    for st in range(0, max(1, len(xt)-W), H):
        w = xt[st:st+W]
        if len(w) < W: break
        if env[st:st+W].max() < pv0*0.25: continue
        ff, rr = frame_f0(w)
        if ff > 0 and rr > 0.45: cands.append((ff, rr))
    if cands:
        arr = np.array([c[0] for c in cands]); rs = np.array([c[1] for c in cands])
        f0 = float(np.median(arr)); hnr = float(np.median(rs))
        voiced = len(cands) / max(1, (max(1, len(xt)-W)//H + 1))
        f0_spread = float(np.percentile(arr,90) - np.percentile(arr,10))
    else:
        f0 = 0.0; hnr = 0.0; voiced = 0.0; f0_spread = 0.0

    # --- attack / decay measured on the FIRST onset event ---
    pk = int(np.argmax(env)); pv = env[pk] + 1e-20
    on = np.where(env >= pv*0.3)[0]
    onset = int(on[0]) if len(on) else 0
    win = env[onset:onset+int(SR*0.35)]
    if len(win) < 8: win = env[onset:]
    lpk = int(np.argmax(win)); lpv = win[lpk] + 1e-20
    r90 = np.where(win[:lpk+1] >= lpv*0.9)[0]
    attack = float((r90[0] if len(r90) else lpk)/SR)
    tail = env[onset+lpk:]
    dec = np.where(tail <= lpv*0.1)[0]
    decay = float((dec[0]/SR) if len(dec) else (len(tail)/SR))
    # dominant spectral peak
    fpeak = float(f[int(np.argmax(spec))])
    # onset density: events per second (rough, for rolls)
    thr = pv*0.35
    above = (env > thr).astype(np.int8)
    rises = np.where((above[1:] - above[:-1]) == 1)[0]
    mingap = int(SR*0.06)
    kept = []
    for r in rises:
        if not kept or r - kept[-1] >= mingap: kept.append(int(r))
    events = len(kept)
    ev_rate = round(events/max(dur,1e-6), 2)
    # sustain-ness: fraction of duration above 30% of peak
    sus=float((env>pv*0.3).sum()/len(env))
    # waveform peaks for drawing
    NW=110
    seg_len=max(1,len(xt)//NW)
    wf=[float(np.abs(xt[i*seg_len:(i+1)*seg_len]).max()) for i in range(NW) if (i+1)*seg_len<=len(xt)]
    if wf:
        mx=max(wf)+1e-12
        wf=[round(v/mx,3) for v in wf]
    bmax=bands.max()+1e-20
    return dict(dur=round(dur,3), f05=round(f05), f25=round(f25), f50=round(f50),
                f75=round(f75), f95=round(f95), centroid=round(centroid),
                flatness=round(flat,4), f0=round(f0,1), hnr=round(hnr,3),
                attack_ms=round(attack*1000,1), decay_ms=round(decay*1000,1),
                sustain=round(sus,3), voiced=round(voiced,3), f0_spread=round(f0_spread,1), fpeak=round(fpeak), events=events, ev_rate=ev_rate,
                spec=[round(float(v/bmax),3) for v in bands],
                wave=wf)

def run(mapping, key, outfile):
    res={}
    for i,o in enumerate(mapping):
        p=os.path.join(ASSETS,o['file'])
        try:
            a=analyze(p)
        except Exception as e:
            a=None; print('ERR',o['file'],e,file=sys.stderr)
        if a: res[o[key]]=a
        if i%40==0: print(i,'/',len(mapping),flush=True)
    json.dump(res,open(outfile,'w'))
    print('wrote',outfile,len(res))

snd=json.load(open(f'{S}/ir_map.json'))
for o in snd: o['k']=o['file']
run(snd,'k',f'{S}/build/acoustics_sounds.json')
pat=json.load(open(f'{S}/ir_patterns.json'))
for o in pat: o['k']=o['file']
run(pat,'k',f'{S}/build/acoustics_patterns.json')
