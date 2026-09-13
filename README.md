# Beatbox Sound Atlas

An open, measured archive of what the human mouth can do as a drum machine — and where it
stops. 200 beatbox sounds, each classified the way a phonetician would classify it
(place of articulation, manner, airstream mechanism, voicing) and each measured directly
from its recording (fundamental, spectral centroid, energy band, attack, decay, onset rate).

Live site: **https://beeb-ox.github.io/bbox-atlas/**

## What's here

| Path | What it is |
|---|---|
| `index.html` | The whole site: seven pages behind a hash router, one file, no build step, no dependencies. |
| `i18n.js` | The complete Chinese localisation — UI, all 200 specimen cards, all 94 pattern names, the coverage notes. English lives inline in `index.html` and is the fallback for any missing key. |
| `data.js` | The dataset the page reads: sounds, patterns, sprite offsets, coverage matrix. |
| `src/p1…p8.html` | The authored source parts `index.html` is concatenated from: styles, markup, then the app in five chunks. Edit these, not `index.html`. |
| `tools/build_site.sh` | Concatenates `src/` into the page and `tools/i18n/` into `i18n.js`. |
| `tools/i18n/` | The Chinese source files, one per sound family. |
| `atlas/`, `coverage/`, … | One-line redirect stubs so `/atlas/` resolves to `index.html#/atlas` for shareable links. |
| `data/sounds.json` | The 200-sound catalogue as plain JSON, without the per-sound spectrum arrays. |
| `data/patterns.json` | 94 patterns with Standard Beatbox Notation, audio offsets, and descriptive names. |
| `data/coverage.json` | The place × manner feasibility matrix (`S` attested in speech, `P` producible but unattested, `X` anatomically impossible) and the reason on each impossible cell. |
| `audio/` | 75 sprite files. All 200 sounds and 94 patterns are packed into these; `data.js` carries the start time and duration of each clip. Each sprite holds at most **45 s** of audio — see Audio below. |
| `tools/analyze.py` | Acoustic measurement: STFT, spectral percentiles, autocorrelation pitch tracking, envelope analysis. |
| `tools/build_audio.py` | Silence-trims, normalises and packs the source mp3s into sprites. |
| `tools/build_data.py` | Joins the taxonomy with the measurements and emits `data.js`. |
| `tools/pat_names.py` | Descriptive names for the 94 patterns, plus the two legends the source ran into its notation lines. |
| `tools/taxonomy/` | The hand-written classification: one Python dict per sound family. **This is the part that needs review.** |

## Pages and routing

Seven pages — home, the atlas, coverage, acoustics, hard limits, patterns, notation & sources —
routed on the URL hash (`index.html#/coverage`). Hash routing rather than separate documents
because the same file has to work both on GitHub Pages and inside a sandboxed single-page host;
the redirect stubs give pretty URLs on top. Each page's charts are built on first visit, so the
initial load only pays for the home page.

## Languages

English and 简体中文, switched by the globe button in the top bar and remembered in
`localStorage`. Everything is translated: the interface, all seven pages of copy, every one of
the 200 specimen cards (name, how-it's-made, notes, language attestation), all 94 pattern names,
and the reason on each anatomically impossible cell.

Technical terms are not translated string-by-string. `placeAtom` / `mannerAtom` / `instAtom` in
`i18n.js` hold the atoms ("bilabial" → 双唇, "ejective" → 挤喉音, "(rolled)" → 滚奏) and the page
composes them, because Chinese phonetic terminology stacks modifiers in the same order as English.
That covers several hundred phrases from about 350 entries and keeps the terminology consistent.
A `placePhrase` / `mannerPhrase` override wins where composition would read badly.

## Audio, and what mobile Safari demands

Playback is Web Audio first, with an `<audio>` element as the fallback. Three constraints shape
it, all learned from an iPhone not playing anything:

1. **A sprite is capped at 45 s** (`MAX_CHUNK` in `tools/build_audio.py`), which is why there
   are 75 files rather than 13. `decodeAudioData` produces float32 PCM at the *hardware* rate —
   48 kHz on an iPhone — so the old per-category sprites decoded to 40–80 MB each and the
   largest was ~80 MB. That reliably fails on a phone. At 45 s the worst decode is ~8 MB, and
   only the four most recently used buffers stay resident (`MAX_BUFS`).
2. **The AudioContext must emit something during a user gesture.** Creating it inside the tap
   handler is not enough if the next thing you do is `await fetch(...)`; by the time the buffer
   resolves the gesture is over and the context can still be suspended. `unlock()` plays a
   one-sample silent buffer synchronously on the first tap.
3. **`HTMLAudioElement.play()` must also be called inside the gesture** — never from a
   `loadedmetadata` handler, which is outside it and rejects with `NotAllowedError`. The
   fallback therefore calls `play()` immediately and seeks afterwards, asking for the slice with
   a media-fragment URI (`#t=start,end`) and falling back to setting `currentTime` once the
   media is seekable, with a capped number of attempts and a wall-clock stop if neither works.

Note that seeking needs HTTP **Range** support. GitHub Pages provides it; Python's
`http.server` does not, so the element fallback cannot be tested against `python -m http.server`
— it will appear to play the whole sprite from zero. `tools/rangeserve.py` is a minimal
Range-capable server for local testing.

When playback is refused the page says so rather than failing silently. On iPhone the other
thing to check is the hardware silent switch: Safari routes Web Audio through it.

## The classification fields

Every sound carries:

- **place** / **manner** — articulatory description, plus a normalised `gplace`/`gmanner` pair used to position it on the coverage chart.
- **airstream** — one or more of `PE` pulmonic egressive, `PI` pulmonic ingressive, `GE` glottalic egressive (ejective), `GI` glottalic ingressive (implosive), `LI` lingual ingressive (click), `BE`/`BI` buccal, `AE`/`AI` aerodynamic (whistle).
- **ipa** — a phonetic approximation of the gesture. Not a claim that the sound is a phoneme.
- **sbn** — Standard Beatbox Notation, the community shorthand.
- **lang** — whether the articulation is attested as a phoneme in a spoken language, with examples.
- **inst** — the drum-machine or orchestral instrument it stands in for.
- **howto** — how to produce it.
- **ac** — the measured acoustics.

## How to regenerate

The source recordings are not vendored here. To rebuild from scratch:

```sh
git clone --depth 1 https://github.com/smkplus/beatboxer.github.io.git
# point the S/A paths at the clone, then:
python3 tools/analyze.py        # measure every recording
python3 tools/build_audio.py    # pack sprites
python3 tools/build_data.py     # emit data.js
```

Requires `ffmpeg`, `numpy` and `scipy`.

## Known gaps and open questions

- **The taxonomy is a first pass.** Community sound names are inconsistent and several sounds
  in the archive are variants of one articulation under different names. Some IPA readings are
  arguable — especially in the snare and liproll families, where the difference between a
  glottalic ejective and a hard pulmonic release is not always audible from one recording.
- **Difficulty ratings are judgements**, not measurements.
- **Pattern names are ours.** The source archive numbers patterns only ("Pattern 1" … "Pattern 50"),
  so `tools/pat_names.py` gives each one a descriptive name based on what it actually plays. The
  original number is kept as `ref` on every pattern. Rename freely — nothing depends on the names.
- **No loudness data.** The recordings are uncalibrated, so nothing here says how loud any of
  these are relative to a real drum.
- **Only one performer.** Every recording comes from the same archive, so what is measured is
  one beatboxer's technique, not the range of the discipline.
- **The Chinese is a first translation**, not a reviewed one. Phonetic terminology in particular
  (发声态, 挤喉音, 口腔气流) follows standard Chinese linguistics usage as best we could, but a
  phonetician's pass would help.
- **Instrument reference ranges** are nominal published ranges, not measurements taken under
  the same conditions as the archive.

Corrections and additional recordings are welcome.

## Attribution and licence

Audio recordings © Seyed Morteza Kamali, from
[beatboxer.ir](https://www.beatboxer.ir/all-beatbox-sounds/)
([source repo](https://github.com/smkplus/beatboxer.github.io)), used under
**[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**. The sprite files in
`audio/` are re-encodings of that material and carry the same licence: **non-commercial use
only, attribution required**.

The classification, measurement code, dataset and site in this repository are released under
CC BY-NC 4.0 as well, so that the whole thing travels under one set of terms.

See `ATTRIBUTION.md` for the full source list.
