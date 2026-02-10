from typing import List
from workout_tracker.exercises import Exercise

class Workout:
    def __init__(self):
        self._exercises: List[Exercise] = []

    def add_exercise(self, ex):
        if not isinstance(ex, Exercise):
            raise TypeError("Only Exercise objects can be added to a workout")
        self._exercises.append(ex)

    def get_exercises(self):
        return self._exercises.copy()

    def total_calories(self):
        return sum(e.calculate_calories() for e in self._exercises)

    def total_duration(self):
        return sum(e.get_duration() for e in self._exercises)

    def exercise_count(self):
        return len(self._exercises)

    def get_summary(self):
        if not self._exercises:
            return "Empty workout - no exercises added"
        lines = ["=== Workout Summary ==="]
        for i, e in enumerate(self._exercises, 1):
            lines.append(f"{i}. {e}")
        lines.append("----------------------------------------")
        lines.append(f"Total: {self.total_calories():.0f} calories, {self.total_duration():.0f} minutes")
        return "\n".join(lines)

    def __str__(self):
        return f"Workout with {self.exercise_count()} exercise(s), {self.total_calories():.0f} calories"

    def __len__(self):
        return len(self._exercises)