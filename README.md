# pfsv.github.io

Public portfolio for Hyeonseop Yoon, built with Astro and deployed with GitHub Pages.

The repository intentionally contains no diary, private study notes, client data, internal
infrastructure configuration, model weights, or generated artifacts.

## Local validation

```bash
npm ci
npm run build
```

The generated site is written to `dist/`.

## CV

The public CV is generated from a small ReportLab source so its content remains reviewable:

```bash
python3 scripts/generate_cv.py
```

This writes `public/assets/cv/hyeonseop_yoon_cv.pdf`. The public version includes only the owner's
undergraduate education and intentionally omits graduate enrollment, phone number, street address,
salary history, client identities, and other unnecessary personal data. Military status is included
by the owner's request.
