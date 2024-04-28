import pytest
from python_learning_progress_tracker.statistics import Statistics
from python_learning_progress_tracker.student import Student

from python_learning_progress_tracker.student_management import StudentManagement


@pytest.fixture
def student_management():
    return StudentManagement()


@pytest.fixture
def empty_statistics(student_management):
    return Statistics(student_management)


@pytest.fixture()
def student_manager_with_one_student(student_management):
    student = Student("Jean", "Clause", "jc@google.it")
    student_id = "1000"
    points = 5, 0, 0, 0

    student_management.add_student(student)
    student_management.add_points(student_id, points)

    return Statistics(student_management)


@pytest.fixture()
def student_manager_with_two_student(student_management):
    student1 = Student("Jean", "Clause", "jc@google.it")
    student2 = Student("John", "Doe", "jd@google.it")
    points1_s1 = 4, 0, 0, 8
    points2_s1 = 0, 0, 0, 5
    points1_s2 = 0, 8, 0, 4

    student_management.add_student(student1)
    student_management.add_student(student2)

    student_management.add_points("1000", points1_s1)
    student_management.add_points("1000", points2_s1)
    student_management.add_points("1001", points1_s2)

    return Statistics(student_management)


@pytest.fixture()
def student_manager_with_same_points(student_management):
    student1 = Student("Jean", "Clause", "jc@google.it")
    student2 = Student("John", "Doe", "jd@google.it")
    points1_s1 = 5, 4, 3, 2
    points2_s2 = 5, 4, 3, 2

    student_management.add_student(student1)
    student_management.add_student(student2)

    student_management.add_points("1000", points1_s1)
    student_management.add_points("1001", points2_s2)

    return Statistics(student_management)


@pytest.fixture()
def student_manager_more_points(student_management):
    student1 = Student("Jean", "Clause", "jc@google.it")
    student2 = Student("John", "Doe", "jd@google.it")
    points1_s1 = 8, 7, 7, 5
    points2_s1 = 7, 6, 9, 7
    points3_s1 = 6, 5, 5, 0

    points1_s2 = 8, 0, 8, 6
    points2_s2 = 7, 0, 0, 0
    points3_s2 = 9, 0, 0, 5

    student_management.add_student(student1)
    student_management.add_student(student2)

    for points in points1_s1, points2_s1, points3_s1:
        student_management.add_points("1000", points)

    for points in points1_s2, points2_s2, points3_s2:
        student_management.add_points("1001", points)

    return Statistics(student_management)


@pytest.fixture()
def student_manager_with_two_student_no_points(student_management):
    student1 = Student("Jean", "Clause", "jc@google.it")
    student2 = Student("John", "Doe", "jd@google.it")

    student_management.add_student(student1)
    student_management.add_student(student2)

    return Statistics(student_management)


def test_initial_statistics(empty_statistics):
    empty = """Most popular: n/a
Least popular: n/a
Highest activity: n/a
Lowest activity: n/a
Easiest course: n/a
Hardest course: n/a"""

    assert (
            str(empty_statistics) == empty
    ), "Statistics should be empty."


def test_statistics(student_manager_with_two_student):
    statistics = """Most popular: Flask
Least popular: Databases
Highest activity: Flask
Lowest activity: Databases
Easiest course: DSA
Hardest course: Python"""
    assert (
            str(student_manager_with_two_student) == statistics
    ), "Statistics have not been calculated correctly."


def test_statistics_more_points(student_manager_more_points):
    statistics = """Most popular: Python, Databases, Flask
Least popular: DSA
Highest activity: Python
Lowest activity: DSA
Easiest course: Python
Hardest course: Flask"""
    assert (
            str(student_manager_more_points) == statistics
    ), "Statistics have not been calculated correctly."


def test_get_statistics_per_course(student_manager_more_points):
    result = [("1001", 24, 4.0), ("1000", 21, 3.5)]
    assert student_manager_more_points.fetch_completion_info("Python") == result


def test_ensure_no_course_is_in_both_categories(student_manager_with_same_points):
    statistics = """Most popular: Python, DSA, Databases, Flask
Least popular: n/a
Highest activity: Python, DSA, Databases, Flask
Lowest activity: n/a
Easiest course: Python
Hardest course: Flask"""
    assert (
            str(student_manager_with_same_points) == statistics
    ), "Expected least popular and lowest activity to be n/a."
