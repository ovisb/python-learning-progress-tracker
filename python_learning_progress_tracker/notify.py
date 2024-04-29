from python_learning_progress_tracker.student_management import StudentManagement
from python_learning_progress_tracker.email_template import Email
from python_learning_progress_tracker.student import Student


class Notify:

    def __init__(self, student_management: StudentManagement):
        self.__to_notify = student_management.to_notify_students

    def notify(self) -> dict[Student, list[Email]]:
        emails = {}

        for student in self.__to_notify:
            for course in self.__to_notify[student]:
                emails.setdefault(student, []).append(Email(student, course))

        self.__to_notify.clear()
        return emails

    @property
    def to_notify(self) -> dict:
        return self.__to_notify
