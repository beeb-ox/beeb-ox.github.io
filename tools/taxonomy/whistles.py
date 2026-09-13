# -*- coding: utf-8 -*-
# key = mp3 basename (without .mp3) within its category folder
TAX = {
"whistle": dict(
  sbn="~", ipa="[ʍ͡β̞ʷ]", place="labial (pucker)", manner="whistle", airstream="AE",
  voice="voiceless", role="melody", inst="Slide whistle / sine lead", diff=1,
  lang="Whistling is used as full speech in whistled languages (Silbo Gomero, Kickapoo) but is never a phoneme inside spoken words.",
  howto="Round the lips to a small aperture, arch the tongue low and flat, and blow steadily. Pitch is set by the volume of the mouth cavity in front of the tongue, not by the vocal folds — the larynx is silent.",
  notes="A Helmholtz resonator: the mouth is the cavity, the lip opening the neck. Because no vocal folds are involved, you can whistle and hum simultaneously."),
"cricket-whistle": dict(
  sbn="~i", ipa="[ʧ͡ʍ]", place="alveolar + labial", manner="whistle (pulsed)", airstream="AE",
  voice="voiceless", role="fx", inst="Insect / high shaker", diff=3,
  lang="Not attested as a speech sound.",
  howto="Set a very small tongue-tip-to-alveolar-ridge channel and blow hard enough that the airstream chirps rather than sustains. Short, rapid bursts at ~3 kHz."),
"bolbol-whistle": dict(
  sbn="~tr", ipa="[ʍ͡r̥]", place="labial + uvular", manner="whistle + trill", airstream="AE",
  voice="voiceless", role="melody", inst="Bird call / ocarina trill", diff=4,
  lang="Trilled whistling has no phonemic counterpart; uvular trilling does ([ʀ] in French, German).",
  howto="Whistle normally, then add water or saliva at the back of the tongue so the airstream flutters. Named after the Persian bolbol (nightingale).",
  notes="Measured as the longest sustained whistle in the archive — a demonstration of breath economy rather than a rhythmic sound."),
"beat-rhino-whistle": dict(
  sbn="~R", ipa="[ʍ̝ʷ]", place="labial", manner="whistle (overblown)", airstream="AE",
  voice="voiceless", role="melody", inst="Piccolo / whistle lead", diff=3,
  lang="Not attested as a speech sound.",
  howto="Overblow a pucker whistle so the resonator jumps to its second mode — a brighter, thinner tone about an octave up. Named after the beatboxer Beat Rhino."),
"ball-zee-whistle": dict(
  sbn="~Bz", ipa="[ʍ͡x]", place="labial + velar", manner="whistle + fricative", airstream="AE",
  voice="voiceless", role="melody", inst="Breathy flute", diff=3,
  lang="Not attested as a speech sound.",
  howto="Whistle while holding a velar constriction so friction noise rides on top of the tone. Popularised by Ball-Zee."),
"laser-whistle": dict(
  sbn="~↗", ipa="[ʍ↗]", place="labial", manner="whistle (glide)", airstream="AE",
  voice="voiceless", role="fx", inst="Synth pitch sweep", diff=2,
  lang="Pitch glides are phonemic as tone contours, but not as whistles.",
  howto="Whistle and sweep the tongue body forward or back fast, shrinking the front cavity to jump the pitch. The steep glide is what reads as a laser.",
  notes="Measured spectrum is a smear rather than a peak because the fundamental moves through more than an octave in under 100 ms."),
"inward-teeth-whistle": dict(
  sbn="^~t", ipa="[ʍ̃↓]", place="dental/labiodental", manner="whistle", airstream="AI",
  voice="voiceless", role="melody", inst="Whistle lead (inhaled)", diff=3,
  lang="Ingressive whistling is unattested in speech; ingressive speech itself is marginal (Damin, some ingressive fricatives in Tsou).",
  howto="Draw air in past the upper front teeth with the lower lip slightly retracted. Inhaled whistles let you whistle a melody and breathe at the same time.",
  notes="One of the two ways beatboxers escape the breath limit: the sound is produced on the inhale, so a line can run indefinitely."),
"outward-teeth-whistle": dict(
  sbn="~t", ipa="[ʍ̪]", place="dental/labiodental", manner="whistle", airstream="AE",
  voice="voiceless", role="melody", inst="Whistle lead", diff=2,
  lang="Not attested as a speech sound.",
  howto="Blow between the tongue tip and the upper teeth rather than through pursed lips. Brighter and quieter than a pucker whistle, and easier to articulate quickly."),
"pacmax-whale-train-whistle": dict(
  sbn="~W", ipa="[ʍ↗↘]", place="labial", manner="whistle (multi-tone)", airstream="AE",
  voice="voiceless", role="fx", inst="Train whistle / theremin", diff=4,
  lang="Not attested as a speech sound.",
  howto="Whistle with a deliberately unstable lip aperture so two resonator modes sound at once, then bend the pitch. Named for Pacmax."),
"recorder-whistle": dict(
  sbn="~rc", ipa="[ʍ̟]", place="labial + palatal", manner="whistle", airstream="AE",
  voice="voiceless", role="melody", inst="Recorder / fipple flute", diff=3,
  lang="Not attested as a speech sound.",
  howto="Whistle with the tongue high and forward against the palate to create a narrow duct, imitating a recorder's fipple. Tone is pure with almost no breath noise."),
"bird-whistle": dict(
  sbn="~bd", ipa="[ʍ↗↗]", place="labial", manner="whistle (trilled glide)", airstream="AE",
  voice="voiceless", role="fx", inst="Bird call", diff=3,
  lang="Not attested as a speech sound.",
  howto="Very small aperture, high tongue, and rapid pitch flicks from the jaw and tongue body. Sits around 3 kHz — the top of the archive's pitched range."),
"finger-whistle": dict(
  sbn="~fg", ipa="[ʍ]", place="labial (finger-assisted)", manner="whistle", airstream="AE",
  voice="voiceless", role="melody", inst="Referee whistle", diff=4,
  lang="Not attested as a speech sound.",
  howto="Fold the tongue back with one or two fingers and blow across the resulting edge. The fingers do the work the lips normally do, which is why it is far louder.",
  notes="The loudest sound a human mouth makes without amplification — the only entry here whose acoustic ceiling is set by the fingers, not the vocal tract."),
"dekoy-whistle": dict(
  sbn="~dk", ipa="[ʍ͡ʜ]", place="labial + pharyngeal", manner="whistle + friction", airstream="AE",
  voice="voiceless", role="fx", inst="Duck call / kazoo", diff=4,
  lang="Pharyngeal fricatives are phonemic in Arabic and Hebrew; whistling with them is not.",
  howto="Whistle with a tight pharynx so a rasp accompanies the tone. Named after the beatboxer Dekoy."),
"ralik-whistle": dict(
  sbn="~hz", ipa="[ʍ̤]", place="labial", manner="whistle (breathy)", airstream="AE",
  voice="breathy", role="melody", inst="Breathy flute / shakuhachi", diff=3,
  lang="Breathy voice is phonemic in Hindi and Gujarati; breathy whistling is not.",
  howto="Whistle with the vocal folds slightly open so a layer of breath sits under the tone. Named for Heartzel / Raik."),
"vortex-whistle": dict(
  sbn="~vx", ipa="[ʍ͡ʃ]", place="labial + postalveolar", manner="whistle + fricative", airstream="AE",
  voice="voiceless", role="fx", inst="Wind / vinyl noise", diff=3,
  lang="Not attested as a speech sound.",
  howto="Spin the airstream against the side of the tongue while whistling so the tone is wrapped in a hiss."),
"calexy-babeli whistle": dict(
  sbn="~cx", ipa="[ʍ̞]", place="labial", manner="whistle (low)", airstream="AE",
  voice="voiceless", role="bass", inst="Bass flute / sub sine", diff=4,
  lang="Not attested as a speech sound.",
  howto="Open the jaw wide and drop the tongue to enlarge the resonating cavity, pushing the whistle down toward 440 Hz. Named for Calexy / Babeli.",
  notes="The lowest whistle measured in the archive — the practical floor for a mouth-cavity Helmholtz resonator."),
"hollow-whistle": dict(
  sbn="~ho", ipa="[ʍˤ]", place="labial + pharyngeal", manner="whistle", airstream="AE",
  voice="voiceless", role="melody", inst="Ocarina", diff=3,
  lang="Pharyngealisation is phonemic in Arabic ([sˤ], [tˤ]).",
  howto="Whistle with the larynx low and the pharynx expanded. The extra back cavity adds a hollow, woody colour and drops the pitch."),
"tongue-flute": dict(
  sbn="~tf", ipa="[ʎ̝̊]", place="palatal", manner="whistle (lateral)", airstream="AE",
  voice="voiceless", role="melody", inst="Flute / ney", diff=4,
  lang="Voiceless lateral fricatives are phonemic in Welsh ([ɬ]) and Nahuatl; the whistled version is not.",
  howto="Curl the tongue into a tube and blow through it as though it were a flute head-joint, with the lips only loosely involved."),
"throat-whistle": dict(
  sbn="~th", ipa="[ʁ̝̊ʷ]", place="uvular/pharyngeal", manner="whistle", airstream="AE",
  voice="voiceless", role="fx", inst="Kettle / steam", diff=5,
  lang="Not attested as a speech sound.",
  howto="Narrow the airway at the uvula until it whistles on its own, with the mouth open. The resonator is behind the tongue, not in front of it.",
  notes="A rare inversion — the whistle source is posterior, so the pitch is controlled by the pharynx instead of the lips."),
"cyclone-whistle": dict(
  sbn="~cy", ipa="[ʍ͡r̥ʷ]", place="labial", manner="whistle + flutter", airstream="AE",
  voice="voiceless", role="fx", inst="Siren / wind", diff=4,
  lang="Not attested as a speech sound.",
  howto="Whistle while swirling saliva or the tongue sides so the tone is modulated at a few tens of hertz."),
"whisper-zekka-whistle": dict(
  sbn="~wz", ipa="[ʍ̥]", place="labial", manner="whistle (very quiet)", airstream="AE",
  voice="voiceless", role="melody", inst="Soft sine", diff=3,
  lang="Not attested as a speech sound.",
  howto="Whistle at the lowest airflow that still sustains a tone. Used to drop dynamic level without losing the melody. Named for Zekka."),
"whale-whistle": dict(
  sbn="~wh", ipa="[ʍ↗↘↗]", place="labial", manner="whistle (portamento)", airstream="AE",
  voice="voiceless", role="fx", inst="Whale song / theremin", diff=3,
  lang="Not attested as a speech sound.",
  howto="Whistle and glide continuously through a wide interval without stopping the air, so the pitch never settles."),
"double-voice": dict(
  sbn="~+V", ipa="[ʍ + V̰]", place="labial + glottal", manner="whistle over voice", airstream="AE+PE",
  voice="voiced + voiceless", role="melody", inst="Two-part harmony", diff=4,
  lang="No spoken language contrasts two simultaneous independent pitches from one speaker.",
  howto="Whistle and hum at the same time. The whistle is driven by the lip aperture and the hum by the vocal folds, so the two pitches are genuinely independent.",
  notes="The clearest example of true human polyphony: two separate sound sources, two separate pitches, one performer."),
"helium-whistle": dict(
  sbn="~he", ipa="[ʍ̟ʰ]", place="labial", manner="whistle (very high)", airstream="AE",
  voice="voiceless", role="melody", inst="Piccolo", diff=4,
  lang="Not attested as a speech sound.",
  howto="Shrink the front cavity to its minimum with the tongue high and forward, pushing the whistle to the top of its range. Named for Helium, not for the gas."),
"hand-whistle": dict(
  sbn="~hd", ipa="[ʍ͡ʘ]", place="labial (hand cavity)", manner="whistle (external resonator)", airstream="AE",
  voice="voiceless", role="fx", inst="Ocarina / owl hoot", diff=3,
  lang="Not attested as a speech sound.",
  howto="Cup both hands to form a sealed chamber, blow across the gap between the thumbs, and open a finger to change pitch.",
  notes="The only sound in the archive whose resonator is outside the body — the limit case of 'human' sound production."),
}
