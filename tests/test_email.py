from python_learning_progress_tracker.email import Email
from python_learning_progress_tracker.student import Student


def test_email():
    student = Student("John", "Doe", "johnd@google.it")
    course = "Python"
    email = Email(student, course)

    email_template = f"""To: johnd@google.it
Re: Your Learning Progress
Hello, John Doe! You have accomplished our {course} course!"""

    assert str(email) == email_template
