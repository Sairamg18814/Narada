"""Reasoning module with chain-of-thought logging."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .llm_adapter import LLMAdapter


@dataclass
class Reasoner:
    """Generate step-by-step plans using a local LLM."""

    llm: LLMAdapter
    max_steps: int = 5
    history: List[str] = field(default_factory=list)

    def create_plan(self, task: str) -> List[str]:
        """Return a list of steps to accomplish *task*."""
        self.history.append(f"Task: {task}")
        prompt = (
            f"Break down the following task into {self.max_steps} concise steps:\n"
            f"{task}\nSteps:"\
        )
        response = self.llm.generate(prompt, max_tokens=200)
        self.history.append(f"Model: {response}")
        steps = [line.strip() for line in response.splitlines() if line.strip()]
        if not steps:
            words = task.split()
            steps = [f"Consider {w}" for w in words[: self.max_steps]]
        return steps[: self.max_steps]
