"""Local LLM adapter optimized for Apple Silicon."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Callable, Optional, List

try:
    from llama_cpp import Llama
except Exception:  # pragma: no cover - optional dependency
    Llama = None


class LLMAdapter:
    """Wrapper around ``llama_cpp.Llama`` with graceful fallback."""

    def __init__(self, model_path: str | Path) -> None:
        self.model_path = Path(model_path)
        self.model = None
        if Llama is not None and self.model_path.exists():  # pragma: no cover - requires real model
            self.model = Llama(
                model_path=str(self.model_path),
                n_threads=os.cpu_count(),
                n_ctx=2048,
                n_gpu_layers=1 if self._use_gpu() else 0,
            )

    @staticmethod
    def _use_gpu() -> bool:
        """Return True if running on Apple Silicon."""
        return os.uname().machine == "arm64"

    def generate(
        self,
        prompt: str,
        max_tokens: int = 128,
        stream: bool = False,
        callback: Optional[Callable[[str], None]] = None,
    ) -> str:
        """Generate text for *prompt* using the local model.

        When no model is loaded a mock response is returned for testing.
        """
        if self.model is None:
            text = f"Mock: {prompt}"
            if callback:
                callback(text)
            return text

        if stream:  # pragma: no cover - requires real model
            tokens: List[str] = []
            for chunk in self.model(prompt, max_tokens=max_tokens, stream=True):
                token = chunk["choices"][0]["text"]
                if callback:
                    callback(token)
                tokens.append(token)
            return "".join(tokens)

        res = self.model(prompt, max_tokens=max_tokens)  # pragma: no cover - requires real model
        text = res["choices"][0]["text"]
        if callback:
            callback(text)
        return text
