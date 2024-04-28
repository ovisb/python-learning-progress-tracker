from python_learning_progress_tracker.student_management import StudentManagement


class Statistics:

    def __init__(self, student_management: StudentManagement) -> None:
        self.__student_management = student_management
        self.__initialize_stats_vars()

    def __initialize_stats_vars(self):
        self.__enrolments = self.__count_total_submissions_and_points_per_course()
        self.__activity_count = self.__student_management.activity_tracker.activity_count
        self.__max_points_per_course = {"Python": 600, "DSA": 400, "Databases": 480, "Flask": 550}
        self.__lowest_activity_count = min(self.__activity_count.values())
        self.__highest_activity_count = max(self.__activity_count.values())
        self.__submissions_count = [item['submissions'] for item in self.__enrolments.values()]
        self.__submissions_count_max_val = max(self.__submissions_count) if self.__submissions_count else 0
        self.__submissions_count_min_val = min(self.__submissions_count) if self.__submissions_count else 0

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

        if not self.__enrolments:
            return "n/a"

        return ", ".join(self.__filter_submissions_by(self.__submissions_count_max_val))

    def __least_popular(self) -> str:
        """Returns the least popular completed courses"""

        if not self.__enrolments:
            return "n/a"

        if self.__submissions_count_min_val == self.__submissions_count_max_val:
            return "n/a"

        return ", ".join(self.__filter_submissions_by(self.__submissions_count_min_val))

    def __filter_submissions_by(self, value: int):
        """Filters the submissions by the max or min value"""
        return [
            course
            for course, enrolment_times in self.__enrolments.items()
            if enrolment_times["submissions"] == value
        ]

    def __highest_activity(self) -> str:
        """Returns the most popular completed courses"""

        if self.__highest_activity_count == 0:
            return "n/a"

        return self.__filter_courses_by_value(self.__activity_count, self.__highest_activity_count)

    def __lowest_activity(self) -> str:
        """Returns the least popular completed courses"""

        if self.__lowest_activity_count == 0 and self.__highest_activity_count == 0:
            return "n/a"

        if self.__lowest_activity_count == self.__highest_activity_count:
            return "n/a"

        return self.__filter_courses_by_value(self.__activity_count, self.__lowest_activity_count)

    def __hardest_course(self) -> str:
        """Returns the hardest completed course"""
        try:
            hardest_course = self.__calculate_highest_lowest()[0]
        except IndexError:
            return "n/a"

        return hardest_course[0]

    def __easiest_course(self) -> str:
        """Returns the easiest completed course"""
        try:
            easiest_course = self.__calculate_highest_lowest()[-1]
        except IndexError:
            return "n/a"

        return easiest_course[0]

    def __calculate_highest_lowest(self) -> list[tuple[str, float]]:
        """Returns a list of tuples containing course, and it's average completed, sorted by hardest to lowest."""
        list_of_courses_averages = []
        total_points_per_course_object = self.__total_points_per_course()
        for course in self.__student_management.available_courses:
            count = self.__count_times_by_course(course)
            if count > 0:
                points_per_course = total_points_per_course_object[course]
                activity_count_per_course = self.__activity_count[course]
                average = self.__calculate_average(points_per_course, activity_count_per_course)
                list_of_courses_averages.append((course, average))

        list_of_courses_averages.sort(key=lambda x: x[1])
        return list_of_courses_averages

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

    def fetch_completion_info(self, course: str) -> list[tuple[str, int, float]]:
        """Return information about students which have more than 0 points on given course
        Get info about student id, it's course score and completed percent value.
        """
        statistics_per_course = []
        for student_id, data in self.__student_management.students.items():
            for crs, score in data["course_progress"].items():
                if crs == course and score > 0:
                    completed_percentage = self.__calculate_course_completed_percentage(course, score)
                    statistics_per_course.append((student_id, score, round(completed_percentage, 1)))

        if statistics_per_course:
            statistics_per_course.sort(key=lambda x: x[2], reverse=True)

        return statistics_per_course

    def __calculate_course_completed_percentage(self, course: str, score: int) -> float:
        """Calculate percentage of completed course"""
        max_point: int = self.__max_points_per_course[course]

        return score / max_point * 100
