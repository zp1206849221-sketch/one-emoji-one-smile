[![make.fun bounty](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=one-emoji-one-smile)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/zp1206849221-sketch/one-emoji-one-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=one-emoji-one-smile)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=one-emoji-one-smile)

# One Emoji, One Smile

A tiny program with one job: pick the single emoji most likely to make a
stranger smile, and write it — and nothing else — to `/output/entry.txt`.

The pick is a hatching chick: small, kind, alive and gently silly. A tiny
creature arriving in the world reads as warm at first glance to anyone, of
any age or background, with no irony, intimacy or flirtation that could land
wrong coming from a stranger — and it is a chosen, slightly unexpected pick
rather than one of the stock smiley faces everyone sends. It is a single
Unicode codepoint (U+1F423), so the entry is exactly one character long.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Requires only the Python 3 standard library. `main.py` creates `/output`
if it does not exist yet.
