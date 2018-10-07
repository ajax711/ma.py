from pyfiglet import Figlet
from mapy import Mapy
import argparse

DESCRIPTION = "Play the most awesome geo-diplo-political" \
              " CLI trivia-game of all-time!\nYou can either " \
              "pass no arguments and receive a random country, " \
              "or enter a\ncountry of your liking."


def main():
    try:
        f = Figlet()
        welcome_message = f.renderText('ma.py')
        print(welcome_message + "\nIf you wish to"
                                " exit the program, hit Ctrl+c")
        parser = argparse.ArgumentParser(description=DESCRIPTION)
        mapy = Mapy(parser=parser)
        mapy.run(mapy.args)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
