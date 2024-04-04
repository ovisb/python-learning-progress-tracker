from python_learning_progress_tracker.student import Student


class StudentManagement:
    def __init__(self) -> None:
        self.__students: dict[str, dict] = {}
        self.__student_id = 1000
        self.__unique_emails = set()

    def add_student(self, student: "Student") -> None:
        """Add a new student to the management system."""
        student_email = student.email

        if student_email in self.__unique_emails:
            raise ValueError("This email is already taken.")

        default_student_data = {
            "student_data": student,
            "course_progress": {"Python": 0, "DSA": 0, "Databases": 0, "Flask": 0}
        }
        self.students.setdefault(str(self.__student_id), default_student_data)
        self.__student_id += 1
        self.__unique_emails.add(student_email)

    def add_points(self, student_id: str, points: tuple) -> None:
        """Add points to the course progress of a student."""
        if student_id not in self.students:
            raise ValueError(f"No student is found for id={student_id}.")

        course_progress = self.students[student_id]["course_progress"]
        for course, point in zip(course_progress.keys(), points):
            self.students[student_id]["course_progress"][course] += point

    def __str__(self) -> str:
        """Return a string representation of the StudentManagement instance."""
        if not self.students:
            return "No students found"

        initial = "Students: \n"
        return initial + "\n".join(self.students.keys())

    @property
    def students(self):
        """Return the dictionary containing student data."""
        return self.__students

    def __len__(self) -> int:
        """Return the number of students in the management system."""
        return len(self.students)

    def __repr__(self) -> str:
        """Return a string representation of the StudentManagement instance."""
        return f"StudentManagement(students: {self.students})"
