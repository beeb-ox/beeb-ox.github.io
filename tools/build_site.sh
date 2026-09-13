#!/bin/sh
# Concatenate the source parts into the single-file site.
# out/p1..p8 are the authored parts: styles, markup, then the app in four chunks.
set -e
cd "$(dirname "$0")/.."
cat src/p1.html src/p2.html src/p3.html src/p4.html src/p5.html src/p6.html src/p7.html src/p8.html > build/body.html
cat tools/i18n/01_ui.js tools/i18n/02_terms.js tools/i18n/03_patterns.js tools/i18n/04_lang.js \
    tools/i18n/05_whistles.js tools/i18n/06_basses.js tools/i18n/07_core.js \
    tools/i18n/08_snares.js tools/i18n/09_rest.js > i18n.js
echo "wrote build/body.html and i18n.js — wrap body.html in a doctype/head/body to produce index.html"
