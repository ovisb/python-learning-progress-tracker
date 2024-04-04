from io import StringIO

import pytest

from python_learning_progress_tracker.student_management import StudentManagement
from python_learning_progress_tracker.user_interface import UserInterface


@pytest.fixture
def ui():
    return UserInterface(StudentManagement())


def test_start_exit_message(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("exit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Bye!"


def test_back_exit_message(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("back\nexit"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter 'exit' to exit the program.\nBye!"


def test_start_empty_input_message(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "No input.\nBye!"


def test_unknown_input_message(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("help\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Error: unknown command!\nBye!"


@pytest.mark.parametrize(
    "full_input",
    [
        "Jean-Clause van Helsing jc@google.it",
        "James Dean james.dean@gmail.com",
        "Andrew Tim Johnson maryj@google.com",
    ],
)
def test_add_single_student_success(ui, monkeypatch, capsys, full_input):
    monkeypatch.setattr(
        "sys.stdin", StringIO(f"add students\n{full_input}\nback\nexit\n")
    )
    ui.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() == "Enter student credentials or 'back' to return: \n"
                                    "The student has been added.\nTotal 1 students have been added.\nBye!"
    )


@pytest.mark.parametrize(
    "full_input",
    [
        (
                "Jean-Clause van Helsing jc@google.it",
                "James Dean james.dean@gmail.com",
                "Andrew Tim Johnson maryj@google.com",
                "Tom Cruise tom.cruise@gmail.com",
                "Robert Jemison Van de Graaff robertvdgraaff@mit.edu",
                "O'Neill Bool onneilbool@mit.edu",
        )
    ],
)
def test_add_multiple_student_success(ui, monkeypatch, capsys, full_input):
    inputs = "\n".join(full_input)
    added_success = "\n".join(["The student has been added." for _ in full_input])
    monkeypatch.setattr("sys.stdin", StringIO(f"add students\n{inputs}\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip()
            == f"Enter student credentials or 'back' to return: \n{added_success}\n"
               f"Total {len(full_input)} students have been added.\nBye!"
    )


@pytest.mark.parametrize(
    "invalid_input, expected",
    [
        ("-John Doe test@gmail.com", "Incorrect first name."),
        ("John -Doe test@gmail.com", "Incorrect last name."),
        ("John Doe test@gmail", "Incorrect email."),
    ],
)
def test_invalid_input(ui, monkeypatch, capsys, invalid_input, expected):
    monkeypatch.setattr("sys.stdin", StringIO(f"add students\n{invalid_input}\nback\nexit\n"))
    ui.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip()
            == f"Enter student credentials or 'back' to return: \n"
               f"{expected}\n"
               f"Total 0 students have been added.\n"
               f"Bye!"
    )


@pytest.mark.parametrize("bad_info", ["1", "james dean", "banana"])
def test_fail_add_student_wrong_info(ui, monkeypatch, capsys, bad_info):
    monkeypatch.setattr(
        "sys.stdin", StringIO(f"add students\n{bad_info}\nback\nexit\n")
    )
    ui.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip()
            == "Enter student credentials or 'back' to return: \n"
               "Incorrect credentials.\n"
               "Total 0 students have been added.\n"
               "Bye!"
    )


def test_ui_list_no_students(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(f"list\nexit"))
    ui.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"No students found\nBye!"


def test_ui_list_single_student_id(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(f"add students\nJames Dean jd@google.it\nback\nlist\nexit"))
    ui.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() ==
            "Enter student credentials or 'back' to return: \n"
            "The student has been added.\n"
            "Total 1 students have been added.\n"
            "Students: \n"
            "1000\n"
            "Bye!"
    )


def test_ui_list_multiple_student_ids(ui, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(
        f"add students\nJames Dean jd@google.it\nJohn Doe john.doe@google.it\nback\nlist\nexit"))
    ui.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() ==
            "Enter student credentials or 'back' to return: \n"
            "The student has been added.\n"
            "The student has been added.\n"
            "Total 2 students have been added.\n"
            "Students: \n"
            "1000\n"
            "1001\n"
            "Bye!"
    )
