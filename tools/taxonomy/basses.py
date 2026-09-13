# -*- coding: utf-8 -*-
TAX = {
"throat-bass": dict(
  sbn="Brrr", ipa="[ʙ̪̬ˤ]/[ʕ̞]", place="pharyngeal/laryngeal", manner="oscillation (aryepiglottic)", airstream="PE",
  voice="voiced (subharmonic)", role="bass", inst="Sub bass / Moog", diff=4,
  lang="Aryepiglottic trilling is phonemic in Agul and Iraqi Arabic; sustained subharmonic phonation is not.",
  howto="Relax the vocal folds and let the false folds above them vibrate at a fraction of the true-fold rate. Push a steady, low-pressure stream of air and let the throat rattle rather than sing.",
  notes="Produces subharmonics — vibration at 1/2 or 1/3 of the modal frequency — which is how a voice reaches under 100 Hz without singing that low."),
"vocal-lip-oscillation": dict(
  sbn="BB+V", ipa="[ʙ̬]", place="bilabial", manner="trill (oscillation)", airstream="PE",
  voice="voiced", role="bass", inst="Distorted sub / reese bass", diff=3,
  lang="Bilabial trills are phonemic in Nias and Kele; combining one with a sung pitch is not.",
  howto="Buzz the lips like a horse's snort while phonating underneath. The lips vibrate at a low rate and the voice supplies a second, higher pitch.",
  notes="Two oscillators at once: the lips and the vocal folds. The audible 'growl' is the beat pattern between them."),
"inward-bass": dict(
  sbn="^BB", ipa="[ʙ̬↓]", place="bilabial", manner="trill (oscillation)", airstream="PI",
  voice="voiced", role="bass", inst="Sub bass", diff=4,
  lang="Ingressive phonation is not phonemic in any language; it appears only paralinguistically (ingressive 'yes' in Scandinavian and Ewe).",
  howto="Draw air inward through loosely closed lips while phonating on the intake. Unnatural at first because the vocal folds are being blown open from above.",
  notes="Measured at around 60 Hz — near the lower limit of what the archive contains. Inhaled production means the bass can be held under a continuous pattern."),
"click-roll": dict(
  sbn="CC", ipa="[ǃǃ]", place="alveolar/postalveolar", manner="click (rolled)", airstream="LI",
  voice="voiceless", role="fx", inst="Woodblock roll / clave", diff=3,
  lang="Clicks are full consonants in Khoisan languages and in Zulu, Xhosa and Sandawe.",
  howto="Seal the tongue tip and back against the palate, pull the tongue body down to rarefy the pocket, and release repeatedly as fast as possible."),
"click-roll-sub-bass": dict(
  sbn="CC+B", ipa="[ǃǃ + ʕ̞]", place="alveolar + pharyngeal", manner="click over bass", airstream="LI+PE",
  voice="voiced bass under voiceless clicks", role="bass", inst="Clave over sub bass", diff=5,
  lang="Zulu and Xhosa combine clicks with voicing, but not with a sustained independent bass line.",
  howto="Hold a throat bass and roll clicks on top. Because clicks use tongue air and the bass uses lung air, the two do not interfere.",
  notes="The canonical proof that the mouth can run two airstream mechanisms simultaneously — the basis of most modern 'bass and clicks' routines."),
"high-octave-vibration-bass": dict(
  sbn="BB↑", ipa="[ʙ̬˦]", place="bilabial", manner="trill (oscillation)", airstream="PE",
  voice="voiced", role="bass", inst="Mid bass / synth lead", diff=3,
  lang="See bilabial trill; the octave-doubled form is not attested.",
  howto="Tighten the lips and raise subglottal pressure so the lip oscillation locks to twice its usual rate."),
"liproll-bass-top-lip": dict(
  sbn="BB(t)", ipa="[ʙ̬↑]", place="bilabial (upper lip)", manner="trill (oscillation)", airstream="PE",
  voice="voiced", role="bass", inst="Sub bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="Let only the upper lip flap against the lower one, with the jaw fairly still. Cleaner and more controllable than a full two-lip roll."),
"liproll-bass-bottom-lip": dict(
  sbn="BB(b)", ipa="[ʙ̬↓]", place="bilabial (lower lip)", manner="trill (oscillation)", airstream="PE",
  voice="voiced", role="bass", inst="Sub bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="Tuck the upper lip and flap the lower one. Slightly darker than the top-lip version because the lower lip has more mass."),
"liproll-sub-bass": dict(
  sbn="BB↓", ipa="[ʙ̬ˤ]", place="bilabial + pharyngeal", manner="trill + subharmonic", airstream="PE",
  voice="voiced", role="bass", inst="808 sub", diff=4,
  lang="Not attested as a speech sound.",
  howto="Roll the lips over a throat-bass foundation with the larynx dropped as far as it will go."),
"lazer-bass": dict(
  sbn="BB↗", ipa="[ʙ̬↗]", place="bilabial", manner="trill (glide)", airstream="PE",
  voice="voiced", role="bass", inst="Synth bass sweep", diff=4,
  lang="Not attested as a speech sound.",
  howto="Start a lip oscillation and sweep the jaw and tongue so the resonance climbs while the buzz rate stays put."),
"chest-bass": dict(
  sbn="Bch", ipa="[ʕ̞ˠ]", place="laryngeal", manner="subharmonic phonation", airstream="PE",
  voice="voiced (creaky)", role="bass", inst="Contrabass / sub sine", diff=4,
  lang="Creaky voice is phonemic in Jalapa Mazatec and Danish (stød); subharmonic chest register is not.",
  howto="Sing at the bottom of your range, then relax further until the tone drops an octave into a rattly register. Keep the airflow low and the chest resonant.",
  notes="Measured near 54 Hz — below the lowest note of a double bass (41 Hz) is out of reach, but this comes within a fourth of it."),
"inward-chest-bass": dict(
  sbn="^Bch", ipa="[ʕ̞↓]", place="laryngeal", manner="subharmonic phonation", airstream="PI",
  voice="voiced", role="bass", inst="Sub bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="Produce the same creaky low register while inhaling. Hard on the throat and best used briefly."),
"chest-bass-falsetto": dict(
  sbn="Bch↑", ipa="[ʕ̞ + V̥ˡ]", place="laryngeal", manner="two-register phonation", airstream="PE",
  voice="voiced", role="bass+melody", inst="Bass + flute", diff=5,
  lang="No language contrasts simultaneous modal and falsetto registers.",
  howto="Hold the low chest rattle while a falsetto tone rides above it — the false folds and the true folds vibrate at different rates.",
  notes="Measured with a strong harmonic at around 535 Hz over a low rattle: one larynx, two audible pitches."),
"vocal-chest-bass-trumpet": dict(
  sbn="Bch+Tp", ipa="[ʕ̞ + ʙ̥]", place="laryngeal + bilabial", manner="subharmonic + lip buzz", airstream="PE",
  voice="voiced", role="bass+melody", inst="Bass + brass", diff=5,
  lang="Not attested as a speech sound.",
  howto="Buzz a trumpet line with the lips while the throat holds a bass note underneath."),
"808-kick-bass-outward-sub-bass": dict(
  sbn="B808", ipa="[p'ˤ→ʕ̞]", place="bilabial → pharyngeal", manner="ejective into sustained bass", airstream="GE+PE",
  voice="voiceless onset, voiced tail", role="bass", inst="TR-808 kick", diff=4,
  lang="Bilabial ejectives are phonemic in Hausa, Quechua and Amharic.",
  howto="Start with a hard lip ejective for the attack, then open straight into a sustained low throat tone for the long decay.",
  notes="A structural copy of the TR-808 bass drum: short transient, then a tuned sine-like tail lasting hundreds of milliseconds."),
"cyclone-liproll": dict(
  sbn="BBcy", ipa="[ʙ̬ʷ]", place="bilabial", manner="trill (modulated)", airstream="PE",
  voice="voiced", role="bass", inst="Wobble bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Lip-roll while swirling the tongue so the timbre rotates. Measured near 56 Hz, among the lowest in the archive."),
"od-bass-least-bassy-bass": dict(
  sbn="Bod", ipa="[ʙ̬̈]", place="bilabial", manner="trill (thin)", airstream="PE",
  voice="voiced", role="bass", inst="Mid bass", diff=2,
  lang="Not attested as a speech sound.",
  howto="A deliberately light, high lip bass with little pharyngeal support — useful for texture rather than weight."),
"lip-oscillation": dict(
  sbn="BB", ipa="[ʙ̥]", place="bilabial", manner="trill (oscillation)", airstream="PE",
  voice="voiceless", role="bass", inst="Motor / engine", diff=2,
  lang="Bilabial trills are phonemic in Nias, Kele and Ngwe.",
  howto="Blow through loosely held lips with no voicing at all. The pitch is purely the mechanical flap rate of the lips.",
  notes="The base case of a buccal oscillator — the lungs supply energy but no vocal-fold vibration is involved."),
"tongue-bass-middle": dict(
  sbn="Btm", ipa="[ɭ̆ˤ]", place="alveolar (mid-tongue)", manner="oscillation (tongue)", airstream="BE",
  voice="voiceless", role="bass", inst="Sub bass / 808", diff=4,
  lang="Not attested as a speech sound in any language.",
  howto="Trap air between the tongue and the palate and let the centre of the tongue flap against the ridge, with the cheeks pressurising the pocket. The lungs are not used.",
  notes="Purely buccal: you can hold a tongue bass while breathing normally through the nose, which is why it underpins long technical patterns."),
"tongue-bass-side": dict(
  sbn="Bts", ipa="[ʟ̞̆ˤ]", place="lateral (tongue side)", manner="oscillation (lateral)", airstream="BE",
  voice="voiceless", role="bass", inst="Sub bass", diff=4,
  lang="Lateral clicks are phonemic in Xhosa and Zulu; lateral tongue oscillation is not.",
  howto="Let one side of the tongue flutter against the upper molars while the other side seals. Darker and more even than the middle version."),
"drill-bass": dict(
  sbn="Bdr", ipa="[ʙ̬r̥]", place="bilabial + uvular", manner="double oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Drill / reese bass", diff=5,
  lang="Not attested as a speech sound.",
  howto="Run a lip oscillation and a uvular rattle at the same time so the two vibration rates beat against each other."),
"overtone-tongue-bass": dict(
  sbn="Bto", ipa="[ɭ̆ˤ + ʍ]", place="alveolar + labial", manner="oscillation + resonance", airstream="BE",
  voice="voiceless", role="bass+melody", inst="Sub bass + overtone flute", diff=5,
  lang="Overtone singing (Tuvan khoomei, Mongolian) uses the same resonance technique but with vocal-fold phonation.",
  howto="Hold a tongue bass and shape the front cavity so one harmonic is boosted into an audible melody above the bass.",
  notes="Works on exactly the principle of Tuvan throat singing — filtering a fixed harmonic series — but with a buccal rather than laryngeal source."),
"whistle-bass-esh": dict(
  sbn="Besh", ipa="[ʕ̞ + ʃ]", place="laryngeal + postalveolar", manner="bass + fricative", airstream="PE",
  voice="voiced bass, voiceless noise", role="bass", inst="Sub bass + hats", diff=4,
  lang="Not attested as a simultaneous combination.",
  howto="Hold a low throat bass and let a continuous 'sh' escape over it, so the bass carries its own hi-hat layer.",
  notes="Measured near 57 Hz — one of the archive's lowest pitches, with the noise layer sitting three decades higher in frequency."),
"static-bass": dict(
  sbn="Bst", ipa="[ʙ̥̃]", place="bilabial", manner="oscillation (noisy)", airstream="PE",
  voice="voiceless", role="bass", inst="Distorted / bitcrushed bass", diff=3,
  lang="Not attested as a speech sound.",
  howto="Run a lip oscillation with an irregular seal so the buzz breaks up into noise — the aperiodicity is the point."),
"slizzer-bass": dict(
  sbn="Bsl", ipa="[ʙ̬ʲ]", place="bilabial + palatal", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Reese bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Lip bass with the tongue held high and forward, thinning the resonance into a sawtooth-like buzz."),
"lip-bass": dict(
  sbn="Blp", ipa="[ʙ̬ˠ]", place="bilabial", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Sub bass", diff=2,
  lang="Not attested with simultaneous voicing.",
  howto="The plain voiced lip bass — loose lips, low larynx, steady air. The starting point for most of the liproll family."),
"top-lip-fart-bass": dict(
  sbn="Btl", ipa="[ʙ̥↑]", place="bilabial (upper lip)", manner="oscillation (buccal)", airstream="BE",
  voice="voiceless", role="bass", inst="Sub bass / 808", diff=3,
  lang="Not attested as a speech sound.",
  howto="Pressurise the cheeks and let the upper lip flutter against the teeth. No lung air, so it can be held indefinitely.",
  notes="Measured as the darkest sound in the whole archive: almost all of its energy sits below 200 Hz."),
"hollow-lip-bass": dict(
  sbn="Bhl", ipa="[ʙ̬ˤ]", place="bilabial + pharyngeal", manner="oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Dub sub bass", diff=3,
  lang="Pharyngealisation is phonemic in Arabic.",
  howto="Lip bass with the throat opened and the larynx low, which adds a big hollow resonance under the buzz."),
"hollow-liproll-bass": dict(
  sbn="BBhl", ipa="[ʙ̬ˤ:]", place="bilabial + pharyngeal", manner="oscillation (rolled)", airstream="PE",
  voice="voiced", role="bass", inst="Dub sub bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="A sustained rolled version of the hollow lip bass, used to carry a whole bar under a pattern."),
"electro-bass": dict(
  sbn="Bel", ipa="[ʙ̬͡z]", place="bilabial + alveolar", manner="oscillation + buzz", airstream="PE",
  voice="voiced", role="bass", inst="Electro / acid bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Lip bass with a voiced alveolar buzz layered on top, giving a square-wave edge."),
"hard-bass": dict(
  sbn="BH", ipa="[ʙ̬̃ˤ]", place="bilabial + pharyngeal", manner="oscillation (distorted)", airstream="PE",
  voice="voiced, harsh", role="bass", inst="Distorted sub / brostep", diff=5,
  lang="Harsh voice quality occurs paralinguistically; it is not phonemic.",
  howto="Constrict the throat hard while lip-rolling so the tone tears into distortion. Known as demon, monster or evil bass depending on the scene.",
  notes="Loud and abrasive by design; the distortion is real aperiodicity in the source, not an effect."),
"air-bass": dict(
  sbn="Bair", ipa="[ʙ̥̞]", place="bilabial", manner="oscillation (breathy)", airstream="PE",
  voice="breathy", role="bass", inst="Soft sub", diff=2,
  lang="Not attested as a speech sound.",
  howto="A very light lip bass with much more air than buzz, used underneath quiet sections."),
"mortal-bass": dict(
  sbn="Bcj", ipa="[ʙ̬ˠ͡ʀ]", place="bilabial + uvular", manner="double oscillation", airstream="PE",
  voice="voiced", role="bass", inst="Growl bass", diff=5,
  lang="Uvular trills are phonemic in French and German.",
  howto="Layer a uvular growl under a lip bass. Named after the beatboxer CJ."),
"enel-bass": dict(
  sbn="Ben", ipa="[ʙ̬ˤ˩]", place="bilabial + pharyngeal", manner="oscillation (sub)", airstream="PE",
  voice="voiced", role="bass", inst="808 sub", diff=5,
  lang="Not attested as a speech sound.",
  howto="A very low, very slow lip bass with maximum pharyngeal space. Named for Enel.",
  notes="Measured at roughly 55 Hz — the lowest pitch in the archive, around A1."),
"snore-bass": dict(
  sbn="Bsn", ipa="[ʀ̝↓]", place="uvular/velar", manner="oscillation (velum)", airstream="PI",
  voice="voiced", role="bass", inst="Growl bass", diff=3,
  lang="Not attested as a speech sound; snoring is involuntary.",
  howto="Inhale through a relaxed velum and uvula so the soft palate flutters — a deliberate snore used as a bass.",
  notes="The soft palate is the oscillator here, which is why it works on the inhale."),
"liquid-bass": dict(
  sbn="Bliq", ipa="[ʙ̬ʷ~]", place="bilabial (saliva-loaded)", manner="oscillation (wet)", airstream="PE",
  voice="voiced", role="bass", inst="Wobble bass", diff=4,
  lang="Not attested as a speech sound.",
  howto="Lip bass with saliva in the seal so the vibration is irregular and gurgling."),
"cannon-bass": dict(
  sbn="Bcn", ipa="[p'ˤ:]", place="bilabial + pharyngeal", manner="ejective + resonant tail", airstream="GE",
  voice="voiceless onset", role="bass", inst="808 kick / cannon", diff=4,
  lang="Bilabial ejectives are phonemic in Hausa and Quechua.",
  howto="A single very hard lip ejective into a wide-open pharynx, so the mouth rings like a cannon barrel afterwards."),
}
