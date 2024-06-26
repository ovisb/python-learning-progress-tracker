from python_learning_progress_tracker.menu_choice_validator import MenuChoiceValidator
from python_learning_progress_tracker.student import Student
from python_learning_progress_tracker.student_input_validator import StudentValidator
from python_learning_progress_tracker.student_management import StudentManagement
from python_learning_progress_tracker.statistics import Statistics
from python_learning_progress_tracker.notify import Notify
from python_learning_progress_tracker.menu_choice_validator import MenuChoice


class UserInterface:
    def __init__(self, student_manager: "StudentManagement") -> None:
        self.__student_manager = student_manager
        self.__actions = {
            MenuChoice.ADD_STUDENTS.value: self.__add_student,
            MenuChoice.ADD_POINTS.value: self.__add_student_points,
            MenuChoice.FIND_STUDENT.value: self.__find_student,
            MenuChoice.LIST_STUDENTS.value: self.__list_students,
            MenuChoice.STATISTICS.value: self.__statistics_menu,
            MenuChoice.NOTIFY.value: self.__notify,
        }

    @staticmethod
    def __get_choice() -> str:
        """Get choice from user input."""
        return input().strip()

    @staticmethod
    def __get_student_details() -> str:
        """Get student details from user input."""
        student_info = input()
        return student_info

    @staticmethod
    def __treat_exception_multiple_last_name(
            student_info: list[str],
    ) -> tuple[str, str, str]:
        """Treat exception where student may have multiple names."""
        if len(student_info) >= 4:
            first_name = student_info[0]
            last_name = " ".join(student_info[1: -1])
            email = student_info[-1]
        else:
            first_name, last_name, email = student_info

        return first_name, last_name, email

    @staticmethod
    def __split_input(choice: str) -> list[str]:
        """Split input into a list of strings."""
        return choice.split()

    def __add_student(self):
        """Add student to studentManagement datastore."""
        print("Enter student credentials or 'back' to return: ")
        while True:
            choice = UserInterface.__get_student_details()
            if MenuChoiceValidator.is_back(choice):
                print(
                    f"Total {len(self.__student_manager)} students have been added."
                )
                break

            student_info = UserInterface.__split_input(choice)

            self.__process_student_info(student_info)

    def __process_student_info(self, student_info: list[str]) -> None:
        """Process student information and add student to studentManagement datastore."""
        if not self.__validate_student_information_input(student_info):
            return

        updated_student_info = UserInterface.__treat_exception_multiple_last_name(
            student_info
        )
        try:
            self.__student_manager.add_student(Student(*updated_student_info))
            print("The student has been added.")
        except ValueError as vl:
            print(vl)

    @staticmethod
    def __validate_student_information_input(student_info: list[str]) -> bool:
        """Validate student information input."""
        if not UserInterface.__validate_number_of_student_inputs(student_info):
            return False

        updated_student_info = UserInterface.__treat_exception_multiple_last_name(
            student_info
        )

        if not UserInterface.__validate_student_info(updated_student_info):
            return False

        return True

    def __find_student(self) -> None:
        """Find student from studentManagement datastore."""
        print("Enter an id or 'back' to return: ")
        while True:
            choice = UserInterface.__get_choice().lower()
            if MenuChoiceValidator.is_back(choice):
                break

            try:
                print(self.__student_manager.find_student(choice))
            except ValueError as vl:
                print(vl)
                continue

    def __add_student_points(self) -> None:
        """Add student points to studentManagement datastore."""
        print("Enter an id and points or 'back' to return: ")
        while True:
            choice = UserInterface.__get_choice().lower()
            if MenuChoiceValidator.is_back(choice):
                break

            if not StudentValidator.validate_points_input(choice):
                print("Incorrect points format.")
                continue

            try:
                choice_list = choice.split()
                student_id = choice_list[0]
                points = tuple(int(num) for num in choice_list[1:])
                self.__student_manager.add_points(student_id, points)
                print("Points updated.")
            except ValueError as vl:
                print(vl)
                continue

    def __list_students(self) -> None:
        """List students from studentManagement datastore."""
        print(self.__student_manager)

    def __statistics_menu(self):
        statistics = Statistics(self.__student_manager)
        print("Type the name of a course to see details or 'back' to quit:")
        print(statistics)
        while True:
            inp = input().strip()

            if MenuChoiceValidator.is_back(inp):
                return

            if inp.lower() not in self.__student_manager.accepted_courses:
                print("Unknown course.")
                continue

            course = self.__student_manager.accepted_courses[inp.lower()]

            try:
                statistics_per_course = statistics.fetch_completion_info(course)
                print(course)
                self.__print_statistics(statistics_per_course)
            except ValueError as vl:
                print(vl)

    def __notify(self) -> None:
        notify = Notify(self.__student_manager)
        notify_list = notify.notify()

        if not notify_list:
            print("Total 0 students have been notified.")
            return

        for student, emails in notify_list.items():
            for email in emails:
                print(email)
        print(f"Total {len(notify_list)} students have been notified.")

    @staticmethod
    def __print_statistics(statistics_per_course: list[tuple[str, int, float]]):
        print("id     points   completed")
        for student_id, score, completed_percentage in statistics_per_course:
            print(f"{student_id}   {score}       {completed_percentage:.1f}%")

    @staticmethod
    def __validate_number_of_student_inputs(student_info: list[str]) -> bool:
        """Validate the input during student add."""
        try:
            StudentValidator.validate_number_of_inputs(student_info)
        except ValueError as vl:
            print(vl)
            return False

        return True

    @staticmethod
    def __validate_student_info(student_info: tuple[str, str, str]) -> bool:
        """Validate student info and return True if valid."""
        try:
            StudentValidator.validate_student_info(student_info)
        except ValueError as vl:
            print(vl)
            return False

        return True

    def start(self) -> None:
        """Start the program."""
        while True:
            choice = UserInterface.__get_choice()

            if MenuChoiceValidator.is_exit(choice):
                print("Bye!")
                return

            if MenuChoiceValidator.is_back(choice):
                print("Enter 'exit' to exit the program.")
                continue

            if MenuChoiceValidator.is_empty_input(choice):
                print("No input.")
                continue

            if MenuChoiceValidator.is_list_students(choice):
                self.__list_students()
                continue

            action = self.__actions.get(choice)
            if action:
                action()
            else:
                print("Error: unknown command!")
