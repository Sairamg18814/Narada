import builtins

import pytest

from agentic_seek.cli import main, suggest_fix


def test_suggest_fix_makefile():
    fix = suggest_fix("Makefile:4: *** missing separator. Stop.")
    assert "TAB" in fix


def test_main_plan(monkeypatch, capsys):
    called = {}

    def fake_gen(prompt, stream=True):
        called['prompt'] = prompt
        if stream:
            print('out')
        return 'out'

    monkeypatch.setattr('agentic_seek.cli.generate_with_reasoning', fake_gen)
    main(['plan', 'hello'])
    assert called['prompt'] == 'hello'
    assert 'out' in capsys.readouterr().out


def test_main_codex(monkeypatch, capsys):
    def fake_codex(question, stream=True):
        if stream:
            print('code')
        return 'code'

    monkeypatch.setattr('agentic_seek.cli.ask_codex', fake_codex)
    main(['codex', 'how to?'])
    assert 'code' in capsys.readouterr().out

