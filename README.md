# Retail Launch Agent

A Claude Code workspace for tracking Shopify Retail/POS merchant launches. Drop in weekly transcripts, emails, and notes — get structured risk registers, milestone tracking, and launch health summaries. Generates a static HTML dashboard you can host on GitHub Pages for team sharing and OOO coverage.

Built for Solutions Engineers on the Shopify Large Segment team.

---

## How It Works

```
intake files (transcripts, emails, notes)
      ↓
Claude Code agent reads CLAUDE.md instructions
      ↓
merchants/[Name]/ (launch-tracker.md, risk-register.md, health-summary.md)
      ↓
python3 scripts/generate-site.py
      ↓
docs/index.html → your private GitHub Pages URL
```

The agent extracts: milestone progress, risks (with severity and category), decisions, open questions, and next steps. It applies deterministic Red/Yellow/Green health logic on every update so you always have an honest picture of where each merchant stands.

---

## Prerequisites

- [Claude Code](https://claude.ai/claude-code) — the CLI or VS Code extension
- Python 3.8+ (for site generation — `python3 --version`)
- Git

---

## Setup

**1. Clone and open**
```bash
git clone https://github.com/YOUR_USERNAME/retail-launch-agent.git
cd retail-launch-agent
```
Open this folder in Claude Code: `claude .` (CLI) or open the folder in VS Code with the Claude Code extension.

**2. Create your personal config**
```bash
cp personal-config.md.template personal-config.md
```
Edit `personal-config.md` with your name, team, and region. This file is gitignored — it stays local.

**3. Replace the milestone framework**
Open `templates/milestone-framework.md` and replace the placeholder phases with your team's actual Shopify Retail/POS launch milestones. This is the reference the agent uses for all new merchants.

Also update the milestone table in `templates/launch-tracker.md` to match.

**4. Add your first merchant**

In Claude Code, say:
```
add merchant [Merchant Name]
```
The agent creates `merchants/[Name]/` with all template files and prompts for the launch target date and partner name.

---

## Weekly Workflow

**1. Drop intake files**

Copy transcripts, emails, or notes into `merchants/[Name]/intake/unprocessed/` as `.md` or `.txt` files.

Or drop files into the global `intake/` folder — the agent will ask which merchant they belong to.

**2. Process intake**

In Claude Code:
```
process intake for [Merchant Name]
```

The agent reads every file in `unprocessed/`, extracts all signals, updates the tracker and risk register, recalculates health, regenerates `health-summary.md`, and archives the processed files.

**3. Review the digest**

```
weekly digest
```

Prints a portfolio table: health per merchant, critical/high risks, launches within 30 days.

Or focus on what's broken:
```
what needs attention
```

**4. Generate and share the dashboard**

```
generate site
```

Opens `site/index.html` locally. To publish to your team:
```bash
bash scripts/publish.sh
```
(Requires one-time setup of a private GitHub repo — see Publishing below.)

---

## Agent Commands

| Command | What it does |
|---|---|
| `add merchant [Name]` | Create merchant folder from templates |
| `attach vtp for [Name]` | Read merchant's Vetted Technical Plan from `merchants/[Name]/vtp.md` — extracts scope, go-live dates, POS customizations, and integration landscape into the tracker |
| `process intake for [Name]` | Process all files in `merchants/[Name]/intake/unprocessed/` |
| `process intake` | Process global `intake/` drop zone (asks which merchant) |
| `weekly digest` | Portfolio health overview |
| `what needs attention` | Red/Yellow merchants only, with "why" narrative |
| `show risk report` | All Critical + High risks across portfolio |
| `show risk report for [Name]` | All risks for one merchant |
| `show milestone status for [Name]` | Milestone table with per-phase completion |
| `show acceleration opportunities for [Name]` | Specific actions to move the launch date earlier |
| `update health for [Name]` | Re-run health logic without processing new intake |
| `generate site` | Build `docs/` and `site/index.html` |

---

## Customization

**Milestone framework:** Edit `templates/milestone-framework.md`. Update `templates/launch-tracker.md` to match (the milestone rows in the table). New merchants will use the updated framework automatically.

**Risk categories:** Documented in `CLAUDE.md` Section 4. Add custom categories to the list if your merchants have unusual risk types.

**Health thresholds:** Defined in `CLAUDE.md` Section 5. Adjust the day-count thresholds if your standard implementation timeline differs.

**Dashboard title:** Set `dashboard_title` in `personal-config.md`.

---

## Publishing the Dashboard

The generated site goes to `docs/` (and `site/` for local preview). To share with your team via a URL:

**1. Create a private GitHub repo** for your merchant data (this is separate from the public template repo)

**2. Configure publish.sh**

Open `scripts/publish.sh` and set:
```bash
PRIVATE_REPO_URL="git@github.com:YOUR_USERNAME/YOUR_PRIVATE_REPO.git"
```

**3. Enable GitHub Pages** on the private repo: Settings → Pages → Source: `gh-pages` branch

**4. Push the site**
```bash
bash scripts/publish.sh
```

Your team can access the dashboard at `https://YOUR_USERNAME.github.io/YOUR_PRIVATE_REPO/`.

---

## Sample Data

`sample-merchant/` contains "Greenleaf Home Goods" — a fake 3-location home goods retailer at 🟡 YELLOW health. Use it to:
- See what a populated tracker looks like
- Test `python3 scripts/generate-site.py` without real merchant data
- Show teammates what the system does before they set up their own

---

## File Structure

```
Retail Launch Agent/
├── CLAUDE.md                        # Agent instructions (do not delete)
├── README.md
├── personal-config.md.template      # Copy → personal-config.md
├── .gitignore
│
├── templates/                       # Blank templates for new merchants
│   ├── launch-tracker.md
│   ├── risk-register.md
│   ├── milestone-framework.md       # Replace with your actual framework
│   └── health-summary.md
│
├── references/                      # Agent reference documents
│   └── vtp-template.md             # VTP structure + field extraction guide
│
├── sample-merchant/                 # Demo merchant — Greenleaf Home Goods
│
├── merchants/                       # Your real merchant data (gitignored)
├── intake/                          # Global drop zone (gitignored)
├── docs/                            # GitHub Pages output (gitignored)
├── site/                            # Local preview (gitignored)
│
└── scripts/
    ├── generate-site.py
    └── publish.sh
```

---

## Git Safety

**Real merchant data is gitignored.** The `merchants/`, `intake/`, `docs/`, and `site/` folders are all in `.gitignore`. The public template repo only contains: CLAUDE.md, templates, scripts, sample data, and README.

Before committing, verify with `git status` that no merchant folders are staged.

---

## About

Built for the Shopify Large Segment Solutions Engineering team. Designed for the unified D2C + Retail/POS model. Clone it, fill in your milestone framework and personal config, and it works for your own book of business.
