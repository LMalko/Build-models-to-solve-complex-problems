from enum import Enum
class Fatigue(Enum):

    ALERT = "alert"
    TIRED = "tired"
    SLEEPING = "sleeping"

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title