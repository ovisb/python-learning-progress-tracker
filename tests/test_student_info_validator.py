from python_learning_progress_tracker.student_input_validator import StudentValidator
import pytest


@pytest.mark.parametrize("first_name", [
    "J.", "Stanisław", "123", "1asd", "Oğuz", "1james", "James123", "n", "-name", "name-", "-name-"
])
def test_invalid_first_name(capsys, first_name):
    inp = (first_name, "placeholder_last", "placeholder_email")
    assert StudentValidator.validate_student_info(inp) is False
    captured = capsys.readouterr()
    assert captured.out.strip() == "Incorrect first name."


@pytest.mark.parametrize("last_name", [
    "J.", "Stanisław", "123", "1asd", "Oğuz", "1james", "James123", "n", "-name", "name-", "-name-"
])
def test_invalid_last_name(capsys, last_name):
    inp = ("John", last_name, "placeholder_email")
    assert StudentValidator.validate_student_info(inp) is False
    captured = capsys.readouterr()
    assert captured.out.strip() == "Incorrect last name."


@pytest.mark.parametrize("email", [
    "test", "-test", "testasdl", "123", "test@gmail"
])
def test_invalid_email(capsys, email):
    inp = ("John", "Don", email)
    assert StudentValidator.validate_student_info(inp) is False
    captured = capsys.readouterr()
    assert captured.out.strip() == "Incorrect email."


@pytest.mark.parametrize("valid_data", [
    (("John", "Don", "test@gmail.com"), True)
])
def test_valid(monkeypatch, capsys, valid_data):
    inp, expected = valid_data
    assert StudentValidator.validate_student_info(inp) is expected
