# Sources

## Recordings

All 200 sound recordings and 94 pattern recordings originate from **beatboxer.ir**,
built and performed by **Seyed Morteza Kamali** (github.com/smkplus).

- Site: https://www.beatboxer.ir/all-beatbox-sounds/
- Source: https://github.com/smkplus/beatboxer.github.io
- Licence: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

The files in `audio/` are the same recordings, silence-trimmed, converted to mono 32 kHz
and concatenated into sprite files with a 120 ms gap between clips. No other processing
was applied. `data.js` records the offset and duration of every clip.

The Standard Beatbox Notation strings in the pattern library are as published on
beatboxer.ir.

## Phonetics

- Proctor, M., Bresch, E., Byrd, D., Nayak, K. & Narayanan, S. (2013).
  *Paralinguistic mechanisms of production in human "beatboxing": a real-time magnetic
  resonance imaging study.* Journal of the Acoustical Society of America 133(2), 1043–1054.
  — the source for the analysis of the classic kick as a bilabial ejective [pʼ], the PF snare
  as [>pfʼ], the K snare as [kx:], and the finding that beatboxers use three of the four
  airstream mechanisms found in speech plus pulmonic ingressive airflow.
- Patil, N., Greer, T., Blaylock, R. & Narayanan, S. (2023).
  *Non-pulmonic initiation in human beatboxing: a real-time MRI study.* ICPhS 2023.
- Splinter & TyTe. *Standard Beatbox Notation (SBN).* humanbeatbox.com.
- The International Phonetic Alphabet (2020 revision) and the Extensions to the IPA
  (extIPA) for percussive and non-pulmonic symbols.

## Instrument reference ranges

Nominal published fundamental and spectral ranges for orchestral instruments, drum-kit
pieces and the Roland TR-808. These are reference values for comparison, not measurements
made under the same conditions as the archive.

## Measurement method

Implemented in `tools/analyze.py`. Each recording is decoded to mono 44.1 kHz, trimmed at
−45 dB relative to peak, and analysed with a 1024-sample Hann STFT at 50% overlap:

- **energy band** — 5th / 25th / 50th / 75th / 95th percentiles of the cumulative mean
  power spectrum.
- **brightness** — spectral centroid of the mean power spectrum.
- **noisiness** — spectral flatness (geometric mean over arithmetic mean of the spectrum).
- **fundamental** — normalised autocorrelation per 50 ms frame over frames above 25% of peak
  envelope, searching 45–4000 Hz past the first zero crossing, parabolically refined; the
  reported value is the median of frames whose peak correlation exceeds 0.45. Sounds with no
  such frames are reported as unpitched.
- **attack / decay** — envelope rise from onset to 90% of the first onset's local peak, and
  fall from that peak to −20 dB.
- **onset rate** — envelope crossings of 35% of peak with a 60 ms minimum gap.
