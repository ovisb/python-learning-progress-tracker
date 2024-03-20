class Student:
    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"

    def __repr__(self) -> str:
        return f"Student(first_name: {self.first_name} last_name: {self.last_name} email: {self.email})"

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email(self) -> str:
        return self.__email
