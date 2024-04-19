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

    assert str(empty_statistics) == empty


def test_least_popular_single(student_manager_with_one_student):
    assert student_manager_with_one_student.least_popular() == "DSA, Databases, Flask"


def test_most_popular_multi(student_manager_with_two_student):
    assert student_manager_with_two_student.most_popular() == "Flask"


def test_least_popular_multi(student_manager_with_two_student):
    assert student_manager_with_two_student.least_popular() == "Databases"


def test_highest_activity(student_manager_with_two_student):
    assert student_manager_with_two_student.highest_activity() == "Flask"


def test_lowest_activity(student_manager_with_two_student):
    assert student_manager_with_two_student.lowest_activity() == "Databases"
