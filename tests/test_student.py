import pytest

from python_learning_progress_tracker.student import Student


@pytest.fixture
def student():
    return Student("Jean", "Clause", "jc@google.it")


def test_student_repr(student):
    assert (
            repr(student)
            == f"Student(first_name: {student.first_name} last_name: {student.last_name} email: {student.email})"
    )


def test_student_str(student):
    assert str(student) == f"Jean Clause ({student.email})"


def test_student_eq(student):
    s1 = Student("Jean", "Clause", "jc@google.it")
    s2 = Student("Jean", "Clause", "jc@google.it")

    assert s1 == s2, "Should be equal."


def test_student_not_eq(student):
    s1 = Student("Jean", "Clause", "jc@google.it")
    s2 = Student("Jean", "Clause", "jc@google.itas")

    assert s1 != s2, "Should not equal."
