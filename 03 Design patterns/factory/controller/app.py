import sys
sys.path.append("..")
from model.elf_blacksmith import ElfBlacksmith
from model.orc_blacksmith import OrcBlacksmith
from enums.weapon_type import WeaponType

class App:

    def __init__(self, blacksmith):
        self.blacksmith = blacksmith

    @staticmethod
    def start_app():
        app_orc = App(OrcBlacksmith())
        app_orc.manufacture_weapons()

        app_elf = App(ElfBlacksmith())
        app_elf.manufacture_weapons()

    def manufacture_weapons(self):

        weapon_one = self.blacksmith.manufacture_weapon(WeaponType.SPEAR.value)
        print(weapon_one)
        weapon_two = self.blacksmith.manufacture_weapon(WeaponType.AXE.value)
        print(weapon_two)