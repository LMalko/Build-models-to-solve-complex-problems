from enum import Enum

class WeaponType(Enum):

    SHORT_SWORD = "short sword"
    SPEAR = "spear"
    AXE = "axe"
    UNDEFINED = "undefined"

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title