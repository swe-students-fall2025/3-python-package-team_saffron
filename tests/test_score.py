import pytest
from emojiguessr.score import score


def test_score_correct_answer():
    """
    When you get an answer right, your score should increase by the point value.
    Default behavior treats answers as correct and adds 1 point.
    """
    # Default behavior adds 1 point for correct answers
    assert score(0, correct=True) == 1, "Correct answer should add 1 point by default"
    assert score(5, correct=True) == 6, "Should add points to existing score"
    
    # Custom point values work too
    assert score(0, correct=True, points=5) == 5, "Should add custom point value"
    assert score(10, correct=True, points=3) == 13, "Custom points should work with existing score"


def test_score_wrong_answer():
    """
    When you get an answer wrong, your score stays the same regardless of point values.
    """
    # Wrong answers don't change the score
    assert score(0, correct=False) == 0, "Wrong answer shouldn't change score"
    assert score(10, correct=False) == 10, "Wrong answer keeps existing score"
    
    # Custom points don't matter when answer is wrong
    assert score(5, correct=False, points=10) == 5, "Wrong answer ignores point value"


def test_score_default_behavior():
    """
    The function has default parameters - correct=True and points=1. When you don't
    specify these, it should still work correctly and add 1 point by default.
    """
    # Default behavior should treat as correct and add 1 point
    assert score(0) == 1, "Default should add 1 point (correct=True, points=1)"
    assert score(5) == 6, "Default should work with any starting score"
    
    # Can specify just one parameter
    assert score(0, points=3) == 3, "Should use default correct=True with custom points"
    assert score(10, correct=False) == 10, "Should use default points=1 but ignore it when wrong"

