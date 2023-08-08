import random
import arcade


class Spaceship(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.center_x=game.width//2
        self.center_y=50
        self.width=48
        self.height=48
        self.speed=10   

class Enemy(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x=game.width //2
        self.center_y=self.height *2
        self.width=48
        self.height=48
        self.angle=180
        self.speed=4


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800,height=600,title="Interstellar")
        self.background= arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me=Spaceship(self)
        self.enemy=Enemy(self)
   
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        print(symbol)
        if symbol == 97:   
            self.me.center_x=self.me.center_x-self.me.speed
        elif symbol == 100:   
            self.me.center_x=self.me.center_x+self.me.speed

    def on_update(self, delta_time: float):
        self.enemy.center_y-=self.enemy.speed



window=Game()
arcade.run()