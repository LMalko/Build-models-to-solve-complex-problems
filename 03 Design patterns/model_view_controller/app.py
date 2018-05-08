from controller.giant_controller import *
from model.giant import *
from model.health import *
from model.fatigue import *
from model.nourishment import *
from view.view import *

def main():
    # create model, view and controller
    giant = Giant(Health.HEALTHY, Fatigue.ALERT, Nourishment.SATURATED)
    view = View()
    controller = GiantController(giant, view)
    # initial display
    controller.update_view()
    # controller receives some interactions that affect the giant
    controller.set_health(Health.WOUNDED)
    controller.set_fatigue(Fatigue.TIRED)
    controller.set_nourishment(Nourishment.HUNGRY)
    # redisplay
    controller.update_view ()

if __name__ == "__main__":
    main()