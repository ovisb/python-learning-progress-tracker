from python_learning_progress_tracker.student import Student


class Email:

    def __init__(self, student: Student, course: str):
        self.__student = student
        self.__course = course

    def __str__(self):
        """Return str representation of Email"""
        return f"""To: {self.__student.email}
Re: Your Learning Progress
Hello, {self.__student.first_name} {self.__student.last_name}! You have accomplished our {self.__course} course!"""
