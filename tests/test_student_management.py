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

    assert new_ids == initial_ids.union({"1000", "1001", "1002"})


def test_fail_user_add_duplicate_email(student_manager):
    student_manager.add_student(Student("Jean", "Clause", "jc@google.it"))

    with pytest.raises(ValueError):
        student_manager.add_student(Student("John", "Curt", "jc@google.it"))


def test_no_students_found(student_manager):
    assert str(student_manager) == "No students found"


def test_list_student(student_manager):
    student_manager.add_student(Student("Jean", "Clause", "jc@google.it"))

    assert str(student_manager) == "Students: \n1000", "Expected correct student ID listed after adding new student."


def test_add_points_id_not_found(student_manager):
    student_id = "1000"
    points = 5, 5, 5, 5

    with pytest.raises(ValueError):
        student_manager.add_points(student_id, points)


def test_add_points_success(student_manager):

    student = Student("Jean", "Clause", "jc@google.it")
    student_id = "1000"
    points = 5, 5, 5, 5

    student_manager.add_student(student)
    student_manager.add_points(student_id, points)

    assert student_manager.students[student_id]["course_progress"] == {
        "Python": 5, "DSA": 5, "Databases": 5, "Flask": 5}, "Expected correct course progress after adding points."
