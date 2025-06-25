from agentic_seek.codex_assistant import ask_codex, CODEX_SYSTEM_PROMPT


def test_ask_codex(monkeypatch):
    captured = {}

    def fake_generate(prompt, stream=False, **kwargs):
        captured['prompt'] = prompt
        return 'code'

    monkeypatch.setattr('agentic_seek.codex_assistant.generate_with_reasoning', fake_generate)
    out = ask_codex('How?', stream=False)
    assert CODEX_SYSTEM_PROMPT in captured['prompt']
    assert 'How?' in captured['prompt']
    assert out == 'code'

