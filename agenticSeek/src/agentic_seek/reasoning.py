from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

from . import generate

LOG_FILE = Path(".cot.log")


def log_step(text: str) -> None:
    with LOG_FILE.open("a") as f:
        f.write(f"[{datetime.now().isoformat()}] {text}\n")


def generate_with_reasoning(prompt: str, stream: bool = False, **kwargs) -> str:
    """Call :func:`generate` while logging chain-of-thought steps."""
    log_step(f"PROMPT: {prompt}")
    output = generate(prompt, **kwargs)
    log_step(f"OUTPUT: {output}")
    if stream:
        print(output)
    return output

