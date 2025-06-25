#!/usr/bin/env bash
set -e
MODEL_DIR="$(dirname "$0")/../models"
mkdir -p "$MODEL_DIR"
cat <<MSG
Place your quantized Llama model file at $MODEL_DIR/llama.bin
or set AGENTIC_SEEK_MODEL to a custom path.
MSG
