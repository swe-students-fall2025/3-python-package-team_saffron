import pytest
from emojiguessr.__main__ import run_quiz, list_themes, list_commands
from emojiguessr.data import _EMOJI_BANK

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
  def fake_input_partial():
    def _input(_):
      return "Jurassic"
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
    assert any("✅ Correct!" in text for text in outputs)
    assert any("Final score: 1/1" in text for text in outputs)


  def test_run_quiz_wrong_answer(fake_output):
    outputs, output_fn = fake_output
    def always_wrong(_):
        return "pizza"
    run_quiz(1, "food", False, True, 1, input_fn=always_wrong, output_fn=output_fn)
    assert any("❌ Nope" in text for text in outputs)
    assert any("Final score: 0/1" in text for text in outputs)


  def test_run_quiz_multiple_attempts(fake_input_multiple, fake_output):
    outputs, output_fn = fake_output
    run_quiz(1, "food", False, True, 2, input_fn=fake_input_multiple, output_fn=output_fn)
    assert any("❌ Wrong!" in text for text in outputs)
    assert any("✅ Correct!" in text for text in outputs)
    assert any("Final score: 1/1" in text for text in outputs)

  def test_run_quiz_multiple_questions(fake_input_multiple, fake_output):
    outputs, output_fn = fake_output
    run_quiz(2, "food", False, True, 1, input_fn=fake_input_multiple, output_fn=output_fn)
    assert any("Question 1/2" in text for text in outputs)
    assert any("Question 2/2" in text for text in outputs)
    correct_amount = [text for text in outputs if "✅ Correct!" in text]
    assert len(correct_amount) == 2
    assert any("Final score: 2/2" in text for text in outputs)

  def test_run_quiz_partial_answer(fake_input_partial, fake_output):
    outputs, output_fn = fake_output
    run_quiz(1, "movies", False, True, 1, input_fn=fake_input_partial, output_fn=output_fn)
    assert any("✅ Correct!" in text for text in outputs)
    assert any("Final score: 1/1" in text for text in outputs)

  def test_run_quiz_no_partial(fake_input_partial, fake_output):
    outputs, output_fn = fake_output
    run_quiz(num_questions=1, theme="movies", case_sensitive=False, allow_partial=False, max_attempts=1, input_fn=fake_input_partial, 
             output_fn=output_fn)
    assert any("❌ Nope" in text for text in outputs)
    assert any("Final score: 0/1" in text for text in outputs)

  def test_list_themes_not_empty(fake_output):
    outputs, output_fn = fake_output
    list_themes(output_fn=output_fn)
    assert output[0] == "Available themes"
    assert len(outputs) >= 1

  def test_list_themes_contains_all_themes(fake_output):
    outputs, output_fn = fake_output
    list_themes(output_fn=output_fn)
    for theme in _EMOJI_BANK.keys():
        assert any(theme in text for text in outputs)

  def test_list_themes_sorted(fake_output):
    outputs, output_fn = fake_output
    list_themes(output_fn=output_fn)
    theme_lines = outputs[1:]
    themes = [line.strip()[2:] if line.startswith("  - ") else line.strip() for line in theme_lines]
    assert themes == sorted(themes)

  def test_list_commands_non_empty(fake_output):
    outputs, output_fn = fake_output
    list_commands(output_fn=output_fn)
    assert outputs[0] == "Available commands:"
    assert len(outputs) > 1

  def test_list_commands_contains_known_command(fake_output):
    outputs, output_fn = fake_output
    list_commands(output_fn=output_fn)
    assert any("--num-questions" in text for text in outputs)
    assert any("--theme" in text for text in outputs)

  def test_list_commands_order(fake_output):
    outputs, output_fn = fake_output
    list_commands(output_fn=output_fn)
    command_lines = outputs[1:]
    commands = [line.strip().split()[0] for line in command_lines]
    expected_commands = ["--num-questions", "--theme", "--case-sensitive", "--no-partial", "--max-attempts", "--list-themes", "--list-commands"]
    assert commands[:len(expected_commands)] == expected_commands


  
  
  
  
    
