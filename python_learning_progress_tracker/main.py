"""Main module"""
from python_learning_progress_tracker.user_interface import UserInterface
from python_learning_progress_tracker.student_management import StudentManagement


def main() -> None:
    print("Learning Progress Tracker")
    student_manager = StudentManagement()
    ui = UserInterface(student_manager)
    ui.start()


if __name__ == '__main__':
    main()
