"""Interactive coding assistant powered by the local LLM."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .llm_adapter import LLMAdapter


@dataclass
class CodexAssistant:
    """Provide on-the-fly code snippets and refactoring advice."""

    llm: LLMAdapter
    log: List[str] = field(default_factory=list)

    def ask(self, query: str) -> str:
        """Return a code suggestion for *query*."""
        prompt = (
            "You are Codex, a helpful coding assistant. Respond with code when"
            " possible.\nQuery: "
            f"{query}\n"
        )
        answer = self.llm.generate(prompt, max_tokens=200)
        self.log.append(f"Q:{query}\nA:{answer}")
        return answer.strip()
