import os
import platform
from . import generate


def is_apple_m_chip() -> bool:
    """Return True if running on Apple Silicon."""
    return platform.system() == "Darwin" and platform.machine().startswith("arm")


class LLMAdapter:
    """Adapter that loads a local LLM optimized for Apple Silicon."""

    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = model_path or os.environ.get("AGENTIC_SEEK_MODEL", "model.bin")
        self.loaded = False

    def load(self) -> None:
        if not is_apple_m_chip():
            raise RuntimeError("LLMAdapter requires Apple Silicon (M-chip)")
        # Loading of the quantized model would happen here, using accelerate/metal
        self.loaded = True

    def generate(self, prompt: str, **kwargs) -> str:
        if not self.loaded:
            self.load()
        return generate(prompt, **kwargs)

