# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A GitHub **profile README** repo (renders at github.com/RovshenAshirov). Not an app — there's no build, no tests, no dependencies. The deliverable is `README.md` itself.

## How the experience counter works

`README.md` contains a years-of-experience number wrapped in markers:

```
<!-- EXPERIENCE_START -->4+<!-- EXPERIENCE_END -->
```

`update_experience.py` computes `years = (today - 2021-11-01) / 365.25`, formats it as `N+`, and regex-replaces the text between those markers. Editing the number by hand is pointless — the workflow overwrites it.

- `.github/workflows/update_experience.yml` runs the script on the 1st of each month (and on manual `workflow_dispatch`), then commits any change as "Auto update experience".
- The start date `date(2021, 11, 1)` in `update_experience.py:3` is the only knob for the calculation.

Run it locally to preview:

```
python update_experience.py
```

## Editing notes

- The "Key Projects" table has an `(As of YYYY-MM-DD)` line that is **not** auto-updated — bump it by hand when you change project stats.
- Most badges/stats are external image URLs (shields.io, vercel, herokuapp) keyed to the `RovshenAshirov` username; they render on GitHub, not in local preview.