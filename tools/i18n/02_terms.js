(function(Z){
var U=Z.ui;
U["lim.1.h"]="最低的那个八度是缺的";
U["lim.1.p"]="本档案中实测到的最低音高是 {lowHz} Hz，来自「{lowName}」。五弦电贝斯能到 31 Hz，TR-808 底鼓通常调在 40 Hz。次谐波发声能让人声比常态音域再低大约一个八度，但越往下振幅塌得越快，而且声带没法临时变长变重。";
U["lim.1.v"]="实测：{nPitched} 段有音高录音中的最低基频";
U["lim.2.h"]="吊镲的余音撑不住";
U["lim.2.p"]="档案里最长的吊镲衰减是 {cymS} 秒，来自「{cymName}」。真正的 18 吋 crash 能响两到四秒，因为金属片会把能量存起来再慢慢放出去。气流噪声没有这个「存储」：气一停，声就断。";
U["lim.2.v"]="实测：首个起音点从峰值降到 −20 dB 的时间";
U["lim.3.h"]="高频段其实比听起来更薄";
U["lim.3.p"]="这里最明亮的声音「{brightName}」，重心在 {brightHz} Hz——确实已经进了踩镲的地盘。但音高最高的声音也只到 {highHz} Hz，低于短笛的最高音；而在真实吊镲仍有内容的 16 kHz 以上，档案里没有任何声音带着可用的能量。";
U["lim.3.v"]="实测：全部 200 段录音的频谱重心与基频";
U["lim.4.h"]="复调到三个声部就到顶了";
U["lim.4.p"]="口腔一共只有三个彼此独立的声源：声带、一个口腔或舌部振动体、以及口哨。三者同时启动就是天花板，本档案里只有少数几个声音做到了。弦乐四重奏有四个人，乐队有六十个；一个人没法用三种独立音色奏出一个三和弦。";
U["lim.4.v"]="推算：档案中有 {poly} 个声音叠加了两个以上同时声源";
U["lim.5.h"]="有些发音方式根本没有被造出来";
U["lim.5.p"]="在覆盖表上，{cells} 个部位—方法组合里有 {imposs} 个是被解剖结构排除的，而不是因为没人练。双唇没有侧向通道；咂舌音的软腭闭合之后没有可抽负压的腔体；而声门不可能既当挤喉音的活塞又当它的阀门。这些格子练多久都打不开。";
U["lim.5.v"]="解剖原因：每一格的具体理由见覆盖表";
U["lim.6.h"]="呼吸才是真正的约束——也是最聪明的绕道";
U["lim.6.p"]="200 个声音里有 {noLung} 个完全不需要肺部气流：它们靠舌部气流、面颊气流，或者干脆在吸气时发出。这不是花招，而是整套工程解法。这正是节奏口技能在十六分音符底下把一条贝斯线撑上好几分钟的原因，也是纯靠肺部气流的人做不到的原因。";
U["lim.6.v"]="推算：气流机制不含肺部的声音";
U["lim.7.h"]="发音速率有机械上限";
U["lim.7.p"]="这里测到的最快持续滚奏是每秒 {rate} 次（「{rateName}」）。日常说话大约每秒六到八个音节；滚奏能超过它，只是因为舌尖或唇的行程只有说话时的一小部分。再往上推，发音器官就来不及复位了。";
U["lim.7.v"]="实测：60 毫秒最小间隔的起音检测，仅统计 2 秒以上的录音";
U["lim.8.h"]="音量不在这份数据里";
U["lim.8.p"]="这些录音没有经过声压校准，所以这里没有任何数据能告诉你一个嘴打的底鼓比起真正的大鼓有多响。诚实的答案是：差得远。大鼓要推动一整张大鼓面和三十升的腔体空气。现场节奏口技之所以成立，是因为有麦克风；这一页上任何相反的说法都只能是编的。";
U["lim.8.v"]="这份档案无法测量——作为已知缺口如实标出";

Z.gridNotes={
 "nasal|pharyngeal":"鼻音需要在下降的软腭之上有一处口腔闭合。而咽之上没有任何可以闭合的东西。",
 "nasal|glottal":"声门位于软腭之下，气流永远不可能从那里改道进鼻腔。",
 "trill|palatal":"舌体质量太大，无法在硬腭处维持气动颤动。",
 "trill|velar":"同样是质量问题：舌体不会在软腭处自由振动。",
 "trill|glottal":"声带确实会振动，但那是发声，而不是某个声门上发音器官的颤动。",
 "lateral|bilabial":"双唇没有侧向通道——气流没有「绕过去」的余地。",
 "lateral|labiodental":"与双唇同理：唇部不存在侧向通道。",
 "lateral|uvular":"软腭之后气道是单一管腔，没有侧壁可绕。",
 "lateral|pharyngeal":"咽部不存在侧向通道。",
 "lateral|glottal":"声门处不存在侧向通道。",
 "click|labiodental":"咂舌音需要在两处闭合之间形成密闭腔；牙齿与唇无法构成前闭合。",
 "click|velar":"软腭本来就是每个咂舌音的后闭合，因此它不可能同时充当前闭合。",
 "click|uvular":"在软腭后闭合之后，已经没有可以抽成负压的腔体了。",
 "click|pharyngeal":"位置太后——可抽负压的腔体在软腭前方。",
 "click|glottal":"位置太后，而且声门无法密封一个舌部腔体。",
 "ejective|glottal":"挤喉音的动力来自上抬的闭合声门。声门不可能既是活塞又是阀门。",
 "implosive|pharyngeal":"内爆音需要在某处口腔闭合之下有喉部下降；而咽并不在喉之上。",
 "implosive|glottal":"与声门挤喉音是同一个矛盾——一个声门干不了两份活。",
 "whistle|glottal":"吹哨需要在细窄气流前方有一个共鸣腔。声门两者都没有。",
 "percussive|labiodental":"这里没有东西能在不封住气道的前提下相互敲击。",
 "percussive|postalveolar":"敲击音需要两个硬面相碰；齿龈脊后方是软组织对软组织。",
 "percussive|palatal":"这里没有两个硬面能相碰。",
 "percussive|velar":"这里没有两个硬面能相碰。",
 "percussive|uvular":"小舌是软组织，它会拍打，但不会形成敲击音。",
 "percussive|glottal":"声门处没有任何东西可以敲击。",
 "phonation|bilabial":"发声是喉的工作。别的发音器官都没有可振动的褶皱。",
 "phonation|alveolar":"发声是喉的工作。别的发音器官都没有可振动的褶皱。",
 "phonation|velar":"发声是喉的工作。别的发音器官都没有可振动的褶皱。"};

Z.placeAtom={
 "labial":"唇","bilabial":"双唇","labiodental":"唇齿","dental":"齿","alveolar":"齿龈",
 "postalveolar":"龈后","palatal":"硬腭","velar":"软腭","uvular":"小舌",
 "pharyngeal":"咽","epiglottal":"会厌","laryngeal":"喉","glottal":"声门","lateral":"舌侧",
 "(pucker)":"收圆","(finger-assisted)":"手指辅助","(hand cavity)":"手掌腔",
 "(upper lip)":"上唇","(lower lip)":"下唇","(mid-tongue)":"舌中","(tongue side)":"舌侧",
 "(blade)":"舌叶","(rounded)":"圆唇","(saliva-loaded)":"含唾液","(saliva)":"含唾液",
 "(external)":"体外"};

Z.mannerAtom={
 "plosive":"塞音","affricate":"塞擦音","fricative":"擦音","nasal":"鼻音","trill":"颤音",
 "click":"咂舌音","ejective":"挤喉音","implosive":"内爆音","whistle":"口哨",
 "phonation":"发声","percussive":"敲击音","oscillation":"振动","flutter":"抖振",
 "aspiration":"送气","friction":"摩擦噪声","glide":"滑移","roll":"滚奏","vibrato":"颤振",
 "squeak":"尖啸","subharmonic":"次谐波","falsetto":"假声","voice":"人声","bass":"贝斯",
 "buzz":"蜂鸣","resonance":"共鸣","tongue":"舌","compound":"复合","lip buzz":"唇振",
 "lip oscillation":"唇振","tongue slap":"舌拍","tongue oscillation":"舌振",
 "glottal release":"声门除阻","creaky phonation":"嘎裂发声","creaky squeak":"嘎裂尖啸",
 "aspirated plosive":"送气塞音","aspirated stop":"送气塞音","double aspiration":"双重送气",
 "double click":"双咂舌音","double oscillation":"双重振动","compound oscillation":"复合振动",
 "ejective affricate":"挤喉塞擦音","ejective fricative":"挤喉擦音","ejective plosive":"挤喉塞音",
 "ejective cluster":"挤喉音连缀","ejective tongue slap":"挤喉舌拍",
 "unreleased ejective":"不除阻挤喉音","ingressive click":"吸气咂舌音",
 "pluck-like click":"拨弦式咂舌音","reed-like oscillation":"簧片式振动",
 "subharmonic phonation":"次谐波发声","two-pitch phonation":"双音高发声",
 "two-register phonation":"双声区发声","three-source polyphony":"三声源复调",
 "two-rate oscillation":"双速率振动","voiced fricative":"浊擦音","voiced trill":"浊颤音",
 "affricate over voice":"叠在人声之上的塞擦音","click over bass":"叠在贝斯之上的咂舌音",
 "whistle over voice":"叠在人声之上的口哨","affricate with vowel colour":"带元音色彩的塞擦音",
 "ejective into sustained bass":"挤喉音接持续贝斯","ejective with pharyngeal onset":"带咽部起音的挤喉音",
 "pitched tail":"带音高的尾音","resonant tail":"共鸣尾音","falling resonance":"下行共鸣",
 "resonance glide":"共鸣滑移","sung note":"歌唱音",
 "(oscillation)":"振动","(rolled)":"滚奏","(glide)":"滑移","(sub)":"超低","(rapid)":"快速",
 "(very rapid)":"极快","(harsh)":"粗糙","(distorted)":"失真","(modulated)":"调制",
 "(wet)":"多唾液","(low)":"低","(high)":"高","(very high)":"极高","(thin)":"纤细",
 "(clean)":"干净","(noisy)":"多噪声","(double)":"双重","(double-rate)":"双倍速率",
 "(lateral)":"舌侧","(buccal)":"口腔气流","(breathy)":"气声","(accented)":"带重音",
 "(alternating)":"交替","(aryepiglottic)":"喉会厌","(buzzy)":"蜂鸣感","(chopped)":"切断",
 "(delayed)":"延后","(double closure)":"双闭合","(double glide)":"双重滑移",
 "(embouchure)":"号嘴式","(external resonator)":"体外共鸣腔","(false-fold)":"假声带",
 "(falsetto glide)":"假声滑移","(formant-swept)":"共振峰扫频","(ingressive)":"吸气",
 "(large cavity)":"大腔体","(long)":"长","(multi-tone)":"多音","(overblown)":"超吹",
 "(portamento)":"连续滑音","(pulsed)":"脉冲式","(raised larynx)":"喉位上抬",
 "(rolled falsetto)":"假声滚奏","(rounded)":"圆唇","(scrubbed)":"来回搓动",
 "(square-ish)":"近方波","(squeezed)":"挤压","(struck)":"敲击","(swept)":"扫频",
 "(tongue)":"舌","(trilled glide)":"颤动滑移","(triplet)":"三连音","(velum)":"软腭",
 "(very quiet)":"极轻","(voiced)":"浊","(wide glide)":"大幅滑移","(sub, clean)":"超低、干净",
 "(rolled, low)":"滚奏、低","(rolled, very low)":"滚奏、极低","(sub, rolled)":"超低、滚奏",
 "(harsh, wet)":"粗糙、多唾液"};
Z.mannerPhrase={
 "whistle (whistle)":"口哨",
 "oscillation (tongue)":"舌部振动",
 "trill (oscillation)":"颤动式振动"};

Z.instAtom={
 "snare":"军鼓","kick":"底鼓","clap":"掌声","rim":"鼓边","rimshot":"打边","rimclick":"敲边",
 "rim click":"敲边","sub bass":"超低贝斯","bass":"贝斯","sub":"超低音","sub sine":"超低正弦",
 "808":"808","808 kick":"808 底鼓","808 snare":"808 军鼓","808 sub":"808 超低音",
 "808 sub bass":"808 超低贝斯","808 boom":"808 轰鸣","tr-808 kick":"TR-808 底鼓",
 "tr-808 snare":"TR-808 军鼓","tr-909 kick":"TR-909 底鼓","tr-909 snare":"TR-909 军鼓",
 "acoustic kick drum":"原声底鼓","acoustic snare":"原声军鼓","deep kick":"深沉底鼓",
 "gated kick":"门限底鼓","gated snare":"门限军鼓","gated hi-hat":"门限踩镲",
 "kick roll":"底鼓滚奏","triple kick":"三连底鼓","double":"双击","double snare":"双军鼓",
 "double-time bass":"倍速贝斯","flam":"装饰音","ghost note snare":"幽灵音军鼓",
 "tight snare":"紧实军鼓","muffled snare":"闷军鼓","distorted snare":"失真军鼓",
 "layered snare":"叠层军鼓","layered big snare":"叠层大军鼓","layered bass":"叠层贝斯",
 "layered growl bass":"叠层咆哮贝斯","big snare":"大军鼓","big room snare":"大厅军鼓",
 "house snare":"House 军鼓","club":"俱乐部风","laid-back snare":"拖后军鼓",
 "snare roll":"军鼓滚奏","snare with reverb":"带混响的军鼓","snare with room":"带房间感的军鼓",
 "snare with flanger":"带镶边效果的军鼓","closed hi-hat":"闭镲","open hi-hat":"开镲",
 "soft hi-hat":"柔和踩镲","muted hi-hat":"闷踩镲","sliced":"切片","trap hi-hat":"Trap 踩镲",
 "trap hi-hat roll":"Trap 踩镲滚奏","hats":"踩镲","brush":"刷","egg shaker":"蛋沙锤",
 "maraca":"沙球","high shaker":"高音沙锤","crash cymbal":"吊镲","brushed cymbal":"刷镲",
 "choked cymbal":"掐镲","reverse cymbal":"倒放镲","ride wash":"叮叮镲铺底",
 "woodblock":"木鱼","low woodblock":"低音木鱼","deep woodblock":"深沉木鱼",
 "woodblock roll":"木鱼滚奏","clave":"响棒","clave roll":"响棒滚奏",
 "clave over sub bass":"叠在超低贝斯上的响棒","horse clop":"马蹄声","tom":"通鼓",
 "floor tom":"落地鼓","taiko":"太鼓","talking drum":"会说话的鼓","impact":"冲击音",
 "punch":"拳击音","cannon":"炮声","cardboard box":"纸箱","pop":"爆破音",
 "double bass":"低音提琴","upright bass":"立式贝斯","contrabass":"倍低音提琴",
 "cello":"大提琴","violin":"小提琴","pizzicato strings":"拨奏弦乐","electric guitar":"电吉他",
 "guzheng":"古筝","pipa":"琵琶","trumpet":"小号","piccolo trumpet":"高音小号",
 "trombone":"长号","brass":"铜管","saxophone":"萨克斯","reed":"簧片",
 "flute":"长笛","bass flute":"低音长笛","breathy flute":"气声长笛","fipple flute":"哨口笛",
 "overtone flute":"泛音笛","recorder":"竖笛","ney":"奈伊笛","shakuhachi":"尺八",
 "ocarina":"陶笛","ocarina trill":"陶笛颤音","piccolo":"短笛","slide whistle":"滑音哨",
 "referee whistle":"裁判哨","train whistle":"火车汽笛","whistle lead":"口哨主奏",
 "kazoo":"卡祖笛","bulb horn":"气囊喇叭","clown horn":"小丑喇叭","duck call":"鸭哨",
 "duck call roll":"鸭哨滚奏","bird call":"鸟哨","insect":"昆虫声","cat":"猫叫",
 "owl hoot":"猫头鹰叫","whale song":"鲸歌","water drop":"水滴","bubbles":"气泡",
 "bubble fx":"气泡音效","water fx":"水声效果","liquid":"液体感","wind":"风声",
 "steam":"蒸汽","kettle":"水壶哨","motor":"马达","engine":"引擎","siren":"警笛",
 "theremin":"特雷门琴","laser":"激光音","riser":"上升音","high riser":"高音上升",
 "fx sweep":"效果扫频","fx roll":"效果滚奏","zipper":"拉链音","turntable scratch":"唱盘搓盘",
 "vinyl noise":"黑胶噪声","choir":"合唱","pad":"铺底音","analogue synth pad":"模拟合成器铺底",
 "two-part harmony":"二声部和声","soft sine":"柔和正弦","sine lead":"正弦主奏",
 "synth lead":"合成器主奏","lead":"主奏","synth blip":"合成器短音","synth stab":"合成器插入音",
 "synth zap":"合成器电击音","synth bass sweep":"合成器贝斯扫频","synth pitch sweep":"合成器音高扫频",
 "synth arpeggio":"合成器琶音","chiptune":"芯片音乐","chiptune bass":"芯片贝斯",
 "fm synth":"FM 合成器","vocoder":"声码器","ring modulator":"环形调制器",
 "bitcrushed bass":"比特压缩贝斯","acid bass":"Acid 贝斯","electro":"Electro",
 "electro bass line":"Electro 贝斯线","reese bass":"Reese 贝斯","wobble bass":"摇摆贝斯",
 "dubstep bass":"Dubstep 贝斯","brostep":"Brostep","dub bass":"Dub 贝斯",
 "dub sub bass":"Dub 超低贝斯","grimy bass":"脏音贝斯","growl":"咆哮","growl bass":"咆哮贝斯",
 "drill":"电钻","distorted":"失真","distortion":"失真","distorted sub":"失真超低音",
 "mid bass":"中低频贝斯","punchy bass":"有力贝斯","clean sub bass":"干净超低贝斯",
 "soft sub":"柔和超低音","moog":"Moog","air":"气流声","alien fx":"外星音效",
 "alien voice":"外星人声","cartoon":"卡通音","squeal":"尖叫","reverb tail":"混响尾音",
 "pitched-up vocal sample":"升调人声采样","milky":"乳白质感",
 "(distorted)":"失真","(inhaled)":"吸气","(triplet rolls)":"三连音滚奏"};

Z.legend={
 "X = any sound you feel fits":"X ＝ 任何你觉得合适的声音",
 "Bm = bass kick":"Bm ＝ 贝斯底鼓",
 "(KQ) = K snare with a duck sound (big brr)":"(KQ) ＝ 带鸭音的 K 军鼓（大 brr）"};
})(window.BBX_I18N.zh);
(function(Z){
Z.alias={
 "normal whistle":"普通口哨","Pacmax whistle":"Pacmax 哨","whale whistle":"鲸哨",
 "Heartzel whistle":"Heartzel 哨","Zekka whistle":"Zekka 哨",
 "demon bass":"恶魔贝斯","hardcore bass":"硬核贝斯","monster bass":"怪物贝斯",
 "evil bass":"邪恶贝斯","trombone":"长号","808 snare":"808 军鼓",
 "double kick":"双底鼓","triple kick":"三连底鼓","normal hi-hat":"普通踩镲",
 "Mhs cymbal":"Mhs 镲","Beatfox squeak":"Beatfox 尖啸","TrungBao squeak":"TrungBao 尖啸",
 "CTB sound":"CTB 音","KIM squeak":"KIM 尖啸","MixFx roll":"MixFx 滚奏",
 "Stitch sound":"史迪奇音","meow squeak roll":"猫叫尖啸滚奏","outward sub bass":"呼气超低贝斯"};
})(window.BBX_I18N.zh);
