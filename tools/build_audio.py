import json, os, subprocess, shutil, math
S='/tmp/claude-0/-home-claude/7a78a83e-d3e0-5061-9f25-1f78822d90c1/scratchpad'
A=f'{S}/bbsrc/assets'; OUT=f'{S}/out'
os.makedirs(f'{OUT}/audio',exist_ok=True)
TMP=f'{S}/tmp_wav'; shutil.rmtree(TMP,ignore_errors=True); os.makedirs(TMP)
SR=32000; GAP=0.12

def norm_wav(src,dst,cap):
    # trim leading/trailing silence, cap length, mono, normalise peak
    subprocess.run(['ffmpeg','-v','quiet','-y','-i',src,'-ac','1','-ar',str(SR),
        '-af',f'silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.02,areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,areverse',
        '-t',str(cap),dst],check=True)
    d=float(subprocess.run(['ffprobe','-v','quiet','-show_entries','format=duration','-of','csv=p=0',dst],capture_output=True,text=True).stdout.strip() or 0)
    return d

from concurrent.futures import ThreadPoolExecutor
def build(items, keyfn, groupfn, cap, prefix):
    groups={}
    for it in items: groups.setdefault(groupfn(it),[]).append(it)
    manifest={}
    for g,lst in groups.items():
        parts=[]; offs={}; t=0.0
        gd=f'{TMP}/{g}'; os.makedirs(gd,exist_ok=True)
        def job(iit):
            i,it=iit; w=f'{gd}/{i}.wav'
            try: return it,w,norm_wav(os.path.join(A,it['file']),w,cap)
            except Exception as e: print('skip',it['file'],e); return it,w,0.0
        with ThreadPoolExecutor(max_workers=8) as ex:
            res=list(ex.map(job, enumerate(lst)))
        for it,w,d in res:
            if d<=0.02: continue
            offs[keyfn(it)]=[round(t,3),round(d,3)]
            parts.append(w); t+=d+GAP
        # concat with gaps
        lst_file=f'{gd}/list.txt'
        sil=f'{gd}/sil.wav'
        subprocess.run(['ffmpeg','-v','quiet','-y','-f','lavfi','-i',f'anullsrc=r={SR}:cl=mono','-t',str(GAP),sil],check=True)
        with open(lst_file,'w') as fh:
            for j,p in enumerate(parts):
                fh.write(f"file '{p}'\n")
                if j<len(parts)-1: fh.write(f"file '{sil}'\n")
        outmp3=f'{OUT}/audio/{prefix}{g}.mp3'
        subprocess.run(['ffmpeg','-v','quiet','-y','-f','concat','-safe','0','-i',lst_file,
                        '-c:a','libmp3lame','-b:a','64k','-ac','1','-ar',str(SR),outmp3],check=True)
        manifest[g]={'file':f'audio/{prefix}{g}.mp3','map':offs,
                     'bytes':os.path.getsize(outmp3),'total':round(t,3)}
        print(f'{prefix}{g}: {len(offs)} clips, {os.path.getsize(outmp3)/1048576:.2f} MB, {t:.1f}s')
    return manifest

sounds=json.load(open(f'{S}/ir_map.json'))
for o in sounds:
    o['id']=os.path.splitext(os.path.basename(o['file']))[0]
    o['grp']=o['file'].split('/')[1]
sm=json.load(open(f'{S}/build/sprites.json'))['sounds'] if os.path.exists(f'{S}/build/sprites.json') else build(sounds, lambda o:o['id'], lambda o:o['grp'], 10.0, 's_')

pats=json.load(open(f'{S}/ir_patterns.json'))
import re as _re
for p in pats:
    parts=p['file'].split('/')
    p['grp']=parts[1].lower().replace(' ','-')
    p['id']=_re.sub(r'[^a-z0-9]+','-',os.path.splitext(p['file'][len('patterns/'):])[0].lower()).strip('-')
pm=build(pats, lambda o:o['id'], lambda o:o['grp'], 40.0, 'p_')

json.dump({'sounds':sm,'patterns':pm},open(f'{S}/build/sprites.json','w'))
tb=sum(v['bytes'] for v in list(sm.values())+list(pm.values()))
print('TOTAL AUDIO: %.1f MB across %d files'%(tb/1048576,len(sm)+len(pm)))
