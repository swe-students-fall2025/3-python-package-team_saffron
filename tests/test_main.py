import pytest
from emojiguessr.__main__ import run_quiz, list_themes, list_commands

class Tests:
  
  @pytest.fixture
  def fake_input_single():
    def _input(_):
      return "burger"
    return _input

  @pytest.fixture
  def fake_input_multiple():
    inputs = iter(["burger", "sushi"])
    def _input(_):
      return next(inputs)
    return _input

  @pytest.fixture
  def fake_output():
    outputs = []
    def output_fn(text):
      outputs.append(text)
    return outputs, output_fn

def test_run_quiz_correct_answer(fake_input_single, fake_output):
    outputs, output_fn = fake_output
    run_quiz(1, "food", False, True, 1, input_fn=fake_input_single, output_fn=output_fn)
    assert any("✅ Correct!" in msg for msg in outputs)
    assert any("Final score: 1/1" in msg for msg in outputs)


def test_run_quiz_wrong_answer(fake_output):
    outputs, output_fn = fake_output
    def always_wrong(_):
        return "pizza"
    run_quiz(1, "food", False, True, 1, input_fn=always_wrong, output_fn=output_fn)
    assert any("❌ Nope" in msg for msg in outputs)
    assert any("Final score: 0/1" in msg for msg in outputs)


def test_run_quiz_multiple_attempts(fake_input_multiple, fake_output):
    outputs, output_fn = fake_output
    run_quiz(1, "food", False, True, 2, input_fn=fake_input_multiple, output_fn=output_fn)
    assert any("❌ Wrong!" in msg for msg in outputs)
    assert any("✅ Correct!" in msg for msg in outputs)
    assert any("Final score: 1/1" in msg for msg in outputs)
  
  
    
