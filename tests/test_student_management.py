import pytest

from python_learning_progress_tracker.student_management import StudentManagement
from python_learning_progress_tracker.student import Student

student_manager = StudentManagement()


@pytest.fixture
def empty_student_manager():
    return StudentManagement()


def test_empty_students(empty_student_manager):
    assert len(empty_student_manager) == 0


@pytest.mark.parametrize("input, expected_len", [
    (("Jean", "Clause", "jc@google.it"), 1),
    (("James", "Dean", "james.dean@gmail.com"), 2),
    (("Tim", "Bax", "tim.bax@gmail.com"), 3),
])
def test_add_student(input, expected_len):
    student_manager.add_student(Student(*input))
    assert len(student_manager) == expected_len
