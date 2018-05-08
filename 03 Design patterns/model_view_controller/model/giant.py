class Giant:

    def __init__(self, health, fatigue, nourishment):
        self.health = health
        self.fatigue = fatigue
        self.nourishment = nourishment

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_fatigue(self):
        return self.fatigue

    def set_fatigue(self, fatigue):
        self.fatigue = fatigue

    def get_nourishment(self):
        return self.nourishment

    def set_nourishment(self, nourishment):
        self.nourishment = nourishment

    def __repr__(self):
        return f"The giant looks {self.health.value}, " \
               f"{self.fatigue.value} and {self.nourishment.value}."

