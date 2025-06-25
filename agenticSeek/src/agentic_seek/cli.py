from __future__ import annotations

import argparse
from typing import Optional

from .codex_assistant import ask_codex
from .llm_adapter import LLMAdapter
from .reasoning import generate_with_reasoning


def suggest_fix(error_message: str) -> Optional[str]:
    if "missing separator" in error_message:
        return "Makefile commands need to start with a TAB character."
    if "command not found" in error_message and "agentic-seek" in error_message:
        return "Run `pip install .` and ensure your PATH includes the Python scripts directory."
    return None


def main(argv: list[str] | None = None) -> str:
    parser = argparse.ArgumentParser(prog="agentic-seek")
    sub = parser.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="Generate a plan from a prompt")
    p_plan.add_argument("prompt")

    p_codex = sub.add_parser("codex", help="Ask coding questions")
    p_codex.add_argument("question")

    args = parser.parse_args(argv)

    adapter = LLMAdapter()
    try:
        if args.command == "plan":
            return generate_with_reasoning(args.prompt, stream=True)
        if args.command == "codex":
            return ask_codex(args.question, stream=True)
    except Exception as exc:  # pragma: no cover - truly unexpected
        msg = str(exc)
        fix = suggest_fix(msg)
        if fix:
            print(f"Suggestion: {fix}")
        raise
    return ""


if __name__ == "__main__":  # pragma: no cover
    main()

