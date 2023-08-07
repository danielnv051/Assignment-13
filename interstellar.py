import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width //2
        self.center_y = 48
        self.width = 30
        self.height = 30


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar Game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()


window = Game()
arcade.run()
