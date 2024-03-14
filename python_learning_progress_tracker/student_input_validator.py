import re


class StudentValidator:

    @staticmethod
    def __validate_name(name: str) -> bool:
        if StudentValidator.__length_bellow_threshold(name):
            return False

        name_pattern = r"^(?!['-])[a-zA-Z]+(?:['\s-][a-zA-Z]+)*(?<!-)$"
        return StudentValidator.__validate_pattern(name_pattern, name)

    @staticmethod
    def __validate_email(email: str) -> bool:
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return StudentValidator.__validate_pattern(email_pattern, email)

    @staticmethod
    def __validate_pattern(name_pattern: str, text: str) -> bool:
        return bool(re.match(name_pattern, text))

    @staticmethod
    def __length_bellow_threshold(name):
        return len(name) < 2

    @staticmethod
    def validate_student_info(student_info: tuple[str, str, str]) -> bool:
        first_name, last_name, email = student_info

        if not StudentValidator.__validate_name(first_name):
            print("Incorrect first name.")
            return False

        if not StudentValidator.__validate_name(last_name):
            print("Incorrect last name.")
            return False

        if not StudentValidator.__validate_email(email):
            print("Incorrect email.")
            return False

        return True
