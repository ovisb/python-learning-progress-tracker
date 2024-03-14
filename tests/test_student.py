import pytest

from python_learning_progress_tracker.student import Student


@pytest.fixture
def student():
    return Student("Jean", "Clause", "jc@google.it")


def test_student_repr(student):
    assert repr(student) == f"Student(first_name: {student.first_name} last_name: {student.last_name} email: {student.email})"


def test_student_str(student):
    assert str(student) == f"Jean Clause ({student.email})"
