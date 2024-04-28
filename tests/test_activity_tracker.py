import pytest

from python_learning_progress_tracker.activity_tracker import ActivityTracker


@pytest.fixture()
def empty_activity_tracker():
    courses = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
    return ActivityTracker(courses)


@pytest.mark.parametrize(["course", "expected"], [
    ("Python", 1),
    ("DSA", 1),
    ("Databases", 1),
    ("Flask", 1)
])
def test_activity_increments_successfully(empty_activity_tracker, course, expected):
    empty_activity_tracker.increment_activity(course)
    assert (
        empty_activity_tracker.activity_count[course] == expected
    ), "Should increment course by one."
