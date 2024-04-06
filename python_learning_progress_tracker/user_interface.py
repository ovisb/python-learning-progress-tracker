from typing import Union

from python_learning_progress_tracker.menu_choice_validator import MenuChoiceValidator
from python_learning_progress_tracker.student import Student
from python_learning_progress_tracker.student_input_validator import StudentValidator
from python_learning_progress_tracker.student_management import StudentManagement


class UserInterface:
    def __init__(self, student_manager: "StudentManagement") -> None:
        self.__student_manager = student_manager

    @staticmethod
    def __get_input() -> str:
        return input().strip()

    @staticmethod
    def __get_user_details() -> str:
        student_info = input()
        return student_info

    @staticmethod
    def __treat_exception_multiple_last_name(
            student_info: list[str],
    ) -> tuple[str, str, str]:
        if len(student_info) >= 4:
            first_name = student_info[0]
            last_name = " ".join(student_info[1: -1])
            email = student_info[-1]
        else:
            first_name, last_name, email = student_info

        return first_name, last_name, email

    @staticmethod
    def __split_input(choice: str) -> list[str]:
        return choice.split()

    def __add_student_choice(self):
        while True:
            choice = UserInterface.__get_user_details()
            if MenuChoiceValidator.is_back(choice):
                print(
                    f"Total {len(self.__student_manager)} students have been added."
                )
                break

            student_info = UserInterface.__split_input(choice)

            if not UserInterface.__validate_input(student_info):
                continue

            updated_student_info = UserInterface.__treat_exception_multiple_last_name(
                student_info
            )

            if not UserInterface.__validate_student_info(updated_student_info):
                continue

            self.__student_manager.add_student(Student(*updated_student_info))
            print("The student has been added.")

    def __find_student(self) -> None:
        while True:
            choice = UserInterface.__get_input().lower()
            if MenuChoiceValidator.is_back(choice):
                break

            # to implement validation
            if not StudentValidator.validate_input_student_id(choice):
                print("Please input a non-negative number as the ID.")
                continue

            try:
                print(self.__student_manager.find_student(choice))
            except ValueError as vl:
                print(vl)
                continue

    def __add_student_points(self) -> None:
        while True:
            choice = UserInterface.__get_input().lower()
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
        print(self.__student_manager)

    @staticmethod
    def __validate_input(student_info: list[str]) -> bool:
        try:
            StudentValidator.validate_number_of_inputs(student_info)
        except ValueError as vl:
            print(vl)
            return False

        return True

    @staticmethod
    def __validate_student_info(student_info: tuple[str, str, str]) -> bool:
        try:
            StudentValidator.validate_student_info(student_info)
        except ValueError as vl:
            print(vl)
            return False

        return True

    def start(self) -> None:
        while True:
            choice = UserInterface.__get_input()

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

            if MenuChoiceValidator.is_add_student(choice):
                print("Enter student credentials or 'back' to return: ")
                self.__add_student_choice()
            elif MenuChoiceValidator.is_add_points(choice):
                print("Enter an id and points or 'back' to return: ")
                self.__add_student_points()
            elif MenuChoiceValidator.is_find_student(choice):
                print("Enter an id or 'back' to return: ")
                self.__find_student()
            else:
                print("Error: unknown command!")
