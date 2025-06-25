import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from agentic_seek.reasoning import Reasoner
from agentic_seek.codex_assistant import CodexAssistant
from agentic_seek.llm_adapter import LLMAdapter


class DummyLLM(LLMAdapter):
    def __init__(self):
        pass

    def generate(self, prompt: str, max_tokens: int = 128, stream: bool = False, callback=None) -> str:
        if "Break down" in prompt:
            return "1. Step one\n2. Step two\n3. Step three"
        return "print('hello world')"


def test_reasoner_plan():
    llm = DummyLLM()
    reasoner = Reasoner(llm, max_steps=3)
    plan = reasoner.create_plan("do something")
    assert len(plan) == 3
    assert plan[0].startswith("1.")
    assert reasoner.history


def test_codex_assistant():
    llm = DummyLLM()
    codex = CodexAssistant(llm)
    answer = codex.ask("hello")
    assert "print" in answer
    assert codex.log


def test_adapter_mock_output():
    adapter = LLMAdapter(model_path="/nonexistent.bin")
    text = adapter.generate("test prompt")
    assert "Mock" in text
