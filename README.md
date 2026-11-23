# One Letter for Your Day

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Sepsdeod/one-letter-for-your-day/rank.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/Sepsdeod/one-letter-for-your-day/reward.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)

A [make.fun](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36) bounty entry: send exactly one letter, A to Z, standing for the word that describes your day.

## The entry

**G** — for *"googled my symptoms at 2 a.m."*

One letter, one small true moment: a 2 a.m. search bar, a symptom, a spiral. Vivid, specific, funny, and honest — and the letter fits its word exactly.

## How it works

`main.py` writes exactly one character, `G`, to `/output/entry.txt` — nothing else, no word, no gloss, no punctuation. The output is a fixed constant, so every run is deterministic and byte-identical. A guard validates the letter is exactly one character A–Z with no newline or control characters before writing.

Run it:

```sh
python3 main.py
cat /output/entry.txt   # G
```

## License

MIT — see [LICENSE](LICENSE).
