import pytest

from python_learning_progress_tracker.student import Student
from python_learning_progress_tracker.student_management import StudentManagement


@pytest.fixture()
def student_manager():
    return StudentManagement()


def test_empty_students(student_manager):
    assert len(student_manager) == 0


def test_add_student(student_manager):
    initial_len = len(student_manager.students)
    students = [
        ("Jean", "Clause", "jc@google.it"),
        ("James", "Dean", "james.dean@gmail.com"),
        ("Tim", "Bax", "tim.bax@gmail.com")
    ]
    for student in students:
        student_manager.add_student(Student(*student))

    new_len = len(student_manager.students)

    assert new_len == initial_len + len(students)


def test_increment_student_ids(student_manager):
    initial_ids = set(student_manager.students.keys())

    students = [
        ("Jean", "Clause", "jc@google.it"),
        ("James", "Dean", "james.dean@gmail.com"),
        ("Tim", "Bax", "tim.bax@gmail.com")
    ]

    for student in students:
        student_manager.add_student(Student(*student))

    new_ids = set(student_manager.students.keys())

    assert new_ids == initial_ids.union({1000, 1001, 1002})
