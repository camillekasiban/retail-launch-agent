#!/usr/bin/env bash
# Retail Launch Agent — Publisher
# Generates the site and pushes docs/ to your private GitHub Pages repo.
#
# SETUP (one-time):
#   1. Create a private GitHub repo for your real merchant data
#   2. Set PRIVATE_REPO_URL below to that repo's SSH URL
#   3. Enable GitHub Pages on that repo (Settings → Pages → Branch: gh-pages)
#   4. Run this script once — it will push the site to the gh-pages branch
#
# USAGE:
#   bash scripts/publish.sh              # generate + publish
#   bash scripts/publish.sh --skip-generate  # publish only (use existing docs/)

set -e

# =============================================================
# CONFIGURE BEFORE FIRST USE
# =============================================================
PRIVATE_REPO_URL=""    # e.g., git@github.com:yourname/your-private-repo.git
PRIVATE_REPO_BRANCH="gh-pages"
# =============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DOCS_DIR="$ROOT_DIR/docs"
WORKTREE_DIR="/tmp/retail-launch-publish-$$"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log()  { echo -e "${GREEN}[publish]${NC} $*"; }
warn() { echo -e "${YELLOW}[publish]${NC} $*"; }
fail() { echo -e "${RED}[publish] ERROR:${NC} $*"; exit 1; }

# Check configuration
if [ -z "$PRIVATE_REPO_URL" ]; then
  fail "PRIVATE_REPO_URL is not set in scripts/publish.sh.

  Setup steps:
  1. Create a private GitHub repo for your merchant data
  2. Open scripts/publish.sh and set PRIVATE_REPO_URL to your repo's SSH URL
     Example: git@github.com:yourname/your-private-repo.git
  3. Enable GitHub Pages on that repo (Settings → Pages → Source: gh-pages branch)
  4. Re-run: bash scripts/publish.sh"
fi

# Parse args
SKIP_GENERATE=false
for arg in "$@"; do
  case $arg in
    --skip-generate) SKIP_GENERATE=true ;;
    --help|-h)
      echo "Usage: bash scripts/publish.sh [--skip-generate]"
      echo "  --skip-generate    Skip site regeneration, publish existing docs/"
      exit 0
      ;;
  esac
done

# Step 1: Generate site
if [ "$SKIP_GENERATE" = false ]; then
  log "Generating site..."
  cd "$ROOT_DIR"
  python3 scripts/generate-site.py || fail "Site generation failed. Check Python output above."
  log "Site generated."
fi

# Step 2: Verify docs/index.html exists
if [ ! -f "$DOCS_DIR/index.html" ]; then
  fail "docs/index.html not found. Run without --skip-generate to regenerate."
fi

log "Publishing to $PRIVATE_REPO_URL ($PRIVATE_REPO_BRANCH branch)..."

# Step 3: Push docs/ to gh-pages branch using a temporary clone
rm -rf "$WORKTREE_DIR"
mkdir -p "$WORKTREE_DIR"

# Clone just the target branch (shallow, for speed)
if git ls-remote --heads "$PRIVATE_REPO_URL" "$PRIVATE_REPO_BRANCH" | grep -q "$PRIVATE_REPO_BRANCH"; then
  git clone --depth=1 --branch "$PRIVATE_REPO_BRANCH" "$PRIVATE_REPO_URL" "$WORKTREE_DIR" 2>/dev/null || \
    git clone --depth=1 "$PRIVATE_REPO_URL" "$WORKTREE_DIR"
else
  # Branch doesn't exist yet — clone default branch and create gh-pages
  git clone --depth=1 "$PRIVATE_REPO_URL" "$WORKTREE_DIR"
  cd "$WORKTREE_DIR"
  git checkout --orphan "$PRIVATE_REPO_BRANCH"
  git rm -rf . --quiet 2>/dev/null || true
fi

# Copy docs/ content into the worktree
cd "$WORKTREE_DIR"
# Remove existing HTML files (keep .git)
find . -maxdepth 1 -type f -not -name '.git' -delete 2>/dev/null || true
# Copy new site
cp -r "$DOCS_DIR"/. .

# Commit and push
COMMIT_MSG="Site update: $(date '+%Y-%m-%d %H:%M')"
git add -A
if git diff --cached --quiet; then
  warn "No changes to publish — site is already up to date."
else
  git config user.email "retail-launch-agent@local" 2>/dev/null || true
  git config user.name "Retail Launch Agent" 2>/dev/null || true
  git commit -m "$COMMIT_MSG"
  git push origin "$PRIVATE_REPO_BRANCH"
  log "Published successfully."
fi

# Cleanup
cd "$ROOT_DIR"
rm -rf "$WORKTREE_DIR"

# Print URL hint
REPO_PATH=$(echo "$PRIVATE_REPO_URL" | sed 's/.*github\.com[:/]//' | sed 's/\.git$//')
if [ -n "$REPO_PATH" ]; then
  OWNER=$(echo "$REPO_PATH" | cut -d/ -f1)
  REPO=$(echo "$REPO_PATH" | cut -d/ -f2)
  log "GitHub Pages URL: https://${OWNER}.github.io/${REPO}/"
fi

log "Done."
