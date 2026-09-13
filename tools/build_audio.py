import json, os, subprocess, shutil, re
from concurrent.futures import ThreadPoolExecutor
S='/tmp/claude-0/-home-claude/7a78a83e-d3e0-5061-9f25-1f78822d90c1/scratchpad'
A=f'{S}/bbsrc/assets'; OUT=f'{S}/out'
SR=32000; GAP=0.12
MAX_CHUNK=45.0          # seconds of audio per sprite file — caps one decode on a phone
shutil.rmtree(f'{OUT}/audio',ignore_errors=True); os.makedirs(f'{OUT}/audio')
TMP=f'{S}/tmp_wav2'; shutil.rmtree(TMP,ignore_errors=True); os.makedirs(TMP)

def norm_wav(src,dst,cap):
    subprocess.run(['ffmpeg','-v','quiet','-y','-i',src,'-ac','1','-ar',str(SR),
        '-af','silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.02,'
              'areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse',
        '-t',str(cap),dst],check=True)
    return float(subprocess.run(['ffprobe','-v','quiet','-show_entries','format=duration',
        '-of','csv=p=0',dst],capture_output=True,text=True).stdout.strip() or 0)

def build(items, keyfn, groupfn, cap, prefix):
    groups={}
    for it in items: groups.setdefault(groupfn(it),[]).append(it)
    manifest={}
    for g,lst in sorted(groups.items()):
        gd=f'{TMP}/{prefix}{g}'; os.makedirs(gd,exist_ok=True)
        def job(iit):
            i,it=iit; w=f'{gd}/{i}.wav'
            try: return it,w,norm_wav(os.path.join(A,it['file']),w,cap)
            except Exception as e: print('skip',it['file'],e); return it,w,0.0
        with ThreadPoolExecutor(max_workers=8) as ex:
            res=list(ex.map(job, enumerate(lst)))
        res=[r for r in res if r[2]>0.02]
        # pack into chunks of at most MAX_CHUNK seconds (one clip is never split)
        chunks=[]; cur=[]; curlen=0.0
        for it,w,d in res:
            if cur and curlen+d+GAP > MAX_CHUNK:
                chunks.append(cur); cur=[]; curlen=0.0
            cur.append((it,w,d)); curlen+=d+GAP
        if cur: chunks.append(cur)
        sil=f'{gd}/sil.wav'
        subprocess.run(['ffmpeg','-v','quiet','-y','-f','lavfi','-i',
            f'anullsrc=r={SR}:cl=mono','-t',str(GAP),sil],check=True)
        for ci,chunk in enumerate(chunks):
            name=f'{g}-{ci}' if len(chunks)>1 else g
            offs={}; t=0.0; parts=[]
            for it,w,d in chunk:
                offs[keyfn(it)]=[round(t,3),round(d,3)]; parts.append(w); t+=d+GAP
            lst_file=f'{gd}/list{ci}.txt'
            with open(lst_file,'w') as fh:
                for j,p in enumerate(parts):
                    fh.write(f"file '{p}'\n")
                    if j<len(parts)-1: fh.write(f"file '{sil}'\n")
            outmp3=f'{OUT}/audio/{prefix}{name}.mp3'
            subprocess.run(['ffmpeg','-v','quiet','-y','-f','concat','-safe','0','-i',lst_file,
                '-c:a','libmp3lame','-b:a','64k','-ac','1','-ar',str(SR),outmp3],check=True)
            manifest[name]={'file':f'audio/{prefix}{name}.mp3','map':offs,
                            'bytes':os.path.getsize(outmp3),'total':round(t,3)}
        print(f'{prefix}{g}: {len(res)} clips -> {len(chunks)} chunk(s)')
    return manifest

sounds=json.load(open(f'{S}/ir_map.json'))
for o in sounds:
    o['id']=os.path.splitext(os.path.basename(o['file']))[0]
    o['grp']=o['file'].split('/')[1]
sm=build(sounds, lambda o:o['id'], lambda o:o['grp'], 10.0, 's_')

pats=json.load(open(f'{S}/ir_patterns.json'))
for p in pats:
    p['grp']=p['file'].split('/')[1].lower().replace(' ','-')
    p['id']=re.sub(r'[^a-z0-9]+','-',os.path.splitext(p['file'][len('patterns/'):])[0].lower()).strip('-')
pm=build(pats, lambda o:o['id'], lambda o:o['grp'], 40.0, 'p_')

json.dump({'sounds':sm,'patterns':pm},open(f'{S}/build/sprites.json','w'))
all_=list(sm.values())+list(pm.values())
print('FILES: %d   TOTAL: %.1f MB   worst chunk: %.1f s = %.1f MB decoded @32k / %.1f MB @48k'%(
  len(all_), sum(v['bytes'] for v in all_)/1048576,
  max(v['total'] for v in all_),
  max(v['total'] for v in all_)*32000*4/1048576,
  max(v['total'] for v in all_)*48000*4/1048576))
