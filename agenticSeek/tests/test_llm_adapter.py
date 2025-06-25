from agentic_seek.llm_adapter import LLMAdapter, is_apple_m_chip


def test_is_apple_m_chip_type():
    assert isinstance(is_apple_m_chip(), bool)


def test_llm_adapter_generate(monkeypatch):
    adapter = LLMAdapter()
    monkeypatch.setattr(adapter, 'load', lambda: None)

    def fake_generate(prompt, **kwargs):
        return 'response'

    monkeypatch.setattr('agentic_seek.llm_adapter.generate', fake_generate)
    out = adapter.generate('test')
    assert out == 'response'

