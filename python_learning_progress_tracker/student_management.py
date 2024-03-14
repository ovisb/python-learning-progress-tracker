from python_learning_progress_tracker.student import Student


class StudentManagement:

    def __init__(self) -> None:
        self.__students = []

    def add_student(self, student: "Student") -> None:
        self.__students.append(student)

    def __len__(self) -> int:
        return len(self.__students)

    def __repr__(self) -> str:
        return f"StudentManagement(students: {self.__students})"
