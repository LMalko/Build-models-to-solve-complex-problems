from enum import Enum
class Nourishment(Enum):
    SATURATED = "saturated"
    HUNGRY = "hungry"
    STARVING = "starving"

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title