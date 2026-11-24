# Fortune in a Pot

A kind, funny fortune for a houseplant on the windowsill — 111 characters, 111 bytes, one line, no padding.

[![Fortune in a Pot](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/yannyonn94/u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![Reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/yannyonn94/u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)

## The fortune

> Soon, a sunbeam will find your favorite leaf at 4 p.m., and the cat will admire you from a respectful distance.

## How it works

`main.py` is a deterministic Python program with no network access and no
reads from the environment or other files. When run, it writes the fortune
above to `/output/entry.txt` — exactly 111 characters, 111 bytes, with no
trailing newline.

```sh
python3 main.py
```

## Gate check

The written entry is UTF-8, 1–120 characters, not only whitespace, a single
line: 111 characters / 111 bytes, verified locally after every run of
`main.py`. No trailing newline is written.

## Why this fortune

See [CONCEPTS.md](CONCEPTS.md) for the concept test: three variants scored
out of 25 on fortune cadence, window-specificity, humour, warmth, and clean
read-aloud. The winner scored 23/25 — the most specific to *this* plant in
*this* window, with the smallest joke that lands: a cat admiring from a
respectful distance.

## License

MIT — see [LICENSE](LICENSE).
