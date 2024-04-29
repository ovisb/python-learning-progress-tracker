import pytest
from python_learning_progress_tracker.notify import Notify
from python_learning_progress_tracker.student_management import StudentManagement
from python_learning_progress_tracker.student import Student


@pytest.fixture
def student_management():
    return StudentManagement()


@pytest.fixture
def empty_notify(student_management):
    return Notify(student_management)


@pytest.fixture
def one_student_notify(student_management):
    student = Student("John", "Doe", "johnd@google.it")
    points = 600, 0, 0, 0
    student_management.add_student(student)
    student_management.add_points("1000", points)
    return Notify(student_management)


def test_no_students_notify(empty_notify):
    assert bool(empty_notify.notify()) is False, "Expected notify email list to be empty."


def test_one_student_to_notify(one_student_notify):
    assert len(one_student_notify.notify()) == 1, "Expected notify email list to be empty."


def test_ensure_notify_list_is_cleared(one_student_notify):
    one_student_notify.notify()
    assert bool(one_student_notify.to_notify) is False, "Expected notify email list to be empty."
