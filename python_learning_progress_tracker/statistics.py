from python_learning_progress_tracker.student_management import StudentManagement


class Statistics:

    def __init__(self, student_management: StudentManagement) -> None:
        self.__student_management = student_management

    def __str__(self) -> str:
        """ Returns a string representation of the Statistics object """
        return f"""Most popular: n/a
Least popular: n/a
Highest activity: n/a
Lowest activity: n/a
Easiest course: n/a
Hardest course: n/a"""

    def most_popular(self) -> str:
        """Returns the most popular completed courses"""
        enrolments = self.__total_points_per_course()

        max_val = max(enrolments.values())
        if max_val == 0:
            return "n/a"

        return ", ".join(
            [
                course
                for course, enrolment_times in enrolments.items()
                if enrolment_times == max_val
            ]
        )

    def least_popular(self) -> str:
        """Returns the least popular completed courses"""
        enrolments = self.__total_points_per_course()

        max_val = max(enrolments.values())
        min_val = min(enrolments.values())

        if max_val == min_val:
            return "n/a"

        return ", ".join(
            [
                course
                for course, enrolment_times in enrolments.items()
                if enrolment_times == min_val
            ]
        )

    def __total_points_per_course(self) -> dict[str, int]:
        """Get total points per course enrolment"""
        total_points_per_course = self.__student_management.default_courses.copy()
        for data in self.__student_management.students.values():
            for course, score in data["course_progress"].items():
                if score > 0:
                    total_points_per_course[course] += score

        return total_points_per_course

    def __total_enrolments_per_course(self) -> dict[str, int]:
        """Get total number of enrolments per course"""
        enrolments = self.__student_management.default_courses.copy()
        for data in self.__student_management.students.values():
            for course, score in data["course_progress"].items():
                if score > 0:
                    enrolments[course] += 1

        return enrolments
