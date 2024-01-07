import arcade
from src.game import Game


def main():
    game = Game()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
