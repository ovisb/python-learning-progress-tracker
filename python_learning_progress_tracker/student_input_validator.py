import re


class StudentValidator:
    @classmethod
    def __validate_name(cls, name: str) -> bool:
        """Ensure valid name."""
        if cls.__length_bellow_threshold(name):
            return False

        name_pattern = r"^(?!['-])[a-zA-Z]+(?:['\s-][a-zA-Z]+)*(?<!-)$"
        return cls.__validate_pattern(name_pattern, name)

    @classmethod
    def __validate_email(cls, email: str) -> bool:
        """Ensure valid email."""
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return cls.__validate_pattern(email_pattern, email)

    @staticmethod
    def __validate_pattern(name_pattern: str, text: str) -> bool:
        """Validate name pattern."""
        return bool(re.match(name_pattern, text))

    @staticmethod
    def __length_bellow_threshold(name):
        """Ensure that the length of the name is above the threshold."""
        return len(name) < 2

    @staticmethod
    def validate_number_of_inputs(student_info: list[str]) -> None:
        """Validate number of inputs while adding student name and email."""
        if len(student_info) < 3:
            raise ValueError("Incorrect credentials.")

    @staticmethod
    def validate_input_student_id(number: str) -> bool:
        """Validate if string number is numeric"""
        return number.isnumeric()

    @staticmethod
    def validate_points_input(points_text: str) -> bool:
        """Validate if string points input is valid"""
        points_inp = points_text.split()
        if len(points_inp) < 5 or len(points_inp) > 5:
            return False

        return all([StudentValidator.validate_input_student_id(num) for num in points_inp[1:]])

    @classmethod
    def validate_student_info(cls, student_info: tuple[str, str, str]) -> None:
        """Validate student first name, last name and email"""
        first_name, last_name, email = student_info

        if not cls.__validate_name(first_name):
            raise ValueError("Incorrect first name.")

        if not cls.__validate_name(last_name):
            raise ValueError("Incorrect last name.")

        if not cls.__validate_email(email):
            raise ValueError("Incorrect email.")