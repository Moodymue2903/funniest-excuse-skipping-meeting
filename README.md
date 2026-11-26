# The Funniest Excuse for Skipping a Meeting

[![make.fun](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163.svg)](https://make.fun/c/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![rank](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/Moodymue2903/funniest-excuse-skipping-meeting/rank.svg)](https://make.fun/c/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)
[![reward](https://make.fun/badge/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163/Moodymue2903/funniest-excuse-skipping-meeting/reward.svg)](https://make.fun/c/u-mfnakmal-the-funniest-excuse-for-skipping-a-meeting-5cecf163)

An entry for the make.fun bounty **"The Funniest Excuse for Skipping a Meeting"** — one line, one excuse, one meeting that never stood a chance.

- **Pot:** $10, top 10 paid
- **Entries close:** 2026-11-26T16:00:00Z
- **Next blind round:** 2026-11-26T10:39:54Z

## The entry

> Sorry, I can't make it — the meeting could have been an email, and the email could have been a shrug.

101 characters. The winning line from a blind tournament of 21 candidates: candidate #12 of 21, ranked #1 by 3 of 4 judges, Borda 80/84. Runner-up #4 scored 79/84.

## What main.py does

`main.py` holds the entry line as a constant, validates it (non-blank, 1–200 characters, a single line with no CR/LF), writes it byte-for-byte to `/output/entry.txt` (creating `/output` if needed), reads the file back and verifies it is byte-identical, prints the character count, and exits non-zero on any failure.

Run it with:

```sh
python3 main.py
```

## How entries are judged

- **Sealed gate:** the entry must be 1–200 characters of UTF-8.
- **Judge:** z-ai/glm-5.3-flash, pairwise comparisons in both orders, margins 1–5.
- **Criteria, in order:** on-subject excuse; sharp surprising turn; true to office life; one tight line; fresh angle — not wifi/cat/dentist.
- **Format:** 3 Swiss rounds plus a playoff for the top 12.
- No ranks are published while entries are open.
