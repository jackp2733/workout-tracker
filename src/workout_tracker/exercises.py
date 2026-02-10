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
    def __init__(self, name, *, distance, duration, date=None):
        super().__init__(name, date)
        self.distance = distance
        self.duration = duration

    def calculate_calories(self):
        return self.distance * 100

    def get_duration(self):
        return self.duration

    def __str__(self):
        return f"{self.name} ({self.distance} miles, {self.duration} min): {self.calculate_calories():.0f} calories"


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
    INTENSITY_MULTIPLIERS = {"low": 1.0, "medium": 1.5, "high": 2.0}

    def __init__(self, name, *, duration, intensity="medium", date=None):
        super().__init__(name, date)
        self.duration = duration
        self.intensity = intensity.lower()
        if self.intensity not in self.INTENSITY_MULTIPLIERS:
            raise ValueError("Intensity must be 'low', 'medium', or 'high'")

    def calculate_calories(self):
        return self.duration * 2.5 * self.INTENSITY_MULTIPLIERS[self.intensity]

    def get_duration(self):
        return self.duration

    def __str__(self):
        return f"{self.name} ({self.duration} min, {self.intensity} intensity): {self.calculate_calories():.0f} calories"