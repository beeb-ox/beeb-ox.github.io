(function(Z){
Z.sounds=Z.sounds||{};
var S=Z.sounds;
S["whistle"]={name:"收唇口哨",
 howto:"双唇收圆成一个小开口，舌位放低放平，稳定吹气。音高由舌前方口腔的容积决定，而不是声带——喉部完全不发声。",
 notes:"这是一个亥姆霍兹共鸣器：口腔是腔体，唇的开口是颈部。因为完全不用声带，所以可以一边吹哨一边哼唱。"};
S["cricket-whistle"]={name:"蟋蟀哨",
 howto:"在舌尖与齿龈脊之间做出极窄的通道，吹气力度大到气流开始「啾」地断续而不是持续发音。短促快速的爆发，约在 3 kHz。"};
S["bolbol-whistle"]={name:"夜莺哨",
 howto:"先正常吹哨，然后在舌后加入水或唾液，让气流产生抖动。名字来自波斯语的 bolbol（夜莺）。",
 notes:"这是全档案中持续时间最长的一段口哨——它展示的是气息控制，而不是一个节奏性的声音。"};
S["beat-rhino-whistle"]={name:"Beat Rhino 哨",
 howto:"把收唇口哨超吹，让共鸣器跳到第二个模态——音色更亮更细，大约高出一个八度。名字来自节奏口技手 Beat Rhino。"};
S["ball-zee-whistle"]={name:"Ball-Zee 哨",
 howto:"吹哨的同时保持一个软腭处的紧缩，让摩擦噪声骑在哨音之上。由 Ball-Zee 推广。"};
S["laser-whistle"]={name:"激光哨",
 howto:"吹哨时快速把舌体前后移动，缩小前腔以让音高跳跃。陡峭的滑移正是它听起来像激光的原因。",
 notes:"实测频谱呈一片抹开的形状而不是一个尖峰，因为基频在 100 毫秒内就跨过了一个多八度。"};
S["inward-teeth-whistle"]={name:"吸气齿哨",
 howto:"下唇略微后缩，把空气经上门齿吸入。吸气式口哨让你可以一边吹旋律一边呼吸。",
 notes:"这是节奏口技绕过呼吸限制的两条路之一：声音在吸气时产生，所以一条线可以无限延续。"};
S["outward-teeth-whistle"]={name:"呼气齿哨",
 howto:"在舌尖与上齿之间吹气，而不是从收圆的双唇吹出。比收唇口哨更亮、更轻，也更容易快速衔接。"};
S["pacmax-whale-train-whistle"]={name:"火车汽笛哨",
 howto:"故意让唇开口不稳定，使共鸣器的两个模态同时发声，然后弯音。名字来自 Pacmax。"};
S["recorder-whistle"]={name:"竖笛哨",
 howto:"吹哨时把舌头抬高前推贴近硬腭，形成一条窄管，模仿竖笛的哨口。音色纯净，几乎没有气息噪声。"};
S["bird-whistle"]={name:"鸟哨",
 howto:"极小的唇开口、极高的舌位，再用下巴和舌体做快速的音高弹动。位置在 3 kHz 左右——档案中有音高声音的上限区。"};
S["finger-whistle"]={name:"手指哨",
 howto:"用一两根手指把舌头往后折，再对着形成的边缘吹气。手指承担了平时由唇完成的工作，这也是它响得多的原因。",
 notes:"这是人的嘴在没有扩音条件下能发出的最响的声音——也是本档案里唯一一个声学上限由手指而非声道决定的条目。"};
S["dekoy-whistle"]={name:"Dekoy 哨",
 howto:"在咽部紧缩的状态下吹哨，让哨音带上一层沙哑。名字来自节奏口技手 Dekoy。"};
S["ralik-whistle"]={name:"Raik 哨",
 howto:"吹哨时让声带略微张开，使哨音下面垫着一层气声。名字来自 Heartzel / Raik。"};
S["vortex-whistle"]={name:"涡流哨",
 howto:"吹哨的同时让气流在舌侧打旋，使哨音被一层嘶声包住。"};
S["calexy-babeli whistle"]={name:"Calexy 哨",
 howto:"把下巴大幅张开、舌位放低以扩大共鸣腔，把哨音压到 440 Hz 附近。名字来自 Calexy / Babeli。",
 notes:"这是档案中实测最低的口哨——基本就是口腔亥姆霍兹共鸣器的实际下限。"};
S["hollow-whistle"]={name:"空腔哨",
 howto:"吹哨时把喉位放低、咽腔扩张。多出来的后腔会带来一种空、木质的色彩，并把音高压低。"};
S["tongue-flute"]={name:"舌笛",
 howto:"把舌头卷成一个管，像吹长笛吹口那样对着它吹气，双唇只是松松地参与。"};
S["throat-whistle"]={name:"喉哨",
 howto:"张开嘴，把小舌处的气道收窄到它自己开始发哨音。共鸣腔在舌后方，而不是舌前方。",
 notes:"这是一个罕见的反转——哨音声源在后方，因此音高由咽部而不是双唇控制。"};
S["cyclone-whistle"]={name:"旋风哨",
 howto:"吹哨的同时让唾液或舌侧打旋，使哨音被几十赫兹量级的调制包裹。"};
S["whisper-zekka-whistle"]={name:"轻声哨",
 howto:"用刚好还能维持哨音的最小气流吹奏。用来在不丢掉旋律的前提下把力度降下来。名字来自 Zekka。"};
S["whale-whistle"]={name:"鲸哨",
 howto:"吹哨并在一个大音程内持续滑移，中间不断气，让音高始终不落定。"};
S["double-voice"]={name:"双声口哨",
 howto:"同时吹哨和哼唱。哨音由唇开口驱动，哼唱由声带驱动，所以两个音高是真正彼此独立的。",
 notes:"这是人类真实复调最清楚的例子：两个独立声源、两个独立音高，一个人完成。"};
S["helium-whistle"]={name:"Helium 哨",
 howto:"把舌头抬高前推，把前腔缩到最小，从而把哨音顶到音域最高处。名字来自 Helium，与氦气无关。"};
S["hand-whistle"]={name:"手掌哨",
 howto:"两手合成一个密闭腔，对着两个拇指之间的缝隙吹气，再张开一根手指来改变音高。",
 notes:"这是全档案里唯一一个共鸣腔在身体之外的声音——也是「人类声音」这个范畴的极限个案。"};
})(window.BBX_I18N.zh);
