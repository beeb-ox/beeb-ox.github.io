# -*- coding: utf-8 -*-
TAX = {
# ---------------- LIPROLLS ----------------
"electro-liproll": dict(
  sbn="BBel", ipa="[ʙ̬͡z]", place="bilabial + alveolar", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Electro bass line", diff=3,
  lang="Bilabial trills are phonemic in Nias and Kele.",
  howto="Roll the lips with a bright alveolar buzz layered on, then articulate a rhythm by interrupting the roll rather than restarting it.",
  notes="A liproll is a bass line and a drum pattern at once: the roll is continuous and the pattern is cut into it."),
"punchy-liproll": dict(
  sbn="BBp", ipa="[ʙ̬ˈ]", place="bilabial", manner="oscillation (accented)", airstream="PE",
  voice="voiced", role="bass", inst="Punchy bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="Roll with hard periodic accents from the diaphragm so each beat lands as a separate hit."),
"growling-liproll": dict(
  sbn="BBgr", ipa="[ʙ̬͡ʀ]", place="bilabial + uvular", manner="double oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Growl bass", diff=4,
  lang="Uvular trills are phonemic in French and German.",
  howto="Add a uvular growl to the lip roll so two oscillators beat against each other."),
"808-sub-liproll": dict(
  sbn="BB808", ipa="[ʙ̬ˤ˩]", place="bilabial + pharyngeal", manner="oscillation (sub)", airstream="PE",
  voice="voiced", role="bass", inst="808 sub bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="A liproll tuned as low as the lips will oscillate, with the larynx dropped and the pharynx wide open."),
"just-sub-liproll": dict(
  sbn="BBs", ipa="[ʙ̬˩]", place="bilabial", manner="oscillation (sub, clean)", airstream="PE",
  voice="voiced", role="bass", inst="Clean sub bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="The low roll with no distortion or growl — just weight. Used under melodic sections."),
"thin-teeth-liproll": dict(
  sbn="BBt", ipa="[ʙ̬̪̈]", place="labiodental", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Mid bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="Roll the lower lip against the upper teeth instead of lip-to-lip, which thins the tone and speeds up the flap rate."),
"8-bit-liproll": dict(
  sbn="BB8", ipa="[ʙ̬ʲ˜]", place="bilabial + palatal", manner="oscillation (square-ish)", airstream="PE",
  voice="voiced", role="bass", inst="Chiptune bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Roll with a hard palatal constriction so the waveform squares off and sounds like a games console."),
"yoi-sub-liproll": dict(
  sbn="BByo", ipa="[ʙ̬ʷ˩]", place="bilabial (rounded)", manner="oscillation (sub)", airstream="PE",
  voice="voiced", role="bass", inst="Sub bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="A rounded sub roll with a rising 'yoi' vowel colour through the phrase."),
"hi-vocalized-liproll": dict(
  sbn="BB↑V", ipa="[ʙ̬ + V̬˦]", place="bilabial + glottal", manner="oscillation + sung note", airstream="PE",
  voice="voiced", role="bass+melody", inst="Bass + lead", diff=4,
  lang="Not attested as a simultaneous combination.",
  howto="Roll the lips while singing a high note, so the bass and the melody come out together."),
"x2-liproll": dict(
  sbn="BBx2", ipa="[ʙ̬:ʙ̬:]", place="bilabial", manner="oscillation (double-rate)", airstream="PE",
  voice="voiced", role="bass", inst="Double-time bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Push the roll to twice the usual flap rate and articulate double-time patterns on top."),
"blaze-it-up-liproll": dict(
  sbn="BBbz", ipa="[ʙ̬ˤ͡z]", place="bilabial + alveolar", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Dubstep bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="A long, heavy roll with sweeping vowel changes across the bar — the signature of the 'blaze it up' routine."),
"teeth-liproll": dict(
  sbn="BBte", ipa="[ʙ̬̪]", place="labiodental", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Mid bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="Roll with the lower lip riding the upper teeth. Measured among the fastest rolls in the archive at about 10 flaps per second."),
"grimy-teeth-liproll": dict(
  sbn="BBtg", ipa="[ʙ̬̪̃]", place="labiodental", manner="oscillation (distorted)", airstream="PE",
  voice="voiced, harsh", role="bass", inst="Grimy bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Teeth roll with laryngeal distortion, giving the dirty tone used in grime and dubstep routines."),
"hollow-liproll": dict(
  sbn="BBho", ipa="[ʙ̬ˤ]", place="bilabial + pharyngeal", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Dub bass", diff=3,
  lang="Pharyngealisation is phonemic in Arabic.",
  howto="Roll with maximum pharyngeal space so the tone is round and woody rather than buzzy."),
"low-hollow-liproll": dict(
  sbn="BBho↓", ipa="[ʙ̬ˤ˩]", place="bilabial + pharyngeal", manner="oscillation (sub)", airstream="PE",
  voice="voiced", role="bass", inst="Dub sub bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="The hollow roll with the larynx dropped further, taking it into sub territory."),
"tongue-hollow-liproll": dict(
  sbn="BBthq", ipa="[ɭ̆ˤ + ʙ̬]", place="alveolar + bilabial", manner="tongue + lip oscillation", airstream="BE+PE",
  voice="voiced", role="bass", inst="Sub bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="Hold a buccal tongue roll and a lip roll at once, so one is powered by cheek air and the other by the lungs."),
"tongue-punchy-liproll": dict(
  sbn="BBtp", ipa="[ɭ̆ˈ + ʙ̬]", place="alveolar + bilabial", manner="tongue + lip oscillation", airstream="BE+PE",
  voice="voiced", role="bass", inst="Punchy bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="The tongue roll accented hard on the beat while the lips keep the drone going."),
"tongue-808-sub-liproll": dict(
  sbn="BBt808", ipa="[ɭ̆ˤ˩ + ʙ̬]", place="alveolar + bilabial", manner="tongue + lip oscillation", airstream="BE+PE",
  voice="voiced", role="bass", inst="808 sub bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="A tongue-driven sub roll with an 808-style tuned decay on each accent."),
"tongue-just-sub-liproll": dict(
  sbn="BBts", ipa="[ɭ̆˩]", place="alveolar", manner="tongue oscillation (sub)", airstream="BE",
  voice="voiceless", role="bass", inst="Clean sub bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="A pure buccal sub roll with no lip component. Because the lungs are free, you can breathe through it."),
"double-liproll": dict(
  sbn="BB2", ipa="[ʙ̬ + ʙ̬]", place="bilabial", manner="two-rate oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Layered bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="Get the upper and lower lip flapping at different rates at the same time, producing two bass pitches."),

# ---------------- OTHER SOUNDS ----------------
"abx-roll": dict(
  sbn="ABX", ipa="[ʙ̬ˤ͡ʀ:]", place="bilabial + uvular", manner="compound oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Layered growl bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="A signature compound roll combining lip, uvular and laryngeal vibration. Named after the beatboxer ABX.",
  notes="Measured with almost all energy below 200 Hz despite three simultaneous oscillators."),
"abx-polyphonic": dict(
  sbn="ABXp", ipa="[ʙ̬ˤ + V̬ + ʍ]", place="bilabial + glottal + labial", manner="three-source polyphony", airstream="PE+AE",
  voice="voiced + voiceless", role="bass+melody", inst="Bass + pad + lead", diff=5,
  lang="No spoken language uses simultaneous independent sources this way.",
  howto="Hold the ABX roll, phonate a note, and whistle a third line over both.",
  notes="Three independent sound sources at once — close to the practical ceiling of human polyphony."),
"bird-squeak": dict(
  sbn="Sq", ipa="[ʔ͡i̯˥]", place="glottal", manner="squeak (false-fold)", airstream="PE",
  voice="voiced (very high)", role="fx", inst="Bird call / synth blip", diff=3,
  lang="Not attested as a speech sound.",
  howto="Pinch the glottis almost shut and let a tiny high squeak escape. Named for Beatfox and TrungBao.",
  notes="Measured near 4.8 kHz — the highest pitched sound in the archive."),
"vocal-roll(ctb)": dict(
  sbn="CTB", ipa="[r̝̊:]", place="alveolar", manner="voiced trill (rapid)", airstream="PE",
  voice="voiced", role="fx", inst="Synth arpeggio", diff=4,
  lang="Alveolar trills are phonemic in Spanish, Italian and Russian.",
  howto="An extremely fast trilled roll used as a texture rather than a consonant. CTB stands for the Chinese Tongue Bass community style."),
"double-sound": dict(
  sbn="V+V", ipa="[V̬ + V̬']", place="glottal", manner="two-pitch phonation", airstream="PE",
  voice="voiced", role="melody", inst="Two-part harmony", diff=5,
  lang="No language contrasts two simultaneous pitches from one larynx.",
  howto="Set the true folds and false folds vibrating at different rates so two pitches sound together.",
  notes="Genuine laryngeal polyphony — not an illusion. Both pitches are measurable in the spectrum."),
"inward-double-voice": dict(
  sbn="^V+V", ipa="[V̬↓ + V̬↓]", place="glottal", manner="two-pitch phonation", airstream="PI",
  voice="voiced", role="melody", inst="Two-part harmony", diff=5,
  lang="Not attested as a speech sound.",
  howto="The same two-pitch phonation produced while inhaling, so a harmony can be held across a breath."),
"baby-voice": dict(
  sbn="Bby", ipa="[V̬˥ʲ]", place="glottal + palatal", manner="phonation (raised larynx)", airstream="PE",
  voice="voiced", role="fx", inst="Pitched-up vocal sample", diff=2,
  lang="Falsetto and raised-larynx voice occur paralinguistically in every language.",
  howto="Raise the larynx and shrink the whole vocal tract so the formants move up with the pitch — the acoustic signature of a small body."),
"duck-sound": dict(
  sbn="Dk", ipa="[ʕ̞ʷ͡ʀ]", place="pharyngeal + uvular", manner="oscillation (buzzy)", airstream="PE",
  voice="voiced", role="fx", inst="Duck call / reed", diff=3,
  lang="Not attested as a speech sound.",
  howto="Squeeze the pharynx and let the uvula buzz with rounded lips, producing a nasal quack."),
"duck-roll": dict(
  sbn="Dkr", ipa="[ʕ̞ʷ͡ʀ:]", place="pharyngeal + uvular", manner="oscillation (rolled)", airstream="PE",
  voice="voiced", role="fx", inst="Duck call roll", diff=4,
  lang="Not attested as a speech sound.",
  howto="The duck sound sustained and rhythmically articulated as a roll."),
"polyphonic": dict(
  sbn="Poly", ipa="[V̬ + ʍ]", place="glottal + labial", manner="voice + whistle", airstream="PE+AE",
  voice="voiced + voiceless", role="melody", inst="Two-part harmony", diff=4,
  lang="No spoken language uses simultaneous independent pitches.",
  howto="Hum and whistle different notes at once. The two sources are mechanically independent, so real intervals are possible.",
  notes="The cleanest demonstration of two-voice polyphony from one performer — and the reason 'the voice is monophonic' is not quite true."),
"o-synth": dict(
  sbn="Osy", ipa="[ɔ̬ˠ˜]", place="glottal + velar", manner="phonation (formant-swept)", airstream="PE",
  voice="voiced", role="melody", inst="Analogue synth pad", diff=3,
  lang="Vowel formant movement is the basis of every spoken language.",
  howto="Hold an 'o' vowel and sweep the tongue and jaw so the formants move like a filter opening on a synthesiser.",
  notes="A vocal-tract filter sweep is physically the same operation as a synth low-pass sweep — the mouth is a resonant filter bank."),
"bubble-roll-dlow": dict(
  sbn="Bbl", ipa="[ʙ̬ʷ~]", place="bilabial (saliva)", manner="oscillation (wet)", airstream="PE",
  voice="voiced", role="fx", inst="Bubbles / water fx", diff=3,
  lang="Not attested as a speech sound.",
  howto="Roll with saliva pooled at the lips so the vibration breaks into discrete bubbles. Popularised by D-Low."),
"zipper": dict(
  sbn="Zp", ipa="[r̥↗]", place="alveolar", manner="trill (glide)", airstream="PE",
  voice="voiceless", role="fx", inst="Zipper / riser", diff=3,
  lang="Alveolar trills are phonemic in Spanish and Italian; the glide is not.",
  howto="Trill the tongue tip and sweep the resonance upward so the buzz rises like a zip being pulled."),
"dlow-zipper": dict(
  sbn="Zpd", ipa="[r̥↗↗]", place="alveolar + uvular", manner="trill (double glide)", airstream="PE",
  voice="voiceless", role="fx", inst="Riser / FX sweep", diff=4,
  lang="Not attested as a speech sound.",
  howto="A two-stage zipper with a second sweep layered on the first. D-Low's signature transition."),
"water-drop": dict(
  sbn="Wd", ipa="[ǁ↗]", place="lateral", manner="click + resonance glide", airstream="LI",
  voice="voiceless", role="fx", inst="Water drop / rim click", diff=2,
  lang="Lateral clicks [ǁ] are phonemic in Xhosa and Zulu.",
  howto="Make a lateral click and open the jaw immediately after the release so the cavity pitch rises — that rising pitch is what the ear reads as a droplet.",
  notes="A textbook case of imitation by physics rather than by timbre: the rising resonance mimics a bubble collapsing."),
"pash-laser": dict(
  sbn="Psl", ipa="[ʃ↗˥]", place="postalveolar", manner="fricative (swept)", airstream="PE",
  voice="voiceless", role="fx", inst="Laser / synth zap", diff=3,
  lang="Not attested as a speech sound.",
  howto="Sweep a very tight 'sh' constriction forward so the noise band climbs. Measured with a centroid above 6 kHz."),
"sega-sound": dict(
  sbn="Sg", ipa="[z̬ʲ˜↗]", place="alveolar + palatal", manner="voiced fricative (modulated)", airstream="PE",
  voice="voiced", role="fx", inst="Chiptune / FM synth", diff=4,
  lang="Not attested as a speech sound.",
  howto="A bright voiced buzz with fast pitch modulation, imitating a 16-bit console's FM chip."),
"inward-vocal-fry": dict(
  sbn="^Fry", ipa="[V̰↓]", place="glottal", manner="creaky phonation", airstream="PI",
  voice="creaky voiced", role="fx", inst="Growl / distortion", diff=3,
  lang="Creaky voice is phonemic in Jalapa Mazatec and in Danish stød; ingressive creak is not.",
  howto="Inhale while letting the vocal folds slap irregularly at very low frequency. Each pulse is individually audible.",
  notes="At the bottom of the fry register the ear stops hearing pitch and starts hearing individual glottal pulses — the lower limit of pitch perception, around 20–40 Hz."),
"helium-zipper": dict(
  sbn="Zp↑", ipa="[r̥↗˦]", place="alveolar", manner="trill (glide, high)", airstream="PE",
  voice="voiceless", role="fx", inst="High riser", diff=4,
  lang="Not attested as a speech sound.",
  howto="A zipper made in the smallest possible front cavity, so the sweep sits an octave higher. Named for Helium."),
"meow-squeak": dict(
  sbn="Mw", ipa="[ɲ̬˥↘]", place="palatal", manner="phonation (falsetto glide)", airstream="PE",
  voice="voiced", role="fx", inst="Cat / synth blip", diff=3,
  lang="Not attested as a speech sound.",
  howto="A pinched falsetto note with a falling glide and a nasal palatal colour."),
"frosty-sound": dict(
  sbn="Mwr", ipa="[ɲ̬˥↘:]", place="palatal", manner="phonation (rolled falsetto)", airstream="PE",
  voice="voiced", role="fx", inst="Synth arpeggio", diff=4,
  lang="Not attested as a speech sound.",
  howto="Repeat the meow squeak fast enough that it becomes a roll rather than a series of notes."),
"kim-hutch-squeak": dict(
  sbn="Sqk", ipa="[ʔ͡ʲ˥]", place="glottal + palatal", manner="squeak (false-fold)", airstream="PE",
  voice="voiced", role="fx", inst="Synth stab / squeal", diff=4,
  lang="Not attested as a speech sound.",
  howto="A very tight false-fold squeak with a palatal filter. Named for KIM and Hutch."),
"robot-voice": dict(
  sbn="Rbt", ipa="[V̰ˠ˜]", place="glottal + velar", manner="creaky phonation (modulated)", airstream="PE",
  voice="creaky voiced", role="fx", inst="Vocoder / ring modulator", diff=3,
  lang="Creaky voice is phonemic in Danish and Mazatec.",
  howto="Hold a flat creaky tone with no vibrato and articulate words or rhythms over it, so the pitch source sounds mechanical.",
  notes="What makes it read as robotic is the absence of natural pitch jitter — the human voice is normally never that steady."),
"siren": dict(
  sbn="Sir", ipa="[V̬↗↘]", place="glottal", manner="phonation (wide glide)", airstream="PE",
  voice="voiced", role="fx", inst="Siren / theremin", diff=2,
  lang="Pitch glides are phonemic as contour tones in Mandarin and Cantonese.",
  howto="Sing a continuous wide glide up and down without breaking the tone."),
"siren-roll": dict(
  sbn="Sirr", ipa="[ʀ̬↗↘]", place="uvular", manner="trill (glide)", airstream="PE",
  voice="voiced", role="fx", inst="Siren / FX roll", diff=4,
  lang="Uvular trills are phonemic in French and German.",
  howto="A uvular roll swept across a wide pitch range. Used as a transition — sometimes called the MixFx roll."),
"sonic-boom": dict(
  sbn="Bm", ipa="[p'ˤ↘:]", place="bilabial + pharyngeal", manner="ejective + falling resonance", airstream="GE",
  voice="voiceless", role="fx", inst="Impact / 808 boom", diff=3,
  lang="Bilabial ejectives are phonemic in Hausa and Quechua.",
  howto="A very hard lip ejective into a maximally open throat, with the jaw dropping through the decay to sweep the resonance downward."),
"dharni-water-drop": dict(
  sbn="Wdd", ipa="[ǁ͡ʘ↗]", place="lateral + bilabial", manner="double click + glide", airstream="LI",
  voice="voiceless", role="fx", inst="Water drop", diff=4,
  lang="Both click types are phonemic in Xhosa; the combination is not.",
  howto="Two clicks with a rising cavity sweep between them. Dharni's variant of the water drop."),
"milky-sound": dict(
  sbn="Mlk", ipa="[ʘ̬ʷ~]", place="bilabial", manner="click (wet, voiced)", airstream="LI+PE",
  voice="voiced", role="fx", inst="Liquid / bubble fx", diff=4,
  lang="Voiced clicks are phonemic in Zulu and Xhosa.",
  howto="A wet voiced lip click with saliva in the seal, giving a thick liquid pop."),
"vocal-scratch": dict(
  sbn="Scr", ipa="[ʒ̬↗↘:]", place="postalveolar", manner="voiced fricative (scrubbed)", airstream="PE+PI",
  voice="voiced", role="fx", inst="Turntable scratch", diff=4,
  lang="Not attested as a speech sound.",
  howto="Hold a voiced 'zh' and jerk the pitch back and forth by alternating outward and inward airflow, exactly as a hand moves a record.",
  notes="Measured attack of 7 ms — the fastest transient in the archive, which is what makes the scratch illusion convincing."),
"throat-tapping-sound": dict(
  sbn="Tap", ipa="[ʕ̞ + percussion]", place="laryngeal (external)", manner="percussive (struck)", airstream="none (external)",
  voice="voiced", role="fx", inst="Tom / talking drum", diff=2,
  lang="Not attested as a speech sound in any language.",
  howto="Hum a low tone and tap the throat with the fingers so the resonance is modulated from outside the body.",
  notes="The rare case of a sound with no airstream mechanism at all — the energy comes from the hand, not the lungs."),
"clown-horn": dict(
  sbn="Hrn", ipa="[ʙ̥ʷ˥]", place="bilabial", manner="lip buzz (squeezed)", airstream="BE",
  voice="voiceless", role="fx", inst="Bulb horn / kazoo", diff=2,
  lang="Not attested as a speech sound.",
  howto="Squeeze air from the cheeks through very tight rounded lips so it honks. No lung air involved."),
"inward-chant": dict(
  sbn="^Cht", ipa="[V̬↓]", place="glottal", manner="phonation (ingressive)", airstream="PI",
  voice="voiced", role="melody", inst="Choir / pad (inhaled)", diff=3,
  lang="Ingressive phonation appears paralinguistically in Swedish, Finnish and Ewe, but is phonemic nowhere.",
  howto="Sing a sustained note while breathing in. The vocal folds are driven from above, which gives a hollow, wind-like tone.",
  notes="Inhaled singing is how beatboxers keep melodic lines going past the breath limit."),
"inward-drag": dict(
  sbn="^Drg", ipa="[ʜ↓:]", place="pharyngeal", manner="fricative (ingressive)", airstream="PI",
  voice="voiceless", role="fx", inst="Reverse cymbal / riser", diff=3,
  lang="Voiceless epiglottal fricatives [ʜ] are phonemic in Agul.",
  howto="Drag air inward through a tight pharynx over a long build, which sounds like a reversed sample."),
"sucker-punch": dict(
  sbn="Spn", ipa="[ʘ̃↓͡k'ʰ]", place="bilabial + velar", manner="ingressive click + ejective", airstream="LI+GE",
  voice="voiceless", role="fx", inst="Impact / punch", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A sharp inward suck followed immediately by a hard velar crack, giving the whoosh-and-impact of a punch."),
"626-effect": dict(
  sbn="626", ipa="[ʔ͡ɨ̰˥↗]", place="glottal + palatal", manner="creaky squeak (glide)", airstream="PE+PI",
  voice="creaky voiced", role="fx", inst="Cartoon / alien voice", diff=5,
  lang="Not attested as a speech sound.",
  howto="A pinched creaky squeak swept upward with alternating airflow, imitating Stitch (experiment 626)."),
}
