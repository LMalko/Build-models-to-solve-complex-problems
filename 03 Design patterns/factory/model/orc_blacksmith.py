import sys
sys.path.append("..")
from interface.blacksmith import Blacksmith
from model.orc_weapon import OrcWeapon

class OrcBlacksmith(Blacksmith):

    @staticmethod
    def manufacture_weapon(weapon_type):
        return OrcWeapon(weapon_type)