"""Core reasoning engine for Narada.

This module contains the Planner class that generates structured plans
based on textual tasks. The implementation avoids external APIs and
relies on simple heuristics and open-source libraries.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Planner:
    """Create a plan based on a given task string."""

    max_steps: int = 5
    history: List[str] = field(default_factory=list)

    def create_plan(self, task: str) -> List[str]:
        """Generate a step-by-step plan to accomplish *task*.

        The method applies lightweight reasoning patterns:
        1. Breakdown the task into verbs and objects.
        2. Generate sequential steps for each identified action.
        3. Limit the output to *max_steps* for simplicity.
        """
        tokens = task.split()
        verbs = [tok for tok in tokens if tok.endswith("e")]
        objects = [tok for tok in tokens if tok not in verbs]

        self.history.append(task)
        steps = []
        for verb, obj in zip(verbs, objects):
            steps.append(f"{verb.capitalize()} {obj}")

        # If verbs are exhausted, transform remaining objects into review steps.
        while len(steps) < self.max_steps and objects:
            steps.append(f"Review {objects.pop(0)}")

        # Pad with generic evaluation steps to reach the desired length.
        while len(steps) < self.max_steps:
            steps.append("Evaluate progress")
        return steps[: self.max_steps]
