from io import StringIO
import pytest

from python_learning_progress_tracker.user_interface import UserInterface


@pytest.fixture
def ui():
    return UserInterface()


def test_start_exit_message(ui, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('exit\n'))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Bye!"


def test_back_exit_message(ui, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('back\nexit'))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter 'exit' to exit the program.\nBye!"


def test_start_empty_input_message(ui, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('\nexit\n'))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "No input.\nBye!"


def test_unknown_input_message(ui, monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('help\nexit\n'))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Error: unknown command!\nBye!"


@pytest.mark.parametrize("full_input", [
    "Jean-Clause van Helsing jc@google.it",
    "James Dean james.dean@gmail.com",
    "Andrew Tim Johnson maryj@google.com"
])
def test_add_single_student_success(ui, monkeypatch, capsys, full_input):
    monkeypatch.setattr('sys.stdin', StringIO(f"add students\n{full_input}\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter student credentials or 'back' to return: \nThe student has been added.\nTotal 1 students have been added.\nBye!"


@pytest.mark.parametrize("full_input", [
    (
            "Jean-Clause van Helsing jc@google.it",
            "James Dean james.dean@gmail.com",
            "Andrew Tim Johnson maryj@google.com",
            "Tom Cruise tom.cruise@gmail.com",
    )
])
def test_add_multiple_student_success(ui, monkeypatch, capsys, full_input):
    inputs = "\n".join(full_input)
    added_success = "\n".join(["The student has been added." for _ in full_input])
    monkeypatch.setattr('sys.stdin', StringIO(f"add students\n{inputs}\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Enter student credentials or 'back' to return: \n{added_success}\nTotal {len(full_input)} students have been added.\nBye!"


@pytest.mark.parametrize("first_name", [
    "J.", "Stanisław", "123", "1asd", "Oğuz", "1james", "James123"
])
def test_fail_add_student_first_name(ui, monkeypatch, capsys, first_name):
    monkeypatch.setattr('sys.stdin', StringIO(f"add students\n{first_name} Dean james.dean@gmail.com\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter student credentials or 'back' to return: \nIncorrect first name.\nTotal 0 students have been added.\nBye!"


@pytest.mark.parametrize("last_name", [
    "J.", "123", "1asd", "Oğuz", "1james", "James123"
])
def test_fail_add_student_last_name(ui, monkeypatch, capsys, last_name):
    monkeypatch.setattr('sys.stdin', StringIO(f"add students\nJames {last_name} james.dean@gmail.com\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter student credentials or 'back' to return: \nIncorrect last name.\nTotal 0 students have been added.\nBye!"


@pytest.mark.parametrize("student_email", [
    "test", "testasdl", "123", "test@gmail"
])
def test_fail_add_student_email(ui, monkeypatch, capsys, student_email):
    monkeypatch.setattr('sys.stdin', StringIO(f"add students\nJames Dean {student_email}\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter student credentials or 'back' to return: \nIncorrect email.\nTotal 0 students have been added.\nBye!"


@pytest.mark.parametrize("bad_info", [
    "1", "james dean", "banana", "James Dean james@gmail.com test abc"
])
def test_fail_add_student_wrong_info(ui, monkeypatch, capsys, bad_info):
    monkeypatch.setattr('sys.stdin', StringIO(f"add students\n{bad_info}\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter student credentials or 'back' to return: \nIncorrect credentials.\nTotal 0 students have been added.\nBye!"
