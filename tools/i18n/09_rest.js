(function(Z){
var S=Z.sounds;
/* ---- liprolls ---- */
S["electro-liproll"]={name:"Electro 唇滚",
 howto:"滚动双唇，上面叠一层明亮的齿龈嗡鸣，然后靠打断滚奏、而不是重新起振来做出节奏。",
 notes:"唇滚同时是贝斯线和鼓点：滚奏是连续的，节奏是切进去的。"};
S["punchy-liproll"]={name:"有力唇滚",
 howto:"滚奏时用横膈膜做出周期性的强重音，让每一拍都成为独立的击点。"};
S["growling-liproll"]={name:"咆哮唇滚",
 howto:"在唇滚上加一个小舌咆哮，让两个振荡器互相打拍。"};
S["808-sub-liproll"]={name:"808 超低唇滚",
 howto:"把唇滚调到双唇还能振动的最低处，喉位压低、咽腔全开。"};
S["just-sub-liproll"]={name:"纯超低唇滚",
 howto:"不带失真也不带咆哮的低滚奏——只要重量。用在旋律段落底下。"};
S["thin-teeth-liproll"]={name:"纤细齿唇滚",
 howto:"让下唇对着上齿滚动，而不是唇对唇，这会削薄音色并加快拍打速率。"};
S["8-bit-liproll"]={name:"8-Bit 唇滚",
 howto:"滚奏时在硬腭做强烈紧缩，让波形方起来，听上去像游戏主机。"};
S["yoi-sub-liproll"]={name:"Yoi 超低唇滚",
 howto:"一个圆唇的超低滚奏，整句带着上行的「yoi」元音色彩。"};
S["hi-vocalized-liproll"]={name:"高音带声唇滚",
 howto:"一边滚动双唇一边唱一个高音，让贝斯和旋律同时出来。"};
S["x2-liproll"]={name:"倍速唇滚",
 howto:"把滚奏推到平常两倍的拍打速率，并在上面做倍速的节奏型。"};
S["blaze-it-up-liproll"]={name:"Blaze It Up 唇滚",
 howto:"一段长而厚重的滚奏，整个小节里做扫过式的元音变化——这是「blaze it up」套路的标志。"};
S["teeth-liproll"]={name:"齿唇滚",
 howto:"让下唇骑在上齿上滚动。实测是档案中最快的滚奏之一，约每秒 10 次拍打。"};
S["grimy-teeth-liproll"]={name:"脏音齿唇滚",
 howto:"带喉部失真的齿唇滚，做出 grime 和 dubstep 套路里的那种脏音。"};
S["hollow-liproll"]={name:"空腔唇滚",
 howto:"用最大的咽腔空间滚奏，让音色圆润、带木质感，而不是嗡嗡的。"};
S["low-hollow-liproll"]={name:"低空腔唇滚",
 howto:"把空腔滚奏的喉位再压低，进入超低频区。"};
S["tongue-hollow-liproll"]={name:"舌空腔唇滚",
 howto:"同时托住一个口腔气流的舌滚和一个唇滚，一个靠面颊气流，一个靠肺部气流。"};
S["tongue-punchy-liproll"]={name:"舌有力唇滚",
 howto:"舌滚在拍点上做强重音，同时双唇维持持续音。"};
S["tongue-808-sub-liproll"]={name:"舌 808 超低唇滚",
 howto:"由舌头驱动的超低滚奏，每个重音都带一个 808 式的调音衰减。"};
S["tongue-just-sub-liproll"]={name:"舌纯超低唇滚",
 howto:"一个纯口腔气流的超低滚奏，完全没有唇的成分。因为肺是空闲的，你可以透过它呼吸。"};
S["double-liproll"]={name:"双唇滚",
 howto:"让上唇和下唇以不同速率同时拍打，产生两个贝斯音高。"};
/* ---- other sounds ---- */
S["abx-roll"]={name:"ABX 滚奏",
 howto:"一个标志性的复合滚奏，把唇、小舌与喉部振动合在一起。名字来自节奏口技手 ABX。",
 notes:"尽管有三个同时工作的振荡器，实测能量几乎全部在 200 Hz 以下。"};
S["abx-polyphonic"]={name:"ABX 复调",
 howto:"托住 ABX 滚奏、发出一个音，再在两者之上吹出第三条线。",
 notes:"三个彼此独立的声源同时工作——已经接近人类复调的实际天花板。"};
S["bird-squeak"]={name:"鸟鸣尖啸",
 howto:"把声门掐到几乎闭合，让一丝极高的尖啸漏出来。名字来自 Beatfox 和 TrungBao。",
 notes:"实测接近 4.8 kHz——档案中音高最高的声音。"};
S["vocal-roll(ctb)"]={name:"人声滚奏",
 howto:"一个极快的颤音滚奏，用作质感而不是辅音。CTB 指的是中文圈的 Chinese Tongue Bass 风格。"};
S["double-sound"]={name:"双声",
 howto:"让真声带与假声带以不同速率振动，使两个音高同时发声。",
 notes:"这是真正的喉部复调，不是错觉。两个音高在频谱里都能测出来。"};
S["inward-double-voice"]={name:"吸气双声",
 howto:"在吸气时做出同样的双音高发声，于是一个和声可以跨过换气点继续保持。"};
S["baby-voice"]={name:"童声",
 howto:"抬高喉位、把整条声道缩小，让共振峰随音高一起上移——这正是「小身体」的声学特征。"};
S["duck-sound"]={name:"鸭叫",
 howto:"挤压咽部，在圆唇的状态下让小舌嗡鸣，做出带鼻音的嘎嘎声。"};
S["duck-roll"]={name:"鸭叫滚奏",
 howto:"把鸭叫持续下来，并作为滚奏做出节奏。"};
S["polyphonic"]={name:"复调人声",
 howto:"同时哼唱和吹哨两个不同的音。两个声源在机制上彼此独立，所以真正的音程是可能的。",
 notes:"这是一个人做出二声部复调最干净的证明——也是「人声是单声部的」这句话并不完全成立的原因。"};
S["o-synth"]={name:"O 合成器",
 howto:"托住一个「o」元音，同时移动舌头和下巴让共振峰像合成器上打开滤波器那样扫过去。",
 notes:"声道的滤波扫频在物理上与合成器的低通扫频是同一件事——口腔就是一组共振滤波器。"};
S["bubble-roll-dlow"]={name:"气泡滚奏",
 howto:"唇部积着唾液做滚奏，让振动破碎成一颗颗离散的气泡。由 D-Low 推广。"};
S["zipper"]={name:"拉链音",
 howto:"颤动舌尖，并让共鸣向上扫，使嗡鸣像拉链被拉起来那样上行。"};
S["dlow-zipper"]={name:"D-Low 拉链音",
 howto:"一个两段式的拉链音，在第一段之上再叠一段扫频。这是 D-Low 的标志性转场。"};
S["water-drop"]={name:"水滴",
 howto:"做一个边咂舌音，除阻后立刻张开下巴让腔体音高上行——正是这个上行的音高让耳朵读成一滴水。",
 notes:"这是「靠物理而不是靠音色去模仿」的教科书案例：上行的共鸣模拟的是一个气泡塌缩的过程。"};
S["pash-laser"]={name:"Pash 激光音",
 howto:"把一个极紧的「sh」紧缩点向前扫，让噪声带爬升。实测频谱重心在 6 kHz 以上。"};
S["sega-sound"]={name:"Sega 音",
 howto:"一个明亮的带声嗡鸣配上快速的音高调制，模仿 16 位主机的 FM 音源。"};
S["inward-vocal-fry"]={name:"吸气嘎裂声",
 howto:"吸气的同时让声带以极低频率不规则地拍合。每一次声门脉冲都单独可听。",
 notes:"在嘎裂声区的最底端，耳朵不再听到音高，而是开始听到一个个声门脉冲——这就是音高感知的下限，大约 20–40 Hz。"};
S["helium-zipper"]={name:"Helium 拉链音",
 howto:"在尽可能小的前腔里做拉链音，使整段扫频高出一个八度。名字来自 Helium。"};
S["meow-squeak"]={name:"猫叫尖啸",
 howto:"一个被掐紧的假声音，带下行滑移和硬腭处的鼻音色彩。"};
S["frosty-sound"]={name:"Frosty 音",
 howto:"把猫叫尖啸重复得足够快，让它变成一段滚奏而不是一串单音。"};
S["kim-hutch-squeak"]={name:"Hutch 尖啸",
 howto:"一个极紧的假声带尖啸，配上硬腭滤色。名字来自 KIM 和 Hutch。"};
S["robot-voice"]={name:"机器人声",
 howto:"托住一个平直、没有颤音的嘎裂声，在它之上做出词语或节奏，让音源听起来是机械的。",
 notes:"让它听起来像机器人的，是音高抖动的缺席——人声正常情况下绝不会那么稳。"};
S["siren"]={name:"警笛",
 howto:"唱一段连续的大幅上下滑移，中间不要断开音。"};
S["siren-roll"]={name:"警笛滚奏",
 howto:"把一个小舌滚奏扫过很大的音高范围。用作转场，有时也叫 MixFx roll。"};
S["sonic-boom"]={name:"音爆",
 howto:"对着完全打开的喉咙做一个极硬的唇挤喉音，衰减过程中下巴不断下落，把共鸣向下扫。"};
S["dharni-water-drop"]={name:"Dharni 水滴",
 howto:"两个咂舌音，中间带一段上行的腔体扫频。这是 Dharni 版本的水滴音。"};
S["milky-sound"]={name:"乳白音",
 howto:"一个湿的带声唇咂舌音，密封处含唾液，得到一个厚重的液态爆破音。"};
S["vocal-scratch"]={name:"人声搓盘",
 howto:"托住一个带声的「zh」，通过交替呼气与吸气让音高来回猛拽——正是手在唱盘上的动作。",
 notes:"实测起振 7 毫秒——档案中最快的瞬态，这也是搓盘错觉能成立的原因。"};
S["throat-tapping-sound"]={name:"敲喉音",
 howto:"哼一个低音，同时用手指敲击喉部，从身体外部调制共鸣。",
 notes:"这是罕见的一例：完全没有气流机制——能量来自手，而不是肺。"};
S["clown-horn"]={name:"小丑喇叭",
 howto:"把面颊里的空气从收得极紧的圆唇挤出去，让它「叭」地响。完全不用肺部气流。"};
S["inward-chant"]={name:"吸气吟唱",
 howto:"一边吸气一边唱一个持续音。声带是被从上方驱动的，音色因此空洞、带风声。",
 notes:"吸气演唱是节奏口技让旋律线越过呼吸限制的方式。"};
S["inward-drag"]={name:"吸气拖拽",
 howto:"在长时间的铺垫中把气经一个紧缩的咽部往里拖，听起来像倒放的采样。"};
S["sucker-punch"]={name:"偷袭拳",
 howto:"一次锐利的向内吸气，紧接一个硬的软腭脆响，做出拳头破空加命中的效果。"};
S["626-effect"]={name:"626 效果音",
 howto:"一个掐紧的嘎裂尖啸，配合交替气流向上扫频，模仿史迪奇（实验体 626）。"};
})(window.BBX_I18N.zh);
