class ActivityTracker:
    def __init__(self, activity_count_track: dict[str, int]):
        self.__activity_count_track = activity_count_track

    def increment_activity(self, course: str):
        """Increment course activity count."""
        self.__activity_count_track[course] += 1

    @property
    def activity_count(self):
        """return activity count."""
        return self.__activity_count_track
