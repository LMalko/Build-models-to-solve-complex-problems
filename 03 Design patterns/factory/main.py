import sys
sys.path.append("..")
from controller.app import App

def main():
    application = App.start_app()


if __name__ == "__main__":
    main ()