from python_learning_progress_tracker.student import Student


class StudentManagement:
    def __init__(self) -> None:
        self.__students: dict[int, dict] = {}
        self.__student_id = 1000
        self.__unique_emails = set()

    def add_student(self, student: "Student") -> None:
        student_email = student.email

        if student_email in self.__unique_emails:
            raise ValueError("This email is already taken.")

        self.__students.setdefault(self.__student_id, {"student_data": student, "course_progress": []})
        self.__student_id += 1
        self.__unique_emails.add(student_email)

    @property
    def students(self):
        return self.__students

    def __len__(self) -> int:
        return len(self.__students)

    def __repr__(self) -> str:
        return f"StudentManagement(students: {self.__students})"
