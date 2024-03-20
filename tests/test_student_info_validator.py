import pytest

from python_learning_progress_tracker.student_input_validator import StudentValidator


@pytest.mark.parametrize(
    "first_name",
    [
        "J.",
        "Stanisław",
        "123",
        "1asd",
        "Oğuz",
        "1james",
        "James123",
        "n",
        "-name",
        "name-",
        "-name-",
    ],
)
def test_invalid_first_name(capsys, first_name):
    inp = (first_name, "placeholder_last", "placeholder_email")
    with pytest.raises(ValueError):
        StudentValidator.validate_student_info(inp)


@pytest.mark.parametrize(
    "last_name",
    [
        "J.",
        "Stanisław",
        "123",
        "1asd",
        "Oğuz",
        "1james",
        "James123",
        "n",
        "-name",
        "name-",
        "-name-",
    ],
)
def test_invalid_last_name(capsys, last_name):
    inp = ("John", last_name, "placeholder_email")
    with pytest.raises(ValueError):
        StudentValidator.validate_student_info(inp)


@pytest.mark.parametrize("email", ["test", "-test", "testasdl", "123", "test@gmail"])
def test_invalid_email(capsys, email):
    inp = ("John", "Don", email)
    with pytest.raises(ValueError):
        StudentValidator.validate_student_info(inp)


@pytest.mark.parametrize("valid_data, expected", [(("John", "Don", "test@gmail.com"), None)])
def test_valid(monkeypatch, capsys, valid_data, expected):
    assert StudentValidator.validate_student_info(valid_data) is expected


@pytest.mark.parametrize("invalid_input", ["John", "a b", "1 John"]
                         )
def test_too_less_input(invalid_input):
    data = invalid_input.split()
    with pytest.raises(ValueError):
        StudentValidator.validate_number_of_inputs(data)
