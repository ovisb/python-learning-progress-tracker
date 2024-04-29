from typing import Union

from python_learning_progress_tracker.student import Student
from python_learning_progress_tracker.activity_tracker import ActivityTracker


class StudentManagement:
    def __init__(self) -> None:
        self.__students: dict[str, dict] = {}
        self.__student_id = 1000
        self.__unique_emails = set()
        self.__default_courses: dict[str, int] = {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
        self.__max_points_per_course = {"Python": 600, "DSA": 400, "Databases": 480, "Flask": 550}
        self.__accepted_courses = {"python": "Python", "dsa": "DSA", "databases": "Databases", "flask": "Flask"}
        self.__activity_tracker = ActivityTracker(self.__default_courses.copy())
        self.__completed_courses = {}
        self.__to_notify_students = {}

    def add_student(self, student: "Student") -> None:
        """Add a new student to the management system."""
        student_email = student.email

        if student_email in self.__unique_emails:
            raise ValueError("This email is already taken.")

        default_student_data = {
            "student_data": student,
            "course_progress": self.__default_courses.copy()
        }
        self.students.setdefault(str(self.__student_id), default_student_data)
        self.__student_id += 1
        self.__unique_emails.add(student_email)

    def __student_id_exists(self, student_id: str) -> bool:
        """Check if student_id exists in the management system."""
        if student_id not in self.students:
            return False
        return True

    def add_points(self, student_id: str, points: tuple) -> None:
        """Public interface for calling add_points."""
        if not self.__student_id_exists(student_id):
            raise ValueError(f"No student is found for id={student_id}.")

        course_progress = self.students[student_id]["course_progress"]
        for course, point in zip(course_progress.keys(), points):
            self.__add_point(student_id, course, point)

            if point > 0:
                self.__activity_tracker.increment_activity(course)

    def __add_point(self, student_id: str, course: str, point: int) -> None:
        """Add a point to the course progress of a student.
          IF points >= max_points_per_course add to completed list and to notify list
        """
        max_points_course_limit = self.__max_points_per_course[course]
        current_course_points = self.students[student_id]["course_progress"][course]

        if current_course_points + point < max_points_course_limit:
            self.students[student_id]["course_progress"][course] += point
            return

        self.students[student_id]["course_progress"][course] = max_points_course_limit

        student_object = self.students[student_id]["student_data"]
        self.__completed_courses.setdefault(student_object, [])

        if course not in self.__completed_courses[student_object]:
            self.__add_to_completed_and_notify(student_object, course)

    def __add_to_completed_and_notify(self, student_object: Student, course: str):
        """Add student and course to notify list."""
        self.__completed_courses[student_object].append(course)
        self.__to_notify_students.setdefault(student_object, []).append(course)

    def find_student(self, student_id: str) -> Union[ValueError, str]:
        """Find a student by its ID and raise an error if it already exists."""
        if student_id not in self.students:
            raise ValueError(f"No student is found for id={student_id}.")

        return f"{student_id} points: {self.__format_course_progress(student_id)}"

    def __str__(self) -> str:
        """Return a string representation of the StudentManagement instance."""
        if not self.students:
            return "No students found"

        initial = "Students: \n"
        return initial + "\n".join(self.students.keys())

    def __format_course_progress(self, student_id: str) -> str:
        """Pretty print the course progress of a student."""
        course_progress = self.students[student_id]["course_progress"]
        new = []
        for key, val in course_progress.items():
            new.append(f"{key}={val}")

        return "; ".join(new)

    @property
    def available_courses(self) -> list[str]:
        """Return a list of available courses."""
        return list(self.__default_courses.keys())

    @property
    def students(self) -> dict[str, dict]:
        """Return the dictionary containing student data."""
        return self.__students

    @property
    def activity_tracker(self) -> ActivityTracker:
        """Return the ActivityTracker instance."""
        return self.__activity_tracker

    @property
    def accepted_courses(self) -> dict[str, str]:
        """Return the dictionary containing accepted courses."""
        return self.__accepted_courses

    @property
    def max_points_per_course(self) -> dict[str, int]:
        """Return the dictionary containing max points per course."""
        return self.__max_points_per_course

    @property
    def completed_courses(self):
        """Return the dictionary containing completed courses."""
        return self.__completed_courses

    @property
    def to_notify_students(self):
        """Return the dictionary containing student data to notify."""
        return self.__to_notify_students

    def __len__(self) -> int:
        """Return the number of students in the management system."""
        return len(self.students)

    def __repr__(self) -> str:
        """Return a string representation of the StudentManagement instance."""
        return f"StudentManagement(students: {self.students})"
