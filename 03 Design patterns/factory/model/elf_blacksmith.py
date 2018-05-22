import sys
sys.path.append("..")
from interface.blacksmith import Blacksmith
from model.elf_weapon import ElfWeapon

class ElfBlacksmith(Blacksmith):

    @staticmethod
    def manufacture_weapon(weapon_type):
        return ElfWeapon(weapon_type)