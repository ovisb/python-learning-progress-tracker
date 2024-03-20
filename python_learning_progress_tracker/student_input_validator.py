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

    @staticmethod
    def validate_number_of_inputs(student_info: list[str]) -> None:
        if len(student_info) < 3:
            raise ValueError("Incorrect credentials.")

    @classmethod
    def validate_student_info(cls, student_info: tuple[str, str, str]) -> None:
        first_name, last_name, email = student_info

        if not cls.__validate_name(first_name):
            raise ValueError("Incorrect first name.")

        if not cls.__validate_name(last_name):
            raise ValueError("Incorrect last name.")

        if not cls.__validate_email(email):
            raise ValueError("Incorrect email.")
