from enum import Enum
class Health(Enum):

    HEALTHY ="healthy"
    WOUNDED = "wounded"
    DEAD = "dead"

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title