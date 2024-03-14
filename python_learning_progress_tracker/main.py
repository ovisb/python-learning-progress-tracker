"""Main module"""
from python_learning_progress_tracker.user_interface import UserInterface


def main() -> None:
    print("Learning Progress Tracker")
    ui = UserInterface()
    ui.start()


if __name__ == '__main__':
    main()
