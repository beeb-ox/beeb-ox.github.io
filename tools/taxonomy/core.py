# -*- coding: utf-8 -*-
TAX = {
# ---------------- KICKS ----------------
"kick": dict(
  sbn="B", ipa="[p'] ~ [b̪]", place="bilabial", manner="ejective plosive", airstream="GE",
  voice="voiceless", role="kick", inst="Acoustic kick drum / TR-909 kick", diff=1,
  lang="The bilabial ejective [pʼ] is a phoneme in Hausa, Quechua, Amharic and Georgian.",
  howto="Close the lips, close the glottis, and raise the larynx to compress the air trapped between them. Release the lips sharply. Say the letter 'b' with no voice and no lung air — the pop comes from the squeezed pocket.",
  notes="Proctor et al. (2013) confirmed by real-time MRI that the classic beatbox kick is a glottalic egressive stop, not a pulmonic [b]. Measured here at 180 ms with all energy under 300 Hz."),
"electro-kick": dict(
  sbn="Bel", ipa="[p'→ʕ̞]", place="bilabial → pharyngeal", manner="ejective + pitched tail", airstream="GE+PE",
  voice="voiceless onset, voiced tail", role="kick", inst="TR-808 kick", diff=3,
  lang="Ejective release is phonemic; the tuned decay is not.",
  howto="Kick as normal, then let the throat ring on a falling pitch so the drum has an 808-style tail.",
  notes="Measured with a pitch glide of nearly 400 Hz across the decay — the same downward sweep an 808 kick makes."),
"throat-kick": dict(
  sbn="Bth", ipa="[ʡ']", place="epiglottal/pharyngeal", manner="ejective plosive", airstream="GE",
  voice="voiceless", role="kick", inst="Deep kick / taiko", diff=3,
  lang="Epiglottal stops are phonemic in Dahalo and Haida.",
  howto="Make the closure deep in the throat rather than at the lips, then release. Very short attack (measured at 14 ms) and almost no high frequency.",
  notes="Because the closure is behind the mouth, the lips stay free — you can articulate a kick without moving your mouth at all."),
"dry-kick": dict(
  sbn="Bd", ipa="[p'̚]", place="bilabial", manner="unreleased ejective", airstream="GE",
  voice="voiceless", role="kick", inst="Gated kick / cardboard box", diff=2,
  lang="Unreleased stops are phonemic word-finally in Korean, Thai and Cantonese.",
  howto="Kick but damp the release immediately, giving a tight thud with no boom. Used when a pattern needs the beat without the low end."),
"bdb-kick-roll": dict(
  sbn="BdB / BdBdB", ipa="[p'd̥p']", place="bilabial + alveolar", manner="ejective cluster", airstream="GE",
  voice="voiceless", role="kick", inst="Double / triple kick", diff=3,
  lang="Stop clusters are phonemic in Georgian and Polish; this particular cluster is not.",
  howto="Chain kick–tongue-tap–kick from a single glottal compression. Measured at about 6 hits per second.",
  notes="The tongue tap borrows the same pressurised pocket, so two or three kicks come from one breath gesture."),
"brb-kick-roll": dict(
  sbn="BrB", ipa="[p'ʙ̥p']", place="bilabial", manner="ejective + trill", airstream="GE+BE",
  voice="voiceless", role="kick", inst="Kick roll / flam", diff=4,
  lang="Not attested as a speech sound.",
  howto="Kick, let the lips flutter briefly, then kick again — a flam built out of a short lip roll."),

# ---------------- HI HATS AND CYMBALS ----------------
"hi-hat": dict(
  sbn="t", ipa="[t͡s]", place="alveolar", manner="affricate", airstream="PE",
  voice="voiceless", role="hat", inst="Closed hi-hat", diff=1,
  lang="[ts] is a phoneme in German, Japanese, Mandarin and Russian.",
  howto="Tongue tip to the alveolar ridge, release into a short 'ts'. Keep it clipped — the whole sound should last under 60 ms.",
  notes="The workhorse of every beatbox pattern. Measured centroid around 2.7 kHz, close to a real closed hi-hat."),
"open-hi-hat": dict(
  sbn="ts / tss", ipa="[t͡sː]", place="alveolar", manner="affricate (long)", airstream="PE",
  voice="voiceless", role="hat", inst="Open hi-hat", diff=1,
  lang="Long [tsː] is contrastive in Italian and Japanese gemination.",
  howto="Same as the closed hat but hold the 's' and let it ring. Measured decay of 750 ms and a centroid near 8.9 kHz — the brightest sound in the archive.",
  notes="Sits at 8–9 kHz, which is genuinely in real hi-hat territory: this is one of the few instrument imitations that is acoustically accurate rather than suggestive."),
"sliced-hihat": dict(
  sbn="tst", ipa="[t͡sːt]", place="alveolar", manner="affricate (chopped)", airstream="PE",
  voice="voiceless", role="hat", inst="Sliced / gated hi-hat", diff=3,
  lang="Not attested as a speech sound.",
  howto="Start an open hat and interrupt it with tongue taps so the noise is cut into slices — the vocal equivalent of gating a sample."),
"f-hi-hat": dict(
  sbn="f", ipa="[f]", place="labiodental", manner="fricative", airstream="PE",
  voice="voiceless", role="hat", inst="Soft hi-hat / brush", diff=1,
  lang="[f] is a phoneme in most of the world's languages.",
  howto="A plain 'f' against the upper teeth. Quieter and duller than a 'ts' hat, useful for ghost notes between the main hats."),
"fast-hi-hats": dict(
  sbn="tttt", ipa="[t͡s t͡s t͡s t͡s]", place="alveolar", manner="affricate (rapid)", airstream="PE+PI",
  voice="voiceless", role="hat", inst="Trap hi-hat roll", diff=3,
  lang="Not attested as a speech sound.",
  howto="Alternate outward and inward 'ts' so the roll never has to stop for breath. Measured sustaining over 15 seconds.",
  notes="Alternating airstream direction is the standard trick for hi-hat rolls longer than one breath."),
"egg-shaker": dict(
  sbn="tsh-tsh", ipa="[t͡ʃ↔]", place="postalveolar", manner="affricate (alternating)", airstream="PE+PI",
  voice="voiceless", role="hat", inst="Egg shaker / maraca", diff=2,
  lang="Not attested as a speech sound.",
  howto="Swing between an outward and an inward 'tch' at a steady rate, imitating a shaker's two-stroke motion."),
"duck-hi-hat": dict(
  sbn="tk̚", ipa="[t͡s͡ǂ]", place="alveolar + palatal", manner="affricate + click", airstream="PE+LI",
  voice="voiceless", role="hat", inst="Muted hi-hat", diff=3,
  lang="Palatal clicks are phonemic in Nǀuu and Xhosa.",
  howto="A hat with a click folded into it, which mutes and shortens the noise burst."),
"trap-high-hat": dict(
  sbn="tt-t", ipa="[t͡s t͡s t͡s]", place="alveolar", manner="affricate (triplet)", airstream="PE",
  voice="voiceless", role="hat", inst="Trap hi-hat (triplet rolls)", diff=3,
  lang="Not attested as a speech sound.",
  howto="Group hats in fast triplets and sixteenth-note bursts with uneven accents, the way trap hi-hat programming does."),
"crash-cymbal": dict(
  sbn="tshhh", ipa="[t͡ʃːʰ]", place="postalveolar", manner="affricate + aspiration", airstream="PE",
  voice="voiceless", role="cymbal", inst="Crash cymbal", diff=2,
  lang="[tʃ] is a phoneme in English, Spanish and Hindi.",
  howto="A hard 'tch' opening into a long breathy hiss, with the mouth widening through the decay to mimic a cymbal's spreading spectrum.",
  notes="A real crash rings for 2–4 seconds; the mouth version decays far faster, which is one of the clearest physical limits in the archive."),
"brushed-cymbal": dict(
  sbn="shh", ipa="[ʃː]", place="postalveolar", manner="fricative", airstream="PE",
  voice="voiceless", role="cymbal", inst="Brushed cymbal / ride wash", diff=1,
  lang="[ʃ] is a phoneme in English, French and Russian.",
  howto="A sustained 'sh' with gradual mouth opening, used as a wash under a pattern."),
"mhs-cymbal": dict(
  sbn="mhs", ipa="[m̥͡ʃ]", place="bilabial + postalveolar", manner="nasal + fricative", airstream="PE",
  voice="voiceless", role="cymbal", inst="Choked cymbal", diff=3,
  lang="Voiceless nasals are phonemic in Burmese and Icelandic.",
  howto="Release a voiceless nasal into a short 'sh' so the cymbal sounds choked. Known as the collapse cymbal in some scenes."),

# ---------------- CLICKS, CLOPS, POPS ----------------
"alien-click-roll": dict(
  sbn="ǂǂ", ipa="[ǂǂ]", place="palatal", manner="click (rolled)", airstream="LI",
  voice="voiceless", role="fx", inst="Woodblock / alien fx", diff=4,
  lang="Palatal clicks are phonemic in Nǀuu, ǂ'Amkoe and Xhosa.",
  howto="Seal the tongue broadly against the palate, rarefy the pocket and release repeatedly, varying the cavity size so the pitch wanders."),
"bart-click-roll": dict(
  sbn="ǃǃ↓", ipa="[ǃǃˤ]", place="postalveolar", manner="click (rolled, low)", airstream="LI",
  voice="voiceless", role="bass", inst="Low woodblock / clave", diff=4,
  lang="Postalveolar clicks are phonemic in Zulu and !Xóõ.",
  howto="Roll clicks with a very large back cavity so each release is pitched low. Named for the beatboxer Bart.",
  notes="Measured with almost all energy below 200 Hz — a click roll functioning as a bass line."),
"fast-click": dict(
  sbn="ǀǀ", ipa="[ǀǀ]", place="dental", manner="click (rapid)", airstream="LI",
  voice="voiceless", role="fx", inst="Clave / rimclick", diff=3,
  lang="Dental clicks are phonemic in Xhosa and Nǀuu, and occur paralinguistically in English as 'tsk'.",
  howto="Tongue tip behind the upper teeth, repeated dental clicks as fast as the tongue will reset."),
"super-fast-click": dict(
  sbn="ǀǀǀ", ipa="[ǀǀǀ]", place="dental", manner="click (very rapid)", airstream="LI",
  voice="voiceless", role="fx", inst="Clave roll", diff=5,
  lang="See dental click; the tempo is not linguistic.",
  howto="The same dental click pushed to the mechanical limit of the tongue tip, well past anything used in speech.",
  notes="Speech articulators top out around 8 syllables per second; click rolls exceed that because the tongue tip moves over a much smaller distance."),
"tennis-ball-pop": dict(
  sbn="P", ipa="[ʘ]", place="bilabial", manner="click", airstream="LI",
  voice="voiceless", role="fx", inst="Rim click / pop", diff=1,
  lang="The bilabial click [ʘ] is phonemic in Nǀuu and ǂ'Amkoe.",
  howto="Seal the lips, pull the tongue back to rarefy the mouth, and pop the lips open. A kiss with the volume up.",
  notes="A rare case where a beatbox sound is exactly a phoneme of a living language."),
"zekka-h-has-click-roll": dict(
  sbn="ǂǂh", ipa="[ǂǂʰ]", place="palatal", manner="click + aspiration", airstream="LI+PE",
  voice="voiceless", role="fx", inst="Woodblock + air", diff=4,
  lang="Aspirated clicks are phonemic in Zulu and Xhosa.",
  howto="Roll palatal clicks with a breath layer escaping around them. Named for Zekka."),
"dlow-click": dict(
  sbn="ǀd", ipa="[ǀ͡q]", place="dental + uvular", manner="click (double closure)", airstream="LI",
  voice="voiceless", role="snare", inst="Rimshot / woodblock", diff=4,
  lang="Uvular-released clicks are described for !Xóõ.",
  howto="Make the click with a uvular rather than velar back closure, which lowers and thickens the release. Named after D-Low."),
"clop": dict(
  sbn="Cl", ipa="[ǃ]", place="postalveolar", manner="click", airstream="LI",
  voice="voiceless", role="snare", inst="Woodblock / horse clop", diff=1,
  lang="The postalveolar click [ǃ] is a phoneme in Zulu, Xhosa and !Xóõ.",
  howto="Tongue tip sealed behind the ridge, tongue body pulled down hard, sharp release. The classic horse-hoof sound."),
"hollow-clop": dict(
  sbn="Clh", ipa="[ǃˤ]", place="postalveolar + pharyngeal", manner="click (large cavity)", airstream="LI",
  voice="voiceless", role="snare", inst="Deep woodblock / rimshot", diff=2,
  lang="See postalveolar click; the pharyngealised variant is described for Khoekhoe.",
  howto="Clop with the jaw dropped and the pharynx open so the release resonates lower and longer."),

# ---------------- INSTRUMENTS ----------------
"trumpet-trombone": dict(
  sbn="Tp", ipa="[ʙ̥ʷ]", place="bilabial", manner="lip buzz (embouchure)", airstream="PE",
  voice="voiceless", role="melody", inst="Trumpet / trombone", diff=3,
  lang="Not attested as a speech sound.",
  howto="Buzz the lips into a tight embouchure exactly as a brass player does, and use the tongue and jaw as the 'tubing' that sets pitch.",
  notes="Physically the same mechanism as a real brass instrument — a lip-reed oscillator — but with a resonator a few centimetres long instead of over a metre, so the low register is unreachable."),
"helium-trumpet": dict(
  sbn="Tp↑", ipa="[ʙ̥ʷ˦]", place="bilabial", manner="lip buzz (high)", airstream="PE",
  voice="voiceless", role="melody", inst="Piccolo trumpet", diff=4,
  lang="Not attested as a speech sound.",
  howto="Tighten the embouchure and shrink the oral cavity to push the buzz up an octave. Named for Helium."),
"electric-guitar": dict(
  sbn="Gtr", ipa="[ʙ̬ʲ͡z]", place="bilabial + palatal", manner="oscillation (distorted)", airstream="PE",
  voice="voiced", role="melody", inst="Electric guitar (distorted)", diff=4,
  lang="Not attested as a speech sound.",
  howto="A tight, bright lip buzz with a hard palatal constriction and heavy laryngeal distortion, bent with the jaw for vibrato."),
"saxophone": dict(
  sbn="Sx", ipa="[ʙ̬ˤ͡ʒ]", place="bilabial + pharyngeal", manner="reed-like oscillation", airstream="PE",
  voice="voiced", role="melody", inst="Saxophone", diff=4,
  lang="Not attested as a speech sound.",
  howto="Buzz with a looser, wetter embouchure than a trumpet and keep the throat wide, so the tone has a reedy rasp."),
"chinese-Instrument": dict(
  sbn="Gz", ipa="[ǃ͡ʒ↗]", place="alveolar", manner="pluck-like click + glide", airstream="LI+PE",
  voice="mixed", role="melody", inst="Guzheng / pipa", diff=5,
  lang="Not attested as a speech sound.",
  howto="Attack with a sharp click for the pluck, then bend a voiced tone upward to imitate the guzheng's characteristic slide."),
"violin": dict(
  sbn="Vln", ipa="[z̬ˠ˜]", place="alveolar", manner="voiced fricative + vibrato", airstream="PE",
  voice="voiced", role="melody", inst="Violin", diff=5,
  lang="Not attested as a speech sound.",
  howto="Hold a tight voiced buzz and add regular pitch vibrato from the larynx, with slow attacks so each note sounds bowed rather than struck."),
"pızzıcato-strıngs": dict(
  sbn="Pzz", ipa="[ɗ]", place="alveolar", manner="implosive", airstream="GI",
  voice="voiced", role="melody", inst="Pizzicato strings / upright bass", diff=3,
  lang="The voiced alveolar implosive [ɗ] is a phoneme in Sindhi, Hausa and Vietnamese.",
  howto="Lower the larynx while the tongue seals the ridge, so air is drawn inward and the release has a plucked snap that falls in pitch.",
  notes="An implosive: rarefaction rather than compression. The downward pitch bend is exactly what a plucked string does as its tension settles."),
}
