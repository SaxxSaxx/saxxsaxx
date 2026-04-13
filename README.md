<!-- Profile: github.com/SaxxSaxx/SaxxSaxx -->

<h1 align="center">Saxx</h1>
<p align="center"><strong>Python · desktop apps · automation · SMB web</strong></p>
<p align="center"><sub>GitHub: <code>SaxxSaxx</code> · Slovakia / remote</sub></p>

<p align="center">
  <a href="https://github.com/SaxxSaxx/mulebuy-gui"><img src="https://img.shields.io/badge/Featured-mulebuy--gui-0ea5e9?style=flat-square" alt="mulebuy-gui" /></a>
  <a href="https://github.com/SaxxSaxx/pex"><img src="https://img.shields.io/badge/Featured-pex-64748b?style=flat-square" alt="pex" /></a>
</p>

I build **focused tools**—PyQt / Electron-style workflows, Selenium glue, and **HTML/CSS template systems** for Slovak SMBs. Older one-off **demo-*** repos are legacy pitch sandboxes; I’m trimming the public list so only real projects surface.

---

### Public work (curated)

| | |
|:---|:---|
| **[mulebuy-gui](https://github.com/SaxxSaxx/mulebuy-gui)** | PyQt6 app + Selenium runner: config UI, logging, stats. You supply API keys. |
| **[pex](https://github.com/SaxxSaxx/pex)** | PE analyzer: imports/exports, strings, entropy, security flags—dark UI. |
| **[YTDLP-GUI](https://github.com/SaxxSaxx/YTDLP-GUI)** | **yt-dlp** GUI: playlists, audio/video, subtitles, history, dark mode. |
| **[clipboardmanager](https://github.com/SaxxSaxx/clipboardmanager)** | Clipboard history, timestamps, re-copy—offline, privacy-minded. |
| **[keycommander](https://github.com/SaxxSaxx/keycommander)** | Local typing stats & heatmaps (your machine only; not a “cloud” product). |
| **[templates-shop](https://github.com/SaxxSaxx/templates-shop)** | Hub for **HTML/CSS** kits: autoservis, salon, stavebná firma. |
| **[template-autoservis](https://github.com/SaxxSaxx/template-autoservis)** · **[template-kadernictvo](https://github.com/SaxxSaxx/template-kadernictvo)** · **[template-stavebnafirma](https://github.com/SaxxSaxx/template-stavebnafirma)** | Drop-in static templates. |
| **[premium-salon-theme](https://github.com/SaxxSaxx/premium-salon-theme)** | Next.js-leaning salon theme with booking-oriented layout. |
| **[S-P-autoservis](https://github.com/SaxxSaxx/S-P-autoservis)** | Example **delivered** autoservis site (portfolio). |

> **Tip:** On your GitHub profile, use **Customize pins** and pin **mulebuy-gui**, **pex**, and one template or **YTDLP-GUI** so visitors see quality first.

---

### AlphaFeed *(private — not on GitHub)*

**AlphaFeed** isn’t a missing link—it’s intentional. AlphaFeed is a **crypto intelligence / alerts** product (pump.fun–style signals, AI-scored news, Telegram bot, Solana USDC billing, XGBoost scoring on outcomes). Stack in production shape: **FastAPI**, **PostgreSQL**, **Redis**, **aiogram**, **Helius / Solana**. There is **no public repo** and none is planned here; it stays private for commercial and safety reasons.

---

### Local-only ideas (not uploaded)

- **`andrejpokorny` on GitHub:** There is **no user or org** with that exact handle on GitHub right now—so nothing to “merge” from that account. If you create it later, you can mirror selected repos there.
- **`~/Documents/projects/fake-gps-app`:** Electron + Python helper—interesting as a portfolio piece **only** if you’re comfortable with how “GPS spoofing” reads ethically; scrub any keys before a public push.
- **`~/Documents/Obsidian Vault/`** (e.g. `ALPHAFEED*.md`): **Personal notes**—do not bulk-publish; treat as private knowledge base.

---

### Cleaning up old `demo-*` repos

Bulk deletion needs an extra token scope. In a terminal (once):

```bash
gh auth refresh -h github.com -s delete_repo
```

Then remove the pitch sandboxes (same names you had on the account), for example:

```bash
gh repo list SaxxSaxx --limit 300 --json name -q '.[].name' \
  | grep -E '^demo-|^(receptiv-demo|s-p-autoservis-demo)$' \
  | while read -r r; do gh repo delete "SaxxSaxx/$r" --yes; done
```

Review the list **before** running if anything should be kept.

---

### Contact

[![Telegram](https://img.shields.io/badge/Telegram-@profilino-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/profilino)
[![Discord](https://img.shields.io/badge/Discord-s4xx-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discordapp.com/users/s4xx)

---

<p align="center"><sub>Profile README · <code>SaxxSaxx/SaxxSaxx</code> · updated 2026</sub></p>
