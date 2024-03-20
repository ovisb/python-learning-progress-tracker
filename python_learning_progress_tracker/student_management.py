from python_learning_progress_tracker.student import Student


class StudentManagement:
    def __init__(self) -> None:
        self.__students: dict[int, dict] = {}
        self.__student_id = 1000

    def add_student(self, student: "Student") -> None:
        self.__students[self.__student_id] = {"student_data": student, "course_progress": []}
        self.__student_id += 1

    @property
    def students(self):
        return self.__students

    def __len__(self) -> int:
        return len(self.__students)

    def __repr__(self) -> str:
        return f"StudentManagement(students: {self.__students})"
