#!/usr/bin/env bash

set -euo pipefail

if command -v brew >/dev/null; then
    brew bundle --file="$(dirname "$0")/../Brewfile"
else
    echo "Homebrew not found. Please install Homebrew first." >&2
    exit 1
fi

python3 -m pip install -U pip
python3 -m pip install -e "$(dirname "$0")/.."
