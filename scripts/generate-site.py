#!/usr/bin/env python3
"""
Retail Launch Agent — Static Site Generator
Reads merchants/ folder and sample-merchant/ and generates an HTML dashboard.

Usage:
    python3 scripts/generate-site.py
    python3 scripts/generate-site.py --merchants-dir ./merchants --output-dir ./docs

Output: docs/index.html and site/index.html
"""

import os
import re
import sys
import html
import shutil
import argparse
from datetime import date, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
ROOT = SCRIPT_DIR.parent

def parse_args():
    p = argparse.ArgumentParser(description="Generate retail launch portfolio site")
    p.add_argument("--merchants-dir", default=str(ROOT / "merchants"), help="Path to merchants directory")
    p.add_argument("--output-dir", default=str(ROOT / "docs"), help="Primary output directory (GitHub Pages)")
    p.add_argument("--preview-dir", default=str(ROOT / "site"), help="Local preview directory")
    p.add_argument("--include-sample", default=True, action=argparse.BooleanOptionalAction, help="Include sample-merchant in output")
    return p.parse_args()

# ---------------------------------------------------------------------------
# Markdown / frontmatter parsing helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict:
    """Extract YAML-style frontmatter from a markdown file."""
    result = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return result
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            break
        if ":" in line:
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def extract_section(text: str, heading: str) -> str:
    """Extract text between a ## heading and the next ## heading."""
    pattern = rf"##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)"
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


def parse_milestone_table(text: str) -> tuple[int, int]:
    """
    Parse the milestone table in launch-tracker.md.
    Returns (complete_count, total_count).
    """
    section = extract_section(text, "Milestone Progress")
    if not section:
        return 0, 0

    total = 0
    complete = 0
    for line in section.splitlines():
        # Match table rows (not header or separator rows)
        if "|" in line and "---" not in line and "Phase" not in line:
            cols = [c.strip() for c in line.split("|") if c.strip()]
            if len(cols) >= 3:
                status = cols[2].strip() if len(cols) > 2 else ""
                if status in ("Not Started", "In Progress", "Complete", "Blocked"):
                    total += 1
                    if status == "Complete":
                        complete += 1
    return complete, total


def parse_active_risks(text: str) -> list[dict]:
    """
    Parse the Active Risks table from risk-register.md.
    Returns list of dicts with: id, severity, severity_order, category, description, owner, due, status
    """
    SEVERITY_ORDER = {"Critical": 0, "🔴 Critical": 0, "High": 1, "🟠 High": 1,
                      "Med": 2, "🟡 Med": 2, "Low": 3, "⚪ Low": 3}

    section = extract_section(text, "Active Risks")
    if not section:
        return []

    risks = []
    for line in section.splitlines():
        if "|" not in line or "---" in line or "ID" in line:
            continue
        cols = [c.strip() for c in line.split("|")]
        cols = [c for c in cols if c or c == ""]  # keep empty cols
        # Remove leading/trailing empty from split
        while cols and not cols[0]:
            cols.pop(0)
        while cols and not cols[-1]:
            cols.pop()

        if len(cols) < 4:
            continue

        # Expected: ID | Severity | Category | Description | Owner | Due | Status
        risk_id       = cols[0] if len(cols) > 0 else ""
        severity_raw  = cols[1] if len(cols) > 1 else ""
        category      = cols[2] if len(cols) > 2 else ""
        description   = cols[3] if len(cols) > 3 else ""
        owner         = cols[4] if len(cols) > 4 else ""
        due           = cols[5] if len(cols) > 5 else ""
        status        = cols[6] if len(cols) > 6 else "Open"

        if not risk_id or not severity_raw:
            continue

        # Normalize severity text (strip emoji)
        sev_clean = re.sub(r"[🔴🟠🟡⚪]\s*", "", severity_raw).strip()
        sev_order = SEVERITY_ORDER.get(severity_raw, SEVERITY_ORDER.get(sev_clean, 99))

        risks.append({
            "id": risk_id,
            "severity": sev_clean,
            "severity_raw": severity_raw,
            "severity_order": sev_order,
            "category": category,
            "description": description,
            "owner": owner,
            "due": due,
            "status": status,
        })

    return risks


def parse_health_rationale(text: str) -> list[str]:
    """Extract bullet points from the Health Rationale section."""
    section = extract_section(text, "Health Rationale")
    bullets = []
    for line in section.splitlines():
        line = line.strip()
        if line.startswith("- ") or line.startswith("* "):
            bullets.append(line[2:].strip())
    return bullets


def parse_last_intake(text: str) -> str:
    """Extract last intake date from health-summary.md frontmatter or body."""
    fm = parse_frontmatter(text)
    if fm.get("generated"):
        return fm["generated"][:10]
    # Try body
    m = re.search(r"\*\*Last Intake Processed:\*\*\s*(\S+)", text)
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# Merchant data loader
# ---------------------------------------------------------------------------

def load_merchant(folder: Path, merchant_name: str | None = None) -> dict | None:
    """
    Load a merchant's data from a folder.
    Returns a dict with all parsed data, or None if essential files are missing.
    """
    tracker_path  = folder / "launch-tracker.md"
    risks_path    = folder / "risk-register.md"
    health_path   = folder / "health-summary.md"

    name = merchant_name or folder.name

    # Tracker is required
    if not tracker_path.exists():
        print(f"  WARNING: {name} — launch-tracker.md not found, skipping", file=sys.stderr)
        return None

    tracker_text = tracker_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(tracker_text)

    # Merge frontmatter name
    display_name = fm.get("merchant") or name
    launch_target = fm.get("launch_target", "")
    health = fm.get("launch_health", "RED").upper()
    last_updated = fm.get("last_updated", "")
    se_owner = fm.get("se_owner", "")
    partner = fm.get("partner", "")

    # Milestones
    complete, total = parse_milestone_table(tracker_text)
    pct = int(complete / total * 100) if total > 0 else 0

    # Risks
    risks = []
    if risks_path.exists():
        risks_text = risks_path.read_text(encoding="utf-8")
        risks = parse_active_risks(risks_text)
    else:
        print(f"  WARNING: {name} — risk-register.md not found", file=sys.stderr)

    open_risks = [r for r in risks if r["status"].lower() == "open"]
    critical_high = [r for r in open_risks if r["severity_order"] <= 1]
    top_risks = sorted(open_risks, key=lambda r: r["severity_order"])[:3]

    # Health rationale
    rationale = []
    last_intake = last_updated
    if health_path.exists():
        health_text = health_path.read_text(encoding="utf-8")
        rationale = parse_health_rationale(health_text)
        last_intake = parse_last_intake(health_text) or last_updated

    # Days to launch
    days_to_launch = None
    if launch_target:
        try:
            target_date = date.fromisoformat(launch_target)
            days_to_launch = (target_date - date.today()).days
        except ValueError:
            pass

    return {
        "name": display_name,
        "folder": str(folder.name),
        "health": health,
        "launch_target": launch_target,
        "days_to_launch": days_to_launch,
        "last_updated": last_updated,
        "last_intake": last_intake,
        "se_owner": se_owner,
        "partner": partner,
        "milestones_complete": complete,
        "milestones_total": total,
        "milestones_pct": pct,
        "all_risks": risks,
        "open_risks": open_risks,
        "critical_high_risks": critical_high,
        "top_risks": top_risks,
        "rationale": rationale,
    }


def load_all_merchants(merchants_dir: Path, include_sample: bool = True) -> list[dict]:
    merchants = []
    sample_dir = ROOT / "sample-merchant"

    # Load real merchants
    if merchants_dir.exists():
        for folder in sorted(merchants_dir.iterdir()):
            if folder.is_dir() and not folder.name.startswith("."):
                m = load_merchant(folder)
                if m:
                    merchants.append(m)

    # Load sample merchant
    if include_sample and sample_dir.exists():
        m = load_merchant(sample_dir, "Greenleaf Home Goods (Sample)")
        if m:
            merchants.append(m)

    return merchants


# ---------------------------------------------------------------------------
# HTML generation helpers
# ---------------------------------------------------------------------------

HEALTH_CONFIG = {
    "RED":    {"emoji": "🔴", "label": "RED — At Risk",          "bg": "#FFEAEA", "border": "#E3272C", "badge_bg": "#E3272C", "badge_fg": "#FFFFFF"},
    "YELLOW": {"emoji": "🟡", "label": "YELLOW — Needs Attention","bg": "#FFFBEA", "border": "#FFC96B", "badge_bg": "#FFC96B", "badge_fg": "#202223"},
    "GREEN":  {"emoji": "🟢", "label": "GREEN — On Track",        "bg": "#F1F8F5", "border": "#008060", "badge_bg": "#008060", "badge_fg": "#FFFFFF"},
}

SEVERITY_CONFIG = {
    "Critical": {"bg": "#E3272C", "fg": "#FFFFFF"},
    "High":     {"bg": "#F49342", "fg": "#FFFFFF"},
    "Med":      {"bg": "#FFC96B", "fg": "#202223"},
    "Low":      {"bg": "#E4E5E7", "fg": "#202223"},
}

def h(text: str) -> str:
    """HTML-escape a string."""
    return html.escape(str(text))


def health_badge(health: str) -> str:
    cfg = HEALTH_CONFIG.get(health, HEALTH_CONFIG["RED"])
    return (
        f'<span class="badge" style="background:{cfg["badge_bg"]};color:{cfg["badge_fg"]}">'
        f'{cfg["emoji"]} {cfg["label"]}'
        f'</span>'
    )


def severity_badge(severity: str) -> str:
    cfg = SEVERITY_CONFIG.get(severity, SEVERITY_CONFIG["Low"])
    return (
        f'<span class="badge sev-badge" style="background:{cfg["bg"]};color:{cfg["fg"]}">'
        f'{h(severity)}'
        f'</span>'
    )


def progress_bar(pct: int) -> str:
    color = "#008060" if pct >= 75 else "#FFC96B" if pct >= 40 else "#E3272C"
    return (
        f'<div class="progress-outer">'
        f'  <div class="progress-fill" style="width:{pct}%;background:{color}"></div>'
        f'</div>'
        f'<span class="progress-label">{pct}%</span>'
    )


def days_chip(days: int | None) -> str:
    if days is None:
        return '<span class="days-chip">Date TBD</span>'
    if days < 0:
        color = "#6D7175"
        label = f"Launched {abs(days)}d ago"
    elif days <= 7:
        color = "#E3272C"
        label = f"{days}d to go-live"
    elif days <= 14:
        color = "#F49342"
        label = f"{days}d to go-live"
    else:
        color = "#008060"
        label = f"{days}d to go-live"
    return f'<span class="days-chip" style="color:{color};font-weight:600">{h(label)}</span>'


# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: #F6F6F7;
  color: #202223;
  font-size: 14px;
  line-height: 1.5;
}

a { color: #005BD3; text-decoration: none; }
a:hover { text-decoration: underline; }

/* Header */
.header {
  background: #202223;
  color: #FFFFFF;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}
.header h1 { font-size: 18px; font-weight: 600; }
.header .meta { font-size: 12px; color: #A2A8AF; }

/* Summary bar */
.summary-bar {
  background: #FFFFFF;
  border-bottom: 1px solid #E1E3E5;
  padding: 12px 24px;
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
  align-items: center;
}
.stat-chip {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
}
.stat-chip .num {
  font-size: 22px;
  font-weight: 700;
  line-height: 1;
}
.stat-chip.total .num { color: #202223; }
.stat-chip.green .num { color: #008060; }
.stat-chip.yellow .num { color: #B7621D; }
.stat-chip.red .num   { color: #E3272C; }

/* Main content */
.main { padding: 24px; max-width: 1400px; margin: 0 auto; }

/* Section headings */
.section-heading {
  font-size: 16px;
  font-weight: 600;
  margin: 32px 0 16px;
  padding-bottom: 8px;
  border-bottom: 2px solid #E1E3E5;
}

/* Merchant cards grid */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}

.card {
  background: #FFFFFF;
  border: 1px solid #E1E3E5;
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 8px;
}
.card-header h2 { font-size: 15px; font-weight: 600; flex: 1; }
.card-header .badge { white-space: nowrap; }

.card-meta { font-size: 12px; color: #6D7175; display: flex; flex-wrap: wrap; gap: 6px 16px; }

/* Progress */
.progress-row { display: flex; align-items: center; gap: 10px; }
.progress-outer { flex: 1; height: 8px; background: #E1E3E5; border-radius: 4px; overflow: hidden; }
.progress-fill  { height: 100%; border-radius: 4px; transition: width 0.3s; }
.progress-label { font-size: 12px; color: #6D7175; white-space: nowrap; }

/* Risks */
.risks-list { display: flex; flex-direction: column; gap: 4px; }
.risk-item { font-size: 12px; display: flex; align-items: flex-start; gap: 6px; }
.risk-item .sev-badge { font-size: 11px; white-space: nowrap; }
.risk-desc { flex: 1; color: #202223; }

/* Badge */
.badge {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
  white-space: nowrap;
}
.sev-badge { padding: 2px 6px; border-radius: 4px; }

/* Days chip */
.days-chip { font-size: 12px; }

/* No risks */
.no-risks { font-size: 12px; color: #008060; }

/* Risk table */
.risk-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.risk-table th {
  background: #F6F6F7;
  border-bottom: 2px solid #E1E3E5;
  padding: 8px 12px;
  text-align: left;
  font-weight: 600;
  white-space: nowrap;
}
.risk-table td {
  border-bottom: 1px solid #E1E3E5;
  padding: 8px 12px;
  vertical-align: top;
}
.risk-table tr:last-child td { border-bottom: none; }
.risk-table tr:hover td { background: #F6F6F7; }
.risk-table .desc { max-width: 400px; }

/* Footer */
.footer {
  text-align: center;
  font-size: 12px;
  color: #A2A8AF;
  padding: 32px 24px 24px;
}

/* No merchants placeholder */
.empty-state {
  text-align: center;
  padding: 48px;
  color: #6D7175;
  background: #FFFFFF;
  border: 1px dashed #C9CCCF;
  border-radius: 8px;
  font-size: 14px;
}
.empty-state p + p { margin-top: 8px; }

/* Responsive */
@media (max-width: 600px) {
  .header { padding: 12px 16px; }
  .main { padding: 16px; }
  .summary-bar { padding: 10px 16px; gap: 12px; }
}
"""


def render_card(m: dict) -> str:
    health_cfg = HEALTH_CONFIG.get(m["health"], HEALTH_CONFIG["RED"])

    # Partner line
    partner_line = ""
    if m.get("partner") and m["partner"].lower() not in ("", "none", "[partner name]"):
        partner_line = f'<span>Partner: {h(m["partner"])}</span>'

    # SE line
    se_line = f'<span>SE: {h(m["se_owner"])}</span>' if m.get("se_owner") else ""

    # Target date
    date_line = f'<span>Target: {h(m["launch_target"])}</span>' if m.get("launch_target") else ""

    # Progress
    pct = m["milestones_pct"]
    prog = progress_bar(pct)
    milestones_label = f'{m["milestones_complete"]} / {m["milestones_total"]} milestones'

    # Top risks
    if m["top_risks"]:
        risk_items = ""
        for r in m["top_risks"]:
            desc_short = r["description"][:120] + ("…" if len(r["description"]) > 120 else "")
            risk_items += f'<div class="risk-item">{severity_badge(r["severity"])}<span class="risk-desc">{h(desc_short)}</span></div>'
        risks_html = f'<div class="risks-list">{risk_items}</div>'
    else:
        risks_html = '<p class="no-risks">✓ No open Critical/High risks</p>'

    # Last updated
    last = m.get("last_intake") or m.get("last_updated") or "Unknown"
    last_line = f'<span>Updated: {h(last)}</span>'

    return f"""
    <div class="card" style="border-top: 3px solid {health_cfg["border"]}">
      <div class="card-header">
        <h2>{h(m["name"])}</h2>
        {health_badge(m["health"])}
      </div>
      <div class="card-meta">
        {date_line}
        {days_chip(m["days_to_launch"])}
        {se_line}
        {partner_line}
      </div>
      <div class="progress-row">
        {prog}
        <span style="font-size:12px;color:#6D7175">{h(milestones_label)}</span>
      </div>
      {risks_html}
      <div class="card-meta">{last_line}</div>
    </div>
    """


def render_portfolio_risk_table(merchants: list[dict]) -> str:
    # Collect all Critical + High open risks across all merchants
    rows = []
    for m in merchants:
        for r in m["open_risks"]:
            if r["severity_order"] <= 1:  # Critical or High
                rows.append({**r, "merchant": m["name"]})

    if not rows:
        return '<p style="color:#6D7175;font-size:14px;">No Critical or High open risks across portfolio. 🟢</p>'

    rows.sort(key=lambda r: (r["severity_order"], r.get("due", "9999-99-99")))

    rows_html = ""
    for r in rows:
        desc_short = r["description"][:200] + ("…" if len(r["description"]) > 200 else "")
        rows_html += f"""
        <tr>
          <td>{severity_badge(r["severity"])}</td>
          <td>{h(r["merchant"])}</td>
          <td>{h(r["id"])}</td>
          <td class="desc">{h(desc_short)}</td>
          <td>{h(r["category"])}</td>
          <td>{h(r["owner"])}</td>
          <td>{h(r["due"])}</td>
        </tr>
        """

    return f"""
    <table class="risk-table">
      <thead>
        <tr>
          <th>Severity</th>
          <th>Merchant</th>
          <th>ID</th>
          <th>Risk</th>
          <th>Category</th>
          <th>Owner</th>
          <th>Due</th>
        </tr>
      </thead>
      <tbody>{rows_html}</tbody>
    </table>
    """


def render_html(merchants: list[dict], generated_at: str) -> str:
    # Summary counts
    total = len(merchants)
    red    = sum(1 for m in merchants if m["health"] == "RED")
    yellow = sum(1 for m in merchants if m["health"] == "YELLOW")
    green  = sum(1 for m in merchants if m["health"] == "GREEN")
    total_crit_high = sum(len(m["critical_high_risks"]) for m in merchants)

    # Cards
    if merchants:
        cards_html = "".join(render_card(m) for m in merchants)
        cards_section = f'<div class="cards-grid">{cards_html}</div>'
    else:
        cards_section = """
        <div class="empty-state">
          <p><strong>No merchants yet.</strong></p>
          <p>Say <code>add merchant [Name]</code> in Claude Code to create your first merchant folder.</p>
          <p>Then drop intake files into <code>merchants/[Name]/intake/unprocessed/</code> and say <code>process intake for [Name]</code>.</p>
        </div>
        """

    risk_table = render_portfolio_risk_table(merchants)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Retail Launch Portfolio</title>
  <style>{CSS}</style>
</head>
<body>

<header class="header">
  <h1>Retail Launch Portfolio</h1>
  <span class="meta">Generated {h(generated_at)}</span>
</header>

<div class="summary-bar">
  <div class="stat-chip total"><span class="num">{total}</span><span>Merchants</span></div>
  <div class="stat-chip green"><span class="num">{green}</span><span>🟢 On Track</span></div>
  <div class="stat-chip yellow"><span class="num">{yellow}</span><span>🟡 Needs Attention</span></div>
  <div class="stat-chip red"><span class="num">{red}</span><span>🔴 At Risk</span></div>
  <div class="stat-chip" style="margin-left:auto;color:#6D7175">
    <span>{total_crit_high} open Critical/High risks</span>
  </div>
</div>

<main class="main">

  <h2 class="section-heading">Launch Health by Merchant</h2>
  {cards_section}

  <h2 class="section-heading">Portfolio Risk Table — Critical &amp; High</h2>
  {risk_table}

</main>

<footer class="footer">
  <p>Retail Launch Agent &bull; Generated {h(generated_at)}</p>
  <p>Data from local merchant folders &bull; Not for external distribution</p>
</footer>

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    merchants_dir = Path(args.merchants_dir)
    output_dir    = Path(args.output_dir)
    preview_dir   = Path(args.preview_dir)

    print("Retail Launch Agent — Site Generator")
    print(f"  Merchants dir : {merchants_dir}")
    print(f"  Output dir    : {output_dir}")
    print(f"  Preview dir   : {preview_dir}")
    print()

    # Load merchants
    merchants = load_all_merchants(merchants_dir, include_sample=args.include_sample)

    if not merchants:
        print("No merchants found (including sample-merchant). Generating empty dashboard.")
    else:
        print(f"Loaded {len(merchants)} merchant(s):")
        for m in merchants:
            status_emoji = {"RED": "🔴", "YELLOW": "🟡", "GREEN": "🟢"}.get(m["health"], "❓")
            ch = len(m["critical_high_risks"])
            print(f"  {status_emoji} {m['name']} — {m['milestones_pct']}% milestones, {ch} critical/high risks")
    print()

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    html_content = render_html(merchants, generated_at)

    # Write outputs
    for out_dir in (output_dir, preview_dir):
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"
        out_file.write_text(html_content, encoding="utf-8")
        print(f"  Written: {out_file}")

    print()
    print(f"Done. {len(merchants)} merchants, "
          f"{sum(len(m['critical_high_risks']) for m in merchants)} critical/high risks.")
    print(f"Preview: site/index.html")

    return 0


if __name__ == "__main__":
    sys.exit(main())
