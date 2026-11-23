# The One-Line Laugh

[![The One-Line Laugh](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Flowjack94/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Flowjack94/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for [The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
on [make.fun](https://make.fun): one funny line, at most 200 characters, judged
pairwise by a stand-up comic persona on surprise, everyday truth, and economy
of words.

## The line

> I asked AI to write my dating profile and now even my own bio swiped left on me.

80 characters, one sentence.

## Run

```sh
python3 main.py
```

`main.py` (Python standard library only) writes the line deterministically to
`/output/entry.txt`, then reads it back and validates it against the
competition gate: UTF-8 text, 1–200 characters, not only whitespace, exactly
one sentence. It exits non-zero if any check fails.

## License

MIT — see [LICENSE](LICENSE).
