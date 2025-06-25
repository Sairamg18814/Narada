from .reasoning import generate_with_reasoning

CODEX_SYSTEM_PROMPT = (
    "You are Codex, a helpful coding assistant. Provide concise answers and "
    "relevant code snippets."
)


def ask_codex(question: str, stream: bool = False, **kwargs) -> str:
    prompt = f"{CODEX_SYSTEM_PROMPT}\n\nQuestion:\n{question}\n\nAnswer:"
    return generate_with_reasoning(prompt, stream=stream, **kwargs)

