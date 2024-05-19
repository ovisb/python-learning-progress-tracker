from enum import Enum


class MenuChoice(Enum):
    EXIT = "exit"
    BACK = "back"
    EMPTY = ""
    ADD_STUDENTS = "add students"
    ADD_POINTS = "add points"
    LIST_STUDENTS = "list"
    FIND_STUDENT = "find"
    STATISTICS = "statistics"
    NOTIFY = "notify"


class MenuChoiceValidator:
    @staticmethod
    def is_exit(choice: str) -> bool:
        return choice == MenuChoice.EXIT.value

    @staticmethod
    def is_back(choice: str) -> bool:
        return choice == MenuChoice.BACK.value

    @staticmethod
    def is_empty_input(choice: str) -> bool:
        return choice.strip() == MenuChoice.EMPTY.value

    @staticmethod
    def is_add_points(choice: str) -> bool:
        return choice == MenuChoice.ADD_POINTS.value

    @staticmethod
    def is_list_students(choice: str) -> bool:
        return choice == MenuChoice.LIST_STUDENTS.value
