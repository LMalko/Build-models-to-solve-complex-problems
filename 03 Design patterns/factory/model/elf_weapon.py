import sys
sys.path.append("..")
from interface.weapon import Weapon

class ElfWeapon(Weapon):

    def __init__(self, weapon_type):
        self.weapon_type = weapon_type


    def __repr__(self):
        return f"Elven {self.weapon_type}"


    def get_weapon_type(self):
        return self.weapon_type