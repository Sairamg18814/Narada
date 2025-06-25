"""Command-line interface for AgenticSeek."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from .llm_adapter import LLMAdapter
from .reasoning import Reasoner
from .codex_assistant import CodexAssistant


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agentic-seek", description="Offline agentic assistant")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan", help="Generate plan for a task")
    p_plan.add_argument("task")
    p_plan.add_argument("--notify", action="store_true")

    p_codex = sub.add_parser("codex", help="Ask Codex for code help")
    p_codex.add_argument("query")
    return parser


def run_cli() -> None:
    parser = build_parser()
    args = parser.parse_args()

    model_path = Path(os.getenv("AGENTIC_SEEK_MODEL", "models/llama.bin"))
    llm = LLMAdapter(model_path)

    if args.cmd == "plan":
        reasoner = Reasoner(llm)
        plan = reasoner.create_plan(args.task)
        print("\n".join(plan))
        if args.notify:
            try:  # pragma: no cover - requires macOS
                from pync import Notifier
                Notifier.notify("Planning complete", title="AgenticSeek")
            except Exception as exc:  # pragma: no cover
                print(f"Notification failed: {exc}")
    elif args.cmd == "codex":
        codex = CodexAssistant(llm)
        print(codex.ask(args.query))


if __name__ == "__main__":  # pragma: no cover
    run_cli()
