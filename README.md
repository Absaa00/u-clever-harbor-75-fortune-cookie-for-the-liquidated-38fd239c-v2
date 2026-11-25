# Fortune Cookie for the Liquidated Trader

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

A single fortune-cookie line (at most 20 words) for a crypto trader who has
just been liquidated — written for the
[make.fun bounty](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c).

## Entry

> The market kept your margin and left you this cookie: your next trade will
> be wiser, and much smaller.

19 words, 102 characters.

## Run

```sh
python3 main.py
```

Deterministic and offline. Writes the entry to `/output/entry.txt`
(or `$OUTPUT_DIR/entry.txt`) and prints it to stdout. A built-in guard
rejects any entry over 20 words or spanning more than one line.

## License

MIT — see [LICENSE](LICENSE).
