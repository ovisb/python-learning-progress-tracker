import pytest

from python_learning_progress_tracker.menu_choice_validator import MenuChoiceValidator


@pytest.mark.parametrize("choice, expected", [("back", True), ("test", False)])
def test_is_back(choice, expected):
    assert MenuChoiceValidator.is_back(choice) is expected


@pytest.mark.parametrize("choice, expected", [("exit", True), ("test", False)])
def test_is_exit(choice, expected):
    assert MenuChoiceValidator.is_exit(choice) is expected


@pytest.mark.parametrize("choice, expected", [("", True), (" ", True)])
def test_is_empty(choice, expected):
    assert MenuChoiceValidator.is_empty_input(choice) is expected
