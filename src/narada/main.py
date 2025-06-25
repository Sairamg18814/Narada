"""Command-line interface for Narada."""

import argparse
from pathlib import Path

from .reasoning import Planner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Narada local reasoning assistant")
    parser.add_argument("task", help="Task to analyze and plan")
    parser.add_argument("--notify", action="store_true", help="Send macOS notification")
    return parser.parse_args()


def run_cli() -> None:
    args = parse_args()
    planner = Planner()
    plan = planner.create_plan(args.task)
    print("\nPlan:\n" + "\n".join(f"- {step}" for step in plan))
    if args.notify:
        try:
            from pync import Notifier
            Notifier.notify("Narada finished planning", title="Narada")
        except Exception as exc:  # pragma: no cover - macOS specific
            print(f"Notification failed: {exc}")


if __name__ == "__main__":  # pragma: no cover
    run_cli()
