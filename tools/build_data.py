# -*- coding: utf-8 -*-
import json, os, re, sys
S='/tmp/claude-0/-home-claude/7a78a83e-d3e0-5061-9f25-1f78822d90c1/scratchpad'
sys.path.insert(0,f'{S}/build/tax')
import whistles, basses, core, snares, rest
TAX={}
for m in (whistles,basses,core,snares,rest): TAX.update(m.TAX)

FAM={'PE':('pulmonic','out'),'PI':('pulmonic','in'),'GE':('glottalic','out'),'GI':('glottalic','in'),
     'LI':('lingual','in'),'LE':('lingual','out'),'BE':('buccal','out'),'BI':('buccal','in'),
     'AE':('aerodynamic','out'),'AI':('aerodynamic','in')}
PREC=['external','aerodynamic','lingual','buccal','glottalic','pulmonic']

def air(code):
    if code.startswith('none'): return dict(fams=['external'],prim='external',dirs=['none'],code='—')
    toks=[t.strip() for t in code.split('+')]
    fams=[]; dirs=[]
    for t in toks:
        f,d=FAM.get(t,('pulmonic','out'))
        if f not in fams: fams.append(f)
        if d not in dirs: dirs.append(d)
    prim=sorted(fams,key=lambda f:PREC.index(f))[0]
    canon='+'.join(sorted(toks,key=lambda t:(PREC.index(FAM.get(t,('pulmonic','out'))[0]),t)))
    return dict(fams=fams,prim=prim,dirs=dirs,code=canon)

PLACES=['bilabial','labiodental','dental','alveolar','postalveolar','palatal','velar','uvular','pharyngeal','glottal']
PLACE_ALIAS=[('labiodental','labiodental'),('bilabial','bilabial'),('labial (finger','bilabial'),
  ('labial (hand','bilabial'),('labial (pucker','bilabial'),('labial','bilabial'),('lip','bilabial'),
  ('dental','dental'),('alveolar','alveolar'),('postalveolar','postalveolar'),('palatal','palatal'),
  ('velar','velar'),('uvular','uvular'),('epiglottal','pharyngeal'),('pharyngeal','pharyngeal'),
  ('laryngeal','glottal'),('glottal','glottal'),('lateral','alveolar')]
def place_of(s):
    low=s.lower()
    # earliest-occurring recognised place is the primary articulation
    best=None
    for al,p in PLACE_ALIAS:
        i=low.find(al)
        if i>=0 and (best is None or i<best[0]): best=(i,p)
    return best[1] if best else 'glottal'
def places_all(s):
    low=s.lower(); out=[]
    for al,p in PLACE_ALIAS:
        if al in low and p not in out: out.append(p)
    return out or ['glottal']

MANNERS=['plosive','affricate','fricative','nasal','trill','lateral','click','ejective','implosive','whistle','phonation','percussive']
def manner_of(mstr,astr):
    m=mstr.lower()
    if 'percussive' in m or 'struck' in m: return 'percussive'
    if 'click' in m: return 'click'
    if 'whistle' in m: return 'whistle'
    if 'implosive' in m: return 'implosive'
    if 'ejective' in m or ('GE' in astr.split('+') and ('slap' in m or 'plosive' in m or 'affricate' in m or 'fricative' in m)): return 'ejective'
    if 'trill' in m or 'oscillation' in m or 'flutter' in m: return 'trill'
    if 'lateral' in m: return 'lateral'
    if 'affricate' in m: return 'affricate'
    if 'nasal' in m: return 'nasal'
    if 'fricative' in m or 'friction' in m or 'aspiration' in m: return 'fricative'
    if 'plosive' in m or 'slap' in m or 'stop' in m or 'release' in m or 'pluck' in m: return 'plosive'
    if ('phonation' in m or 'polyphony' in m or 'squeak' in m or 'subharmonic' in m
        or 'resonance' in m or 'voice' in m or 'register' in m): return 'phonation'
    return 'fricative'

# place x manner feasibility:  S = attested as a phoneme in some language,
# P = physically producible but not used phonemically anywhere, X = no human can make it
GRID = {
 'plosive':    "SPSSSSSSSS",
 'affricate':  "SSSSSSSSPP",
 'fricative':  "SSSSSSSSSS",
 'nasal':      "SSSSSSSSXX",
 'trill':      "SPSSPXXSSX",
 'lateral':    "XXSSSSSXXX",
 'click':      "SXSSSSXXXX",
 'ejective':   "SPSSSSSSSX",
 'implosive':  "SPSSSSSSXX",
 'whistle':    "PPPPPPPPPX",
 'phonation':  "XXXXXXXXSS",
 'percussive': "SXSPXXXXPX",
}
GRID_NOTES = {
 ('nasal','pharyngeal'):"A nasal needs an oral closure above a lowered velum. There is nothing above the pharynx to close.",
 ('nasal','glottal'):"The glottis sits below the velum, so air can never be routed through the nose from there.",
 ('trill','palatal'):"The tongue body is too massive to sustain aerodynamic flutter against the hard palate.",
 ('trill','velar'):"Same mass problem: the tongue body will not oscillate freely at the velum.",
 ('trill','glottal'):"Vocal folds vibrate, but that is phonation, not a trill of a supraglottal articulator.",
 ('lateral','bilabial'):"Lips have no side channel — there is no 'around' for the air to pass.",
 ('lateral','labiodental'):"Same as bilabial: no lateral channel exists at the lips.",
 ('lateral','uvular'):"Behind the velum the airway is a single tube with no sides to flow around.",
 ('lateral','pharyngeal'):"No lateral channel exists in the pharynx.",
 ('lateral','glottal'):"No lateral channel exists at the glottis.",
 ('click','labiodental'):"A click needs a sealed pocket between two closures; teeth and lip cannot form the front seal.",
 ('click','velar'):"The velum is already the back closure of every click, so it cannot also be the front one.",
 ('click','uvular'):"Behind the velar back closure there is no cavity left to rarefy.",
 ('click','pharyngeal'):"Too far back — the rarefiable pocket lies in front of the velum.",
 ('click','glottal'):"Too far back, and the glottis cannot seal a lingual cavity.",
 ('ejective','glottal'):"An ejective is powered by a raised closed glottis. The glottis cannot be both the piston and the valve.",
 ('implosive','pharyngeal'):"Implosives need a lowering larynx below an oral closure; the pharynx is not above the larynx.",
 ('implosive','glottal'):"Same conflict as the glottal ejective — one glottis cannot do both jobs.",
 ('whistle','glottal'):"Whistling needs a resonating cavity in front of a narrow jet. The glottis has neither.",
 ('phonation','bilabial'):"Phonation is what the larynx does. No other articulator has folds to vibrate.",
 ('phonation','alveolar'):"Phonation is what the larynx does. No other articulator has folds to vibrate.",
 ('phonation','velar'):"Phonation is what the larynx does. No other articulator has folds to vibrate.",
 ('percussive','labiodental'):"Nothing can strike here without also closing the airway.",
 ('percussive','postalveolar'):"Struck sounds need two hard surfaces meeting; the tongue behind the ridge is soft tissue against soft tissue.",
 ('percussive','palatal'):"No two hard surfaces meet here.",
 ('percussive','velar'):"No two hard surfaces meet here.",
 ('percussive','uvular'):"The uvula is soft tissue; it slaps but does not strike percussively.",
 ('percussive','glottal'):"Nothing strikes at the glottis.",
}

CATS={'Whistles Category':'Whistles','Basses Category':'Basses','Instruments Category':'Instruments',
 'Snares Category':'Snares','Liproll Category':'Liprolls','Kicks Category':'Kicks',
 'Hi Hats and Cymbals Category':'Hi-hats & cymbals','Clicks, Clops, and Pops Category':'Clicks, clops & pops',
 'Other Sounds Category':'Other sounds'}

ac=json.load(open(f'{S}/build/acoustics_sounds.json'))
acp=json.load(open(f'{S}/build/acoustics_patterns.json'))
spr=json.load(open(f'{S}/build/sprites.json'))
mp=json.load(open(f'{S}/ir_map.json'))

sounds=[]; offmap={}
for g,v in spr['sounds'].items():
    for k,off in v['map'].items(): offmap[k]=(g,off)

for o in mp:
    sid=os.path.splitext(os.path.basename(o['file']))[0]
    t=TAX[sid]; a=ac.get(o['file'],{})
    ai=air(t['airstream'])
    mn=manner_of(t['manner'],t['airstream'])
    cand=places_all(t['place'])
    if mn=='phonation':
        pl='pharyngeal' if any(w in t['place'].lower() for w in ('pharyng','aryepiglot')) else 'glottal'
    elif mn=='percussive' and place_of(t['place']) in ('glottal',):
        pl='pharyngeal'
    else:
        pl=place_of(t['place'])
        if GRID[mn][PLACES.index(pl)]=='X':
            alt=[p for p in cand if GRID[mn][PLACES.index(p)]!='X']
            if alt: pl=alt[0]
    g,off=offmap.get(sid,(None,None))
    NAME_FIX={
      'Normal/Pucker Whistle':('Pucker Whistle',['normal whistle']),
      'Pacmax/Whale/Train Whistle':('Train Whistle',['Pacmax whistle','whale whistle']),
      'Heartzel/Raik Whistle':('Raik Whistle',['Heartzel whistle']),
      'Whisper/Zekka Whistle':('Whisper Whistle',['Zekka whistle']),
      'Hard Bass/ Demon Bass/Hardcore Bass/Monster Bass/ Evil Bass':
        ('Hard Bass',['demon bass','hardcore bass','monster bass','evil bass']),
      'Trumpet / Trombone':('Trumpet',['trombone']),
      'Tongue Snare / 808':('Tongue Snare',['808 snare']),
      'Bdb Kick Roll / Double Kick / Triple Kick':('Bdb Kick Roll',['double kick','triple kick']),
      'Normal/Closed Hi Hat':('Closed Hi-Hat',['normal hi-hat']),
      'Mhs/Colaps Cymbal':('Collapse Cymbal',['Mhs cymbal']),
      'Bird/Beatfox/TrungBao Squeak':('Bird Squeak',['Beatfox squeak','TrungBao squeak']),
      'Vocal Roll/CTB Sound':('Vocal Roll',['CTB sound']),
      'KIM/Hutch Squeak':('Hutch Squeak',['KIM squeak']),
      'Siren/MixFx Roll':('Siren Roll',['MixFx roll']),
      'Od Bass (Least Bassy Bass XD)':('Od Bass',[]),
      '626 Effect (Stitch Special Sound)':('626 Effect',['Stitch sound']),
      'Kick (Classic Kick Drum)':('Classic Kick',[]),
      'Frosty Sound (Meow Squeak Roll)':('Frosty Sound',['meow squeak roll']),
      'Guzheng (Chinese Instrument)':('Guzheng',[]),
      '808 Kick Bass (Outward Sub Bass)':('808 Kick Bass',['outward sub bass']),
    }
    nm=o['name']; alias=[]
    if nm in NAME_FIX: nm,alias=NAME_FIX[nm]
    sounds.append(dict(
      id=sid, name=nm.strip(), alias=alias, cat=CATS[o['category']], role=t['role'],
      sbn=t['sbn'], ipa=t['ipa'], place=t['place'], places=places_all(t['place']),
      manner=t['manner'], gplace=pl, gmanner=mn,
      air=ai['code'], fams=ai['fams'], prim=ai['prim'], dirs=ai['dirs'],
      voice=t['voice'], inst=t['inst'], diff=t['diff'], lang=t['lang'],
      howto=t['howto'], notes=t.get('notes',''),
      grp=g, off=off, src=o['file'],
      ac={k:a[k] for k in ('dur','f05','f25','f50','f75','f95','centroid','flatness','f0','hnr',
            'attack_ms','decay_ms','sustain','voiced','fpeak','events','ev_rate') if k in a},
      spec=a.get('spec',[]), wave=[round(x,2) for x in a.get('wave',[])[:72]],
    ))

# sanity: any sound landing on an "impossible" cell?
bad=[(s['id'],s['gmanner'],s['gplace']) for s in sounds
     if GRID[s['gmanner']][PLACES.index(s['gplace'])]=='X']
print('sounds on impossible cells:',len(bad)); [print('  ',b) for b in bad]

patoff={}
for g,v in spr['patterns'].items():
    for k,off in v['map'].items(): patoff[k]=(g,off)
from pat_names import NAMES as PAT_NAMES, LEGENDS as PAT_LEGENDS
LEVEL={'Basic Patterns':('Basic',1),'14 Intermediate Patterns':('Intermediate',2),
 '14 Advanced Patterns':('Advanced',3),'CJ Technical Patterns':('Technical — CJ',4)}
pats=[]
for p in json.load(open(f'{S}/ir_patterns.json')):
    pid=re.sub(r'[^a-z0-9]+','-',os.path.splitext(p['file'][len('patterns/'):])[0].lower()).strip('-')
    g,off=patoff.get(pid,(None,None))
    sp=p['source_page']
    lvl,ord_=LEVEL.get(sp,('Technical — Helium',5))
    a=acp.get(p['file'],{})
    notation=p['notation']; legend=[]
    if pid in PAT_LEGENDS: legend,notation=PAT_LEGENDS[pid]
    pats.append(dict(id=pid,name=PAT_NAMES.get(pid,p['name']),ref=p['name'],
      notation=notation,legend=legend,level=lvl,ord=ord_,page=sp,
      grp=g,off=off,src=p['file'],
      ac={k:a[k] for k in ('dur','centroid','f0','ev_rate','events') if k in a},
      wave=[round(x,2) for x in a.get('wave',[])[:72]]))
pats.sort(key=lambda x:(x['ord'], int(re.search(r'(\d+)',x['name']).group(1)) if re.search(r'(\d+)',x['name']) else 0))

INSTR=[
 dict(n='TR-808 kick',lo=40,hi=80,k='perc'), dict(n='Acoustic kick drum',lo=45,hi=200,k='perc'),
 dict(n='Double bass',lo=41,hi=262,k='pitch'), dict(n='Bass guitar',lo=41,hi=392,k='pitch'),
 dict(n='Cello',lo=65,hi=520,k='pitch'), dict(n='Snare drum (body)',lo=150,hi=250,k='perc'),
 dict(n='Trombone',lo=82,hi=520,k='pitch'), dict(n='Trumpet',lo=165,hi=1175,k='pitch'),
 dict(n='Singing voice (bass→soprano)',lo=82,hi=1050,k='pitch'),
 dict(n='Violin',lo=196,hi=3136,k='pitch'), dict(n='Piccolo',lo=587,hi=4186,k='pitch'),
 dict(n='Piano',lo=27.5,hi=4186,k='pitch'),
]
SPECTRAL=[
 dict(n='Acoustic kick drum',lo=30,hi=5000), dict(n='TR-808 kick',lo=30,hi=400),
 dict(n='Snare drum',lo=100,hi=12000), dict(n='Closed hi-hat',lo=300,hi=16000),
 dict(n='Crash cymbal',lo=200,hi=18000), dict(n='Woodblock / clave',lo=800,hi=9000),
]
EDGES=[]
import math
for i in range(57): EDGES.append(round(math.exp(math.log(30)+ (math.log(16000)-math.log(30))*i/56),1))

out=dict(sounds=sounds,patterns=pats,sprites=spr,grid=GRID,gridNotes={f'{m}|{p}':v for (m,p),v in GRID_NOTES.items()},
         places=PLACES,manners=MANNERS,instr=INSTR,spectral=SPECTRAL,edges=EDGES)
os.makedirs(f'{S}/out',exist_ok=True)
with open(f'{S}/out/data.js','w',encoding='utf-8') as fh:
    fh.write('window.BBX=');json.dump(out,fh,ensure_ascii=False,separators=(',',':'));fh.write(';')
print('data.js %.0f KB'%(os.path.getsize(f'{S}/out/data.js')/1024))
from collections import Counter
print('prim families:',Counter(s['prim'] for s in sounds))
print('grid manners:',Counter(s['gmanner'] for s in sounds))
print('grid places:',Counter(s['gplace'] for s in sounds))
cells={(s['gmanner'],s['gplace']) for s in sounds}
print('cells occupied:',len(cells),'of',len(GRID)*10)
pitched=[s for s in sounds if s['ac'].get('f0',0)>0 and s['ac'].get('voiced',0)>0.35]
print('pitched:',len(pitched),'f0 range %.0f-%.0f Hz'%(min(p['ac']['f0'] for p in pitched),max(p['ac']['f0'] for p in pitched)))
print('patterns:',len(pats),Counter(p['level'] for p in pats))
