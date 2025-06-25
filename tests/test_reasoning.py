from narada.reasoning import Planner


def test_create_plan_basic():
    planner = Planner(max_steps=3)
    plan = planner.create_plan("write code unit")
    assert len(plan) == 3
    assert any(step.startswith("Write") for step in plan)
