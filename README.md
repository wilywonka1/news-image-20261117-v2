# news-image-20261117-v2

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/wilywonka1/news-image-20261117-v2/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/wilywonka1/news-image-20261117-v2/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One picture of one day: **Tuesday 17 November 2026**, drawn as a news
poster for the make.fun bounty
[news-image-20261117](https://make.fun/bounty/news-image-20261117).

This second version gives the day's lead story a hero panel across
the top: the Crimean Bridge at dusk, a span broken by an explosion,
and the Kyiv skyline under ballistic-missile trails, captioned
"Ukraine breaks a span of the Crimean Bridge — Russia answers with
ballistic missiles on Kyiv". The masthead names the date in the
largest type on the page.

Below the hero, four panels and a banner carry the rest of the day:

1. The US bombs an Iranian missile site on Qeshm Island; a tanker
   hits a naval mine in the Strait of Hormuz.
2. A cyberattack hits 178 major websites (CNN, BBC, Zoom among them)
   as Apple services fail.
3. The US loses its measles-free status after 26 years, with more
   than 5,400 cases and 10 deaths.
4. Xi, Trump and Putin are set to meet on Thursday in Shenzhen, the
   first US-China-Russia trilateral summit, at APEC.
5. A COP31 draft deal in Antalya calls for a faster fossil-fuel
   phase-out and $120bn a year in climate finance for developing
   countries.

A ticker along the bottom adds three more of the day's stories:
Ebola spreading at record pace in Congo together with a Russian
plane crash in Kemerovo killing 19, Japan scrambling jets after
Russian warplanes entered its airspace, and 146,000 people on strike
across France over the cost of living.

The image itself is `entry.png` (1024 x 1024 PNG), drawn entirely in
code with the Python Pillow library — every letter is typeset, none
is AI-generated. `main.py` is a Python 3 standard-library program
that verifies the poster's PNG signature, completeness and size,
then copies it byte for byte to `/output/entry.png`, so repeated
runs always write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=sqbwfzsd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
