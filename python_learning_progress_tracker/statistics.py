from python_learning_progress_tracker.student_management import StudentManagement


class Statistics:

    def __init__(self, student_management: StudentManagement) -> None:
        self.__student_management = student_management

    def __str__(self) -> str:
        """ Returns a string representation of the Statistics object """
        return f"""Most popular: {self.__most_popular()}
Least popular: {self.__least_popular()}
Highest activity: {self.__highest_activity()}
Lowest activity: {self.__lowest_activity()}
Easiest course: {self.__easiest_course()}
Hardest course: {self.__hardest_course()}"""

    def __most_popular(self) -> str:
        """Returns the most popular completed courses"""
        enrolments = self.__count_total_submissions_and_points_per_course()

        if not enrolments:
            return "n/a"

        max_val = max([item['submissions'] for item in enrolments.values()])

        return ", ".join(
            [
                course
                for course, enrolment_times in enrolments.items()
                if enrolment_times["submissions"] == max_val
            ]
        )

    def __least_popular(self) -> str:
        """Returns the least popular completed courses"""
        enrolments = self.__count_total_submissions_and_points_per_course()

        if not enrolments:
            return "n/a"

        min_val = min([item['submissions'] for item in enrolments.values()])

        return ", ".join(
            [
                course
                for course, enrolment_times in enrolments.items()
                if enrolment_times["submissions"] == min_val
            ]
        )

    def __highest_activity(self) -> str:
        """Returns the most popular completed courses"""
        max_val = max(self.__student_management.activity_tracker.activity_count.values())

        if max_val == 0:
            return "n/a"

        return self.__filter_courses_by_value(self.__student_management.activity_tracker.activity_count, max_val)

    def __lowest_activity(self) -> str:
        """Returns the least popular completed courses"""
        min_val = min(self.__student_management.activity_tracker.activity_count.values())
        max_val = max(self.__student_management.activity_tracker.activity_count.values())

        if min_val == 0 and max_val == 0:
            return "n/a"

        return self.__filter_courses_by_value(self.__student_management.activity_tracker.activity_count, min_val)

    def __hardest_course(self) -> str:
        """Returns the hardest completed course"""
        try:
            hardest = self.__calculate_highest_lowest()[0]
        except IndexError:
            return "n/a"

        return hardest[0]

    def __easiest_course(self) -> str:
        """Returns the easiest completed course"""
        try:
            easiest = self.__calculate_highest_lowest()[-1]
        except IndexError:
            return "n/a"

        return easiest[0]

    def __calculate_highest_lowest(self) -> list[tuple[str, float]]:
        """Returns a list of tuples containing course and it's average completed, sorted by hardest to lowest."""
        new = []
        total_points_per_course_object = self.__total_points_per_course()
        for course in self.__student_management.available_courses:
            count = self.__count_times_by_course(course)
            if count > 0:
                points_per_course = total_points_per_course_object[course]
                activity_count_per_course = self.__student_management.activity_tracker.activity_count[course]
                average = self.__calculate_average(points_per_course, activity_count_per_course)
                new.append((course, average))

        new.sort(key=lambda x: x[1])
        return new

    @staticmethod
    def __calculate_average(total_points_per_course: int, total_submissions_per_course: int) -> float:
        """Calculate average between total points per course and total submissions per course"""
        return total_points_per_course / total_submissions_per_course

    @staticmethod
    def __filter_courses_by_value(course_data: dict[str, int], value: int) -> str:
        """Return courses which whom match by given value."""
        return ", ".join(
            [
                course
                for course, score in course_data.items()
                if score == value
            ]
        )

    def __count_times_by_course(self, filter_course: str) -> int:
        """Counts the number of times a course has passed the given filter."""
        count = 0
        for student, data in self.__student_management.students.items():
            for course, score in data["course_progress"].items():
                if course == filter_course and score > 0:
                    count += 1
        return count

    def __total_points_per_course(self) -> dict[str, int]:
        """Get total points per course enrolment"""
        total_points_per_course = {}
        for data in self.__student_management.students.values():
            for course, score in data["course_progress"].items():
                total_points_per_course.setdefault(course, 0)
                if score > 0:
                    total_points_per_course[course] += score

        return total_points_per_course

    def __count_total_submissions_and_points_per_course(self) -> dict:
        """Get total submissions and points count per course enrolment"""
        total_submissions_and_points = {}
        for data in self.__student_management.students.values():
            for course, score in data["course_progress"].items():
                total_submissions_and_points.setdefault(course, {})
                total_submissions_and_points[course].setdefault("submissions", 0)
                total_submissions_and_points[course].setdefault("points", 0)
                if score > 0:
                    total_submissions_and_points[course]["submissions"] += 1
                    total_submissions_and_points[course]["points"] += score

        return total_submissions_and_points
