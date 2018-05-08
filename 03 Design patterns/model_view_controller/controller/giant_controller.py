import sys
sys.path.append("..")
from view.view import *

class GiantController:

    def __init__(self, giant, view):
        self.giant = giant
        self.view = view

    def get_health(self):
        return self.giant.get_health()

    def set_health(self, health):
        self.giant.set_health(health)

    def get_fatigue(self):
        return self.giant.get_fatigue()

    def set_fatigue(self, fatigue):
        self.giant.set_fatigue(fatigue)

    def get_nourishment(self):
        return self.giant.get_nourishment()

    def set_nourishment(self, nourishment):
        self.giant.set_nourishment(nourishment)

    def update_view(self):
        self.view.print_text(self.giant)