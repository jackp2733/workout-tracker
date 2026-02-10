from datetime import datetime

class Exercise:
    def __init__(self, name, date=None):
        self.name = name
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def calculate_calories(self):
        return 0.0

    def get_duration(self):
        return 0.0

    def __str__(self):
        return f"{self.name}: {self.calculate_calories():.0f} calories"


class CardioExercise(Exercise):
    def __init__(self, name, dist, dur, date=None):
        super().__init__(name, date)
        self.dist = dist
        self.dur = dur

    def calculate_calories(self):
        return self.dist * 100

    def get_duration(self):
        return self.dur

    def __str__(self):
        return f"{self.name} ({self.dist} miles, {self.dur} min): {self.calculate_calories():.0f} calories"


class StrengthExercise(Exercise):
    def __init__(self, name, weight, reps, sets, date=None):
        super().__init__(name, date)
        self.weight = weight
        self.reps = reps
        self.sets = sets

    def calculate_calories(self):
        return self.weight * self.reps * self.sets * 0.05

    def get_duration(self):
        return self.sets * 3

    def __str__(self):
        return f"{self.name} ({self.weight} lbs x {self.reps} reps x {self.sets} sets): {self.calculate_calories():.0f} calories"


class FlexibilityExercise(Exercise):
    MULTIPLIERS = {"low": 1.0, "medium": 1.5, "high": 2.0}

    def __init__(self, name, dur, intensity="medium", date=None):
        super().__init__(name, date)
        self.dur = dur
        self.intensity = intensity.lower()
        if self.intensity not in self.MULTIPLIERS:
            raise ValueError("Intensity must be 'low', 'medium', or 'high'")

    def calculate_calories(self):
        return self.dur * 2.5 * self.MULTIPLIERS[self.intensity]

    def get_duration(self):
        return self.dur

    def __str__(self):
        return f"{self.name} ({self.dur} min, {self.intensity} intensity): {self.calculate_calories():.0f} calories"