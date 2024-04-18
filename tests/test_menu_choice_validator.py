import pytest

from python_learning_progress_tracker.menu_choice_validator import MenuChoiceValidator


@pytest.mark.parametrize("choice, expected", [("back", True), ("test", False)])
def test_is_back(choice, expected):
    assert MenuChoiceValidator.is_back(choice) is expected, f"Expected choice to be {expected}."


@pytest.mark.parametrize("choice, expected", [("exit", True), ("test", False)])
def test_is_exit(choice, expected):
    assert MenuChoiceValidator.is_exit(choice) is expected, f"Expected choice to be {expected}."


@pytest.mark.parametrize("choice, expected", [("", True), (" ", True)])
def test_is_empty(choice, expected):
    assert MenuChoiceValidator.is_empty_input(choice) is expected, f"Expected choice to be {expected}."


@pytest.mark.parametrize("choice, expected", [("list", True), ("exit", False)])
def test_list_students(choice, expected):
    assert MenuChoiceValidator.is_list_students(choice) is expected, f"Expected choice to be {expected}."


@pytest.mark.parametrize("choice, expected", [("find", True), (" ", False)])
def test_find_students(choice, expected):
    assert MenuChoiceValidator.is_find_student(choice) is expected, f"Expected choice to be {expected}."


@pytest.mark.parametrize("choice, expected", [("add points", True), (" ", False)])
def test_add_points(choice, expected):
    assert MenuChoiceValidator.is_add_points(choice) is expected, f"Expected choice to be {expected}."
