import arcade

class Spaceship:
    ...

class Enemy:
    ...

class Game(arcade.Window):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()