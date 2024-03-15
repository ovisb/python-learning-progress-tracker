import re


class StudentValidator:
    @classmethod
    def __validate_name(cls, name: str) -> bool:
        if cls.__length_bellow_threshold(name):
            return False

        name_pattern = r"^(?!['-])[a-zA-Z]+(?:['\s-][a-zA-Z]+)*(?<!-)$"
        return cls.__validate_pattern(name_pattern, name)

    @classmethod
    def __validate_email(cls, email: str) -> bool:
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return cls.__validate_pattern(email_pattern, email)

    @staticmethod
    def __validate_pattern(name_pattern: str, text: str) -> bool:
        return bool(re.match(name_pattern, text))

    @staticmethod
    def __length_bellow_threshold(name):
        return len(name) < 2

    @classmethod
    def validate_student_info(cls, student_info: tuple[str, str, str]) -> bool:
        first_name, last_name, email = student_info

        if not cls.__validate_name(first_name):
            print("Incorrect first name.")
            return False

        if not cls.__validate_name(last_name):
            print("Incorrect last name.")
            return False

        if not cls.__validate_email(email):
            print("Incorrect email.")
            return False

        return True
