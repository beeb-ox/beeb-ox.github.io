# -*- coding: utf-8 -*-
TAX = {
"k-snare-out": dict(
  sbn="K", ipa="[k͡x]", place="velar", manner="affricate", airstream="PE",
  voice="voiceless", role="snare", inst="Acoustic snare / TR-909 snare", diff=1,
  lang="The velar affricate [k͡x] is a phoneme in Xhosa and in High Alemannic German.",
  howto="Build pressure behind a velar closure and release it into a hard 'kh' burst. Say 'k' as forcefully as possible with the throat tight.",
  notes="The default snare of the whole discipline and the one Proctor et al. (2013) transcribed as [kx:]. Broadband, 1.5 kHz centroid, near-instant attack."),
"duck-k-snare-out": dict(
  sbn="Kd", ipa="[k͡xʷ]", place="velar (rounded)", manner="affricate", airstream="PE",
  voice="voiceless", role="snare", inst="Gated snare", diff=2,
  lang="Labialised velars are phonemic in Ewe and Hausa.",
  howto="A K snare with the lips rounded and the cheeks puffed, which darkens the burst and shortens the tail."),
"inward-k-snare": dict(
  sbn="^K", ipa="[k͡x↓]", place="velar", manner="affricate", airstream="PI",
  voice="voiceless", role="snare", inst="Snare / rimshot", diff=2,
  lang="Ingressive fricatives are marginally attested in Tsou and Damin.",
  howto="Draw air sharply inward past a velar constriction. Same articulation as a K snare, opposite airflow.",
  notes="Half the reason beatboxers can hold a pattern indefinitely: the snare is played on the inhale, so the breath resets itself every bar."),
"rim-shot": dict(
  sbn="Kr", ipa="[k'̚]", place="velar", manner="unreleased ejective", airstream="GE",
  voice="voiceless", role="snare", inst="Rimshot", diff=2,
  lang="Velar ejectives [kʼ] are phonemic in Georgian, Quechua and Amharic.",
  howto="Compress air behind a velar closure with the glottis shut and clip the release, so you get a dry crack with no hiss."),
"pf-snare": dict(
  sbn="Pf", ipa="[p͡f']", place="bilabial → labiodental", manner="ejective affricate", airstream="GE",
  voice="voiceless", role="snare", inst="Snare / clap", diff=2,
  lang="[p͡f] is a phoneme in German (Pfund) and Tshivenda.",
  howto="Compress behind closed lips, then release into an 'f' so the burst has a spitty edge. Transcribed [>pf'] in the MRI literature.",
  notes="The most common alternative to the K snare, and the standard snare of the boots-and-cats pattern."),
"psch-snare": dict(
  sbn="Psh", ipa="[p͡ʃ']", place="bilabial → postalveolar", manner="ejective affricate", airstream="GE",
  voice="voiceless", role="snare", inst="Snare with room / clap", diff=2,
  lang="[p͡ʃ] is not a single phoneme in major languages but occurs as a cluster in Russian and Polish.",
  howto="Lip compression released into a 'sh', giving a longer, wetter snare with a visible tail."),
"rhino-snare": dict(
  sbn="Krh", ipa="[k͡xˤ]", place="velar + pharyngeal", manner="affricate (harsh)", airstream="PE",
  voice="voiceless, harsh", role="snare", inst="Distorted snare", diff=3,
  lang="Pharyngealised velars are described for Arabic dialects.",
  howto="A K snare with the pharynx clamped so the burst tears. Named for Beat Rhino."),
"tf-snare": dict(
  sbn="Tf", ipa="[t͡f']", place="alveolar → labiodental", manner="ejective affricate", airstream="GE",
  voice="voiceless", role="snare", inst="Tight snare / rim", diff=2,
  lang="Not attested as a single phoneme.",
  howto="Tongue-tip closure released through the lower lip and teeth. Sharper and thinner than a PF snare."),
"duff-snare": dict(
  sbn="Df", ipa="[d̥͡f]", place="alveolar → labiodental", manner="affricate", airstream="PE",
  voice="voiceless", role="snare", inst="Muffled snare", diff=2,
  lang="Not attested as a single phoneme.",
  howto="A softer, flatter TF with more lip and less tongue, for dull backbeats."),
"ps-snare": dict(
  sbn="Ps", ipa="[p͡s']", place="bilabial → alveolar", manner="ejective affricate", airstream="GE",
  voice="voiceless", role="snare", inst="Snare / clap", diff=2,
  lang="[ps] occurs as a cluster in Greek (ψ) and as a phoneme in some Bantu languages.",
  howto="Lip compression released into a tight 's'. Brighter than PF, good for snappy sixteenths."),
"push-snare": dict(
  sbn="Pu", ipa="[p͡ʃ'ʰ]", place="bilabial → postalveolar", manner="ejective affricate + aspiration", airstream="GE+PE",
  voice="voiceless", role="snare", inst="Big room snare", diff=3,
  lang="Aspirated affricates are phonemic in Mandarin and Korean.",
  howto="A PSCH snare with a deliberate lung-air push after the release, so it has a long noisy tail."),
"hollow-clop-snare": dict(
  sbn="Clh", ipa="[ǃˤ]", place="postalveolar + pharyngeal", manner="click", airstream="LI",
  voice="voiceless", role="snare", inst="Rimshot / woodblock", diff=2,
  lang="Postalveolar clicks are phonemic in Zulu and Xhosa.",
  howto="A large-cavity clop used on the backbeat. Tongue air only, so it can be placed over a sustained bass."),
"tongue-snare(808)": dict(
  sbn="T808", ipa="[ɭ̆']", place="alveolar", manner="ejective tongue slap", airstream="BE",
  voice="voiceless", role="snare", inst="TR-808 snare / rim", diff=3,
  lang="Not attested as a speech sound.",
  howto="Slap the flat of the tongue down off the palate with the cheeks pressurised. No lung air is used.",
  notes="Buccal, so it combines freely with any sustained lung-powered bass — the foundation of tongue-bass technique."),
"tongue-bass-snare": dict(
  sbn="Btsn", ipa="[ɭ̆ˤ']", place="alveolar", manner="tongue slap (large cavity)", airstream="BE",
  voice="voiceless", role="snare", inst="808 snare + sub", diff=4,
  lang="Not attested as a speech sound.",
  howto="A tongue snare made with a big back cavity so the slap carries its own low thump."),
"tus-snare": dict(
  sbn="Tus", ipa="[t͡ʊ̥s]", place="alveolar", manner="affricate with vowel colour", airstream="PE",
  voice="voiceless", role="snare", inst="Snare / clap", diff=2,
  lang="Not attested as a single phoneme.",
  howto="A 't' released through a rounded 'oo' shape into an 's', which adds body between the transient and the hiss."),
"top-lip-spit-snare": dict(
  sbn="Spt", ipa="[p͡s'↑]", place="bilabial (upper lip)", manner="ejective affricate (wet)", airstream="GE",
  voice="voiceless", role="snare", inst="Clap / rimshot", diff=3,
  lang="Not attested as a speech sound.",
  howto="Compress air behind the upper lip with saliva in the seal, so the release has a wet crack. The 'spit' family is defined by that liquid component."),
"kiss-spit-snare": dict(
  sbn="Ksp", ipa="[ʘ͡s]", place="bilabial", manner="click + fricative", airstream="LI+PE",
  voice="voiceless", role="snare", inst="Clap", diff=3,
  lang="Bilabial clicks are phonemic in Nǀuu.",
  howto="Start from a lip click and let it spill into an 's', so a kiss becomes a backbeat."),
"fish-snare": dict(
  sbn="Fsh", ipa="[ʘ̬͡ʃ]", place="bilabial → postalveolar", manner="click + fricative", airstream="LI+PE",
  voice="voiceless", role="snare", inst="Clap / snare", diff=3,
  lang="Not attested as a single phoneme.",
  howto="A wet lip release into 'sh' — named for the fish-mouth shape the lips make."),
"ghost-snare": dict(
  sbn="(k)", ipa="[k͡x̥]", place="velar", manner="affricate (very quiet)", airstream="PE",
  voice="voiceless", role="snare", inst="Ghost note snare", diff=2,
  lang="Not attested as a distinct phoneme.",
  howto="A K snare at minimum volume, placed between the main hits. Ghost notes are what make a pattern swing rather than march."),
"villardo-snare": dict(
  sbn="Kvl", ipa="[k͡x͡ʃ']", place="velar + postalveolar", manner="ejective affricate", airstream="GE+PE",
  voice="voiceless", role="snare", inst="Layered snare", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A K snare and a spit snare fired together so the transient and the tail come from different places. Named for Villardo."),
"sneeze-snare": dict(
  sbn="Sn", ipa="[ʃ͡tʰ]", place="postalveolar + alveolar", manner="fricative + aspirated stop", airstream="PE",
  voice="voiceless", role="snare", inst="Snare with reverb", diff=3,
  lang="Not attested as a single phoneme.",
  howto="Imitate the shape of a sneeze: a short intake, then an explosive 'shh-t' with the whole chest behind it."),
"esh-snare": dict(
  sbn="Esh", ipa="[ɛ̥ʃ']", place="postalveolar", manner="ejective fricative", airstream="GE",
  voice="voiceless", role="snare", inst="Snare / clap", diff=2,
  lang="Ejective fricatives [sʼ] are phonemic in Amharic and Tlingit.",
  howto="Compress air with the glottis closed and release it through a 'sh' shape — the mouth's version of a clap with room on it."),
"peh-snare": dict(
  sbn="Peh", ipa="[pʰɛ̥]", place="bilabial", manner="aspirated plosive", airstream="PE",
  voice="voiceless", role="snare", inst="Clap", diff=1,
  lang="Aspirated [pʰ] is phonemic in Mandarin, Thai, Hindi and Korean.",
  howto="A clean aspirated 'p' with a breathy release. Easy, quick, and common in technical patterns."),
"river-snare": dict(
  sbn="Riv", ipa="[p͡ʃ'r̥]", place="bilabial + postalveolar", manner="ejective affricate + flutter", airstream="GE",
  voice="voiceless", role="snare", inst="Snare with flanger", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A spit snare whose tail flutters because saliva is moving in the release — the flowing sound gives it the name."),
"blade-snare": dict(
  sbn="Bld", ipa="[t͡s'ʲ]", place="alveolar (blade)", manner="ejective affricate", airstream="GE",
  voice="voiceless", role="snare", inst="Tight snare / rim", diff=3,
  lang="Not attested as a single phoneme.",
  howto="Use the blade rather than the tip of the tongue so the release is thin and cutting."),
"vocalized-inward-k": dict(
  sbn="^K+V", ipa="[k͡x↓ + V̬]", place="velar + glottal", manner="affricate over voice", airstream="PI+PE",
  voice="voiced layer", role="snare", inst="Snare + bass", diff=4,
  lang="Not attested as a simultaneous combination.",
  howto="Play an inward K snare while phonating, so the snare arrives with a pitched body under it."),
"double-inward-snare": dict(
  sbn="^KK", ipa="[k͡x↓k͡x↓]", place="velar", manner="affricate (double)", airstream="PI",
  voice="voiceless", role="snare", inst="Double snare / flam", diff=3,
  lang="Not attested as a speech sound.",
  howto="Two inward K snares on a single intake — a flam that costs no breath."),
"two-h-snare": dict(
  sbn="Khh", ipa="[k͡xʰʰ]", place="velar + glottal", manner="affricate + double aspiration", airstream="PE",
  voice="voiceless", role="snare", inst="Snare + reverb tail", diff=3,
  lang="Not attested as a single phoneme.",
  howto="A K snare followed by two distinct breath pulses, which reads as a snare in a big room."),
"mad-clop-snare": dict(
  sbn="Clm", ipa="[ǃ͡ʃ']", place="postalveolar", manner="click + ejective fricative", airstream="LI+GE",
  voice="voiceless", role="snare", inst="Layered snare", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A clop and a spit snare fired together, so a tongue-air click gets a lung-air tail."),
"distorted-tf-snare": dict(
  sbn="Tf~", ipa="[t͡f'̃]", place="alveolar → labiodental", manner="ejective affricate (harsh)", airstream="GE",
  voice="voiceless, harsh", role="snare", inst="Distorted snare", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A TF snare with a constricted throat so the release breaks into noise."),
"vocalized-cough-snare": dict(
  sbn="Cgh+V", ipa="[ʔ͡ʕ̬]", place="glottal/pharyngeal", manner="glottal release + voice", airstream="PE",
  voice="voiced", role="snare", inst="Snare + tom", diff=3,
  lang="Glottal stops are phonemic in Arabic, Hawaiian and Danish.",
  howto="A voiced cough: build pressure under a closed glottis and release it while phonating."),
"cough-snare": dict(
  sbn="Cgh", ipa="[ʔ͡h]", place="glottal", manner="glottal release", airstream="PE",
  voice="voiceless", role="snare", inst="Snare / floor tom", diff=2,
  lang="Glottal stops are phonemic in many languages; a full cough is paralinguistic.",
  howto="A controlled cough used as a backbeat — short, chesty, and low in frequency for a snare."),
"rolled-spit-snare": dict(
  sbn="Sptr", ipa="[p͡s'r̥]", place="bilabial", manner="ejective affricate + roll", airstream="GE",
  voice="voiceless", role="snare", inst="Snare roll", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A spit snare whose release is rolled across the lips, giving several grains instead of one crack."),
"rimshot-hollow-clop": dict(
  sbn="Kr+Clh", ipa="[k'͡ǃˤ]", place="velar + postalveolar", manner="ejective + click", airstream="GE+LI",
  voice="voiceless", role="snare", inst="Rimshot", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A rimshot and a hollow clop at the same instant — two airstream mechanisms firing together for a thicker crack."),
"sneeze-spit-snare": dict(
  sbn="Snsp", ipa="[ʃ͡p͡s'ʰ]", place="postalveolar + bilabial", manner="fricative + ejective affricate", airstream="GE+PE",
  voice="voiceless", role="snare", inst="Big snare", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A sneeze snare with a wet lip release folded in, which is why it measures as one of the brightest snares in the set."),
"falsetto-spit-snare": dict(
  sbn="Spt↑", ipa="[p͡s' + V̬˦]", place="bilabial + glottal", manner="ejective affricate + falsetto", airstream="GE+PE",
  voice="voiced falsetto layer", role="snare", inst="Snare + synth stab", diff=4,
  lang="Not attested as a simultaneous combination.",
  howto="Fire a spit snare and let a falsetto note ring out of it, so the snare has a pitched ping."),
"esh-tongue-bass-snare": dict(
  sbn="Esh+Bts", ipa="[ʃ' + ɭ̆ˤ]", place="postalveolar + alveolar", manner="ejective fricative + tongue slap", airstream="GE+BE",
  voice="voiceless", role="snare", inst="Snare + sub", diff=5,
  lang="Not attested as a single phoneme.",
  howto="An esh snare stacked on a tongue bass slap so the backbeat carries its own low end."),
"double-k-snare-outward": dict(
  sbn="KK", ipa="[k͡xk͡x]", place="velar", manner="affricate (double)", airstream="PE",
  voice="voiceless", role="snare", inst="Double snare", diff=3,
  lang="Not attested as a speech sound.",
  howto="Two outward K snares from one breath push, close enough to read as a flam."),
"inward-tongue-bass-snare": dict(
  sbn="^Btsn", ipa="[ɭ̆ˤ↓]", place="alveolar", manner="tongue slap", airstream="BI",
  voice="voiceless", role="snare", inst="808 snare", diff=4,
  lang="Not attested as a speech sound.",
  howto="A tongue-bass snare made by rarefying rather than compressing the buccal pocket, which snaps the tongue upward."),
"click-snare": dict(
  sbn="ǃsn", ipa="[ǃ͡x]", place="postalveolar + velar", manner="click + fricative", airstream="LI+PE",
  voice="voiceless", role="snare", inst="Rim / clap", diff=3,
  lang="Clicks with velar friction are described for !Xóõ.",
  howto="A click whose back closure releases into friction, so you get both a crack and a hiss."),
"vocalized-fish-snare": dict(
  sbn="Fsh+V", ipa="[ʘ̬͡ʒ]", place="bilabial → postalveolar", manner="click + voiced fricative", airstream="LI+PE",
  voice="voiced", role="snare", inst="Snare + bass", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A fish snare with voicing running through the release, giving it a pitched body."),
"laid-back-inward-k-snare": dict(
  sbn="^K.", ipa="[k͡x↓ˑ]", place="velar", manner="affricate (delayed)", airstream="PI",
  voice="voiceless", role="snare", inst="Laid-back snare", diff=3,
  lang="Not attested as a distinct phoneme.",
  howto="An inward K placed deliberately late against the beat. The articulation is ordinary; the timing is the technique."),
"poly-spit-snare": dict(
  sbn="Sptp", ipa="[p͡s' + V̬ + ʃ]", place="bilabial + glottal + postalveolar", manner="ejective affricate + voice", airstream="GE+PE",
  voice="voiced + voiceless", role="snare", inst="Layered snare", diff=5,
  lang="Not attested as a simultaneous combination.",
  howto="A spit snare with a sung note and a noise layer at once — three sources in one gesture."),
"huckle-snare": dict(
  sbn="Hck", ipa="[ħ͡k']", place="pharyngeal + velar", manner="ejective with pharyngeal onset", airstream="GE",
  voice="voiceless", role="snare", inst="Snare / rim", diff=4,
  lang="Pharyngeal fricatives [ħ] are phonemic in Arabic and Hebrew.",
  howto="Begin with a pharyngeal squeeze and finish with a velar ejective crack."),
"distorted-spit-snare": dict(
  sbn="Spt~", ipa="[p͡s'̃]", place="bilabial", manner="ejective affricate (harsh)", airstream="GE",
  voice="voiceless, harsh", role="snare", inst="Distorted snare", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A spit snare with the throat clamped so the release shreds. Measured among the brightest, noisiest sounds in the archive."),
"mad-cough-snare": dict(
  sbn="Cghm", ipa="[ʔ͡ħ̃]", place="glottal + pharyngeal", manner="glottal release (harsh)", airstream="PE",
  voice="voiceless, harsh", role="snare", inst="Distorted snare", diff=4,
  lang="Not attested as a single phoneme.",
  howto="A cough snare pushed into distortion by holding the false folds tight during the release."),
"vocalized-club-snare": dict(
  sbn="Clb+V", ipa="[p͡ʃ' + V̬ˤ]", place="bilabial + glottal", manner="ejective affricate + voice", airstream="GE+PE",
  voice="voiced", role="snare", inst="Club / house snare", diff=4,
  lang="Not attested as a simultaneous combination.",
  howto="A wide, voiced snare with a long tail, shaped to sit in four-to-the-floor patterns."),
"vocalized-sneeze-spit-snare": dict(
  sbn="Snsp+V", ipa="[ʃ͡p͡s' + V̬]", place="postalveolar + bilabial + glottal", manner="compound + voice", airstream="GE+PE",
  voice="voiced", role="snare", inst="Layered big snare", diff=5,
  lang="Not attested as a single phoneme.",
  howto="The sneeze-spit snare with phonation added, the heaviest snare in the archive."),
"rolled-inward-k-snare": dict(
  sbn="^Kr", ipa="[k͡x↓r̥]", place="velar + uvular", manner="affricate + trill", airstream="PI",
  voice="voiceless", role="snare", inst="Snare roll", diff=4,
  lang="Not attested as a single phoneme.",
  howto="An inward K whose release rolls over the uvula, giving a buzzing snare tail on the inhale."),
"poh-snare": dict(
  sbn="Poh", ipa="[pʰɔ̥]", place="bilabial", manner="aspirated plosive (rounded)", airstream="PE",
  voice="voiceless", role="snare", inst="Clap / rim", diff=1,
  lang="Aspirated [pʰ] is phonemic in Mandarin, Thai and Hindi.",
  howto="Like the Peh snare but with rounded lips, which drops the burst frequency and softens it."),
}
