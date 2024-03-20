class MenuChoiceValidator:
    @staticmethod
    def is_exit(choice: str) -> bool:
        return choice == "exit"

    @staticmethod
    def is_back(choice: str) -> bool:
        return choice == "back"

    @staticmethod
    def is_empty_input(choice: str) -> bool:
        return choice.strip() == ""

    @staticmethod
    def is_add_student(choice: str) -> bool:
        return choice == "add students"
