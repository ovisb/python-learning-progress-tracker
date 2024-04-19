from io import StringIO

import pytest

from python_learning_progress_tracker.student import Student
from python_learning_progress_tracker.student_management import StudentManagement
from python_learning_progress_tracker.user_interface import UserInterface


@pytest.fixture
def ui_empty():
    return UserInterface(StudentManagement())


@pytest.fixture
def ui_with_student():
    student_manager = StudentManagement()
    student_manager.add_student(Student('John', 'Smith', 'js@gmail.com'))
    student_manager.add_points("1000", (5, 5, 5, 5))

    return UserInterface(student_manager)


def test_start_exit_message(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("exit\n"))
    ui_empty.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Bye!", "It should exit and respond with 'Bye!'."


def test_back_exit_message(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("back\nexit"))
    ui_empty.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Enter 'exit' to exit the program.\nBye!"


def test_start_empty_input_message(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("\nexit\n"))
    ui_empty.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == "No input.\nBye!"


def test_unknown_input_message(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("help\nexit\n"))
    ui_empty.start()
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
def test_add_single_student_success(ui_empty, monkeypatch, capsys, full_input):
    monkeypatch.setattr(
        "sys.stdin", StringIO(f"add students\n{full_input}\nback\nexit\n")
    )
    ui_empty.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() ==
            "Enter student credentials or 'back' to return: \n"
            "The student has been added.\nTotal 1 students have been added.\nBye!"
    )


def test_ui_fail_add_student_non_unique_email(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(
        "add students\nJean-Clause van Helsing jc@google.it\nJohn Carl jc@google.it\nback\nexit\n")
                        )
    ui_empty.start()
    captured = capsys.readouterr()
    assert (
        captured.out.strip() ==
        "Enter student credentials or 'back' to return: \n",
        "The student has been added.\n",
        "This email is already taken.\n",
        "Bye!"
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
def test_add_multiple_student_success(ui_empty, monkeypatch, capsys, full_input):
    inputs = "\n".join(full_input)
    added_success = "\n".join(["The student has been added." for _ in full_input])
    monkeypatch.setattr("sys.stdin", StringIO(f"add students\n{inputs}\nback\nexit\n"))
    ui_empty.start()
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
def test_invalid_input(ui_empty, monkeypatch, capsys, invalid_input, expected):
    monkeypatch.setattr("sys.stdin", StringIO(f"add students\n{invalid_input}\nback\nexit\n"))
    ui_empty.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip()
            == f"Enter student credentials or 'back' to return: \n"
               f"{expected}\n"
               f"Total 0 students have been added.\n"
               f"Bye!"
    )


@pytest.mark.parametrize("bad_info", ["1", "james dean", "banana"])
def test_fail_add_student_wrong_info(ui_empty, monkeypatch, capsys, bad_info):
    monkeypatch.setattr(
        "sys.stdin", StringIO(f"add students\n{bad_info}\nback\nexit\n")
    )
    ui_empty.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip()
            == "Enter student credentials or 'back' to return: \n"
               "Incorrect credentials.\n"
               "Total 0 students have been added.\n"
               "Bye!"
    )


def test_ui_list_no_students(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(f"list\nexit"))
    ui_empty.start()
    captured = capsys.readouterr()
    assert captured.out.strip() == f"No students found\nBye!"


def test_ui_list_single_student_id(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(f"add students\nJames Dean jd@google.it\nback\nlist\nexit"))
    ui_empty.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() ==
            "Enter student credentials or 'back' to return: \n"
            "The student has been added.\n"
            "Total 1 students have been added.\n"
            "Students: \n"
            "1000\n"
            "Bye!"
    ), "Should add and list one student ID."


def test_ui_list_multiple_student_ids(ui_empty, monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO(
        f"add students\nJames Dean jd@google.it\nJohn Doe john.doe@google.it\nback\nlist\nexit"))
    ui_empty.start()
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
    ), "Expected total of 2 students IDs to be printed with exit message."


def test_ui_not_found_student_id(ui_empty, monkeypatch, capsys):
    input_commands = f"find\n1000\n1001\nback\nexit\n"
    monkeypatch.setattr("sys.stdin", StringIO(input_commands))
    ui_empty.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() ==
            "Enter an id or 'back' to return: \n"
            "No student is found for id=1000.\n"
            "No student is found for id=1001.\n"
            "Bye!"
    ), "Expected no student IDs to be found."


def test_ui_found_student_id(ui_with_student, monkeypatch, capsys):
    input_commands = f"find\ntest\n-100\n1000\nback\nexit\n"
    monkeypatch.setattr("sys.stdin", StringIO(input_commands))
    ui_with_student.start()
    captured = capsys.readouterr()
    assert (
        captured.out.strip() ==
        "Enter an id or 'back' to return: \n"
        "Please input a non-negative number as the ID.\n",
        "Please input a non-negative number as the ID.\n",
        "1000 points: Python=5; DSA=5; Databases=5; Flask=5\n"
        "Bye!"
    ), "Expected student ID printed with course progress results."


def test_ui_add_points(ui_with_student, monkeypatch, capsys):
    input_commands = f"add points\ntesting 5 5 5 5\n10001 5 5 5 5\n1000 4 3 2\n1000 5 5 5 5\nback\nexit\n"
    monkeypatch.setattr("sys.stdin", StringIO(input_commands))
    ui_with_student.start()
    captured = capsys.readouterr()
    assert (
            captured.out.strip() ==
            "Enter an id and points or 'back' to return: \n"
            "No student is found for id=testing.\n"
            "No student is found for id=10001.\n"
            "Incorrect points format.\n"
            "Points updated.\n"
            "Bye!"
    )
