from python_learning_progress_tracker.student import Student
import re


class UserInterface:

    @staticmethod
    def __get_input() -> str:
        return input().strip()

    @staticmethod
    def __get_user_details() -> str:
        student_info = input()
        return student_info

    @staticmethod
    def __validate_pattern(pattern: str, text: str) -> bool:
        return bool(re.match(pattern, text))

    @staticmethod
    def __length_bellow_threshold(name):
        return len(name) < 2

    @classmethod
    def __validate_name(cls, name: str) -> bool:
        if cls.__length_bellow_threshold(name):
            return False

        pattern = r"^(?!['-])[a-zA-Z]+(?:['\s-][a-zA-Z]+)*(?<!-)$"
        return cls.__validate_pattern(pattern, name)

    @classmethod
    def __validate_email(cls, email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return cls.__validate_pattern(pattern, email)

    @staticmethod
    def __validate_number_of_inputs(student_info: list[str]) -> bool:
        if len(student_info) < 3:
            print("Incorrect credentials.")
            return False

        return True

    @staticmethod
    def __validate_student_info(student_info: tuple) -> bool:
        first_name, last_name, email = student_info

        if not UserInterface.__validate_name(first_name):
            print("Incorrect first name.")
            return False

        if not UserInterface.__validate_name(last_name):
            print("Incorrect last name.")
            return False

        if not UserInterface.__validate_email(email):
            print("Incorrect email.")
            return False

        return True

    @staticmethod
    def __treat_exception_multiple_last_name(student_info: list[str]) -> tuple[str, str, str]:
        if len(student_info) >= 4:
            first_name = student_info[0]
            # last_name = student_info[1] + " " + student_info[2]
            last_name = " ".join(student_info[1:len(student_info) - 1])
            email = student_info[-1]
        else:
            first_name, last_name, email = student_info

        return first_name, last_name, email

    @staticmethod
    def start() -> None:
        users = []
        while True:
            choice = UserInterface.__get_input()
            if choice == "exit":
                print("Bye!")
                return

            elif choice == "back":
                print("Enter 'exit' to exit the program.")
                continue

            elif choice == "":
                print("No input.")

            elif choice == "add students":
                print("Enter student credentials or 'back' to return: ")
                while True:
                    choice = UserInterface.__get_user_details()
                    if choice == "back":
                        print(f"Total {len(users)} students have been added.")
                        break

                    student_info = choice.split()

                    if not UserInterface.__validate_number_of_inputs(student_info):
                        continue

                    student_info = UserInterface.__treat_exception_multiple_last_name(student_info)

                    if not UserInterface.__validate_student_info(student_info):
                        continue

                    users.append(Student(*student_info))
                    print("The student has been added.")
            else:
                print("Error: unknown command!")
