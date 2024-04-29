import pytest

from python_learning_progress_tracker.student import Student
from python_learning_progress_tracker.student_management import StudentManagement


@pytest.fixture()
def empty_student_manager():
    return StudentManagement()


@pytest.fixture()
def student_manager_with_student():
    student_manager = StudentManagement()
    student = Student("Jean", "Clause", "jc@google.it")
    student_id = "1000"
    points = 5, 5, 5, 5

    student_manager.add_student(student)
    student_manager.add_points(student_id, points)

    return student_manager


@pytest.fixture()
def manager_with_completed_course_one_student():
    student_manager = StudentManagement()
    student = Student("Jean", "Clause", "jc@google.it")
    student_id = "1000"
    points = 600, 400, 400, 550

    student_manager.add_student(student)
    student_manager.add_points(student_id, points)

    return student_manager


def test_empty_students(empty_student_manager):
    assert len(empty_student_manager) == 0


def test_add_student(empty_student_manager):
    initial_len = len(empty_student_manager.students)
    students = [
        ("Jean", "Clause", "jc@google.it"),
        ("James", "Dean", "james.dean@gmail.com"),
        ("Tim", "Bax", "tim.bax@gmail.com")
    ]
    for student in students:
        empty_student_manager.add_student(Student(*student))

    new_len = len(empty_student_manager.students)

    assert new_len == initial_len + len(students)


def test_increment_student_ids(empty_student_manager):
    initial_ids = set(empty_student_manager.students.keys())

    students = [
        ("Jean", "Clause", "jc@google.it"),
        ("James", "Dean", "james.dean@gmail.com"),
        ("Tim", "Bax", "tim.bax@gmail.com")
    ]

    for student in students:
        empty_student_manager.add_student(Student(*student))

    new_ids = set(empty_student_manager.students.keys())

    assert new_ids == initial_ids.union({"1000", "1001", "1002"})


def test_fail_user_add_duplicate_email(empty_student_manager):
    empty_student_manager.add_student(Student("Jean", "Clause", "jc@google.it"))

    with pytest.raises(ValueError):
        empty_student_manager.add_student(Student("John", "Curt", "jc@google.it"))


def test_no_students_found(empty_student_manager):
    assert str(empty_student_manager) == "No students found"


def test_list_student(empty_student_manager):
    empty_student_manager.add_student(Student("Jean", "Clause", "jc@google.it"))

    assert str(
        empty_student_manager) == "Students: \n1000", "Expected correct student ID listed after adding new student."


def test_add_points_id_not_found(empty_student_manager):
    student_id = "1000"
    points = 5, 5, 5, 5

    with pytest.raises(ValueError):
        empty_student_manager.add_points(student_id, points)


def test_add_points_success(empty_student_manager):
    student = Student("Jean", "Clause", "jc@google.it")
    student_id = "1000"
    points = 5, 5, 5, 5

    empty_student_manager.add_student(student)
    empty_student_manager.add_points(student_id, points)

    assert empty_student_manager.students[student_id]["course_progress"] == {
        "Python": 5, "DSA": 5, "Databases": 5, "Flask": 5}, "Expected correct course progress after adding points."


def test_fail_finding_student(empty_student_manager):
    with pytest.raises(ValueError):
        empty_student_manager.find_student("1000"), "Expected to raise error if student ID not found."


def test_success_find_student(student_manager_with_student):
    assert student_manager_with_student.find_student("1000") == f"1000 points: Python=5; DSA=5; Databases=5; Flask=5"


def test_points_do_not_exceed_limits(empty_student_manager):
    student = Student("Jean", "Clause", "jc@google.it")
    points = 550, 350, 450, 500
    points_overflow = 60, 60, 60, 60

    max_points_limit = [600, 400, 480, 550]

    empty_student_manager.add_student(student)
    empty_student_manager.add_points("1000", points)
    empty_student_manager.add_points("1000", points_overflow)

    student_obj = empty_student_manager.students["1000"]
    assert (
            list(student_obj["course_progress"].values()) == max_points_limit
    ), "Expected course points to not exceed max limits."


def test_no_completed_course(student_manager_with_student):
    assert (
            student_manager_with_student.completed_courses == {}
    ), "Expected no completed courses."


def test_completed_course_student_added_in_list(manager_with_completed_course_one_student):
    assert (
            len(manager_with_completed_course_one_student.completed_courses) == 1
    ), "Expected 1 completed course."


@pytest.mark.parametrize(["data", "expected"], [
    (((600, 0, 0, 0), "Python"), True),
    (((0, 400, 0, 0), "DSA"), True),
    (((0, 0, 480, 0), "Databases"), True),
    (((0, 0, 0, 550), "Flask"), True),
    (((450, 0, 0, 0), "Python"), False),
    (((0, 0, 0, 0), "Python"), False),
    (((0, 0, 0, 0), "Databases"), False),
    (((0, 0, 0, 0), "DSA"), False),
    (((0, 0, 0, 0), "Flask"), False),
]
)
def test_successfully_added_one_course_to_notify(data, expected, empty_student_manager):
    points, course = data
    student = Student("Jean", "Clause", "jc@google.it")

    empty_student_manager.add_student(student)
    empty_student_manager.add_points("1000", points)

    result = course in empty_student_manager.to_notify_students[student] if empty_student_manager.to_notify_students.get(student, []) else False
    assert result is expected, f"Expected result to be {expected}, but got {result}"
