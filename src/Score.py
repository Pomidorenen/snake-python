class Score:
    def __init__(self):
        self.score = 0

    def increment(self, value: int):
        self.score += value

    def decrement(self, value: int):
        self.score -= value

    def __str__(self):
        return f'Score: {self.score}'