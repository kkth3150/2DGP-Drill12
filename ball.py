from pico2d import *
import game_world
import game_framework
import random
class Ball:
    image = None

    def __init__(self, x=None, y=None, speed_x=0, speed_y=0):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x is not None else random.randint(100, 1180)
        self.y = y if y is not None else random.randint(100, 924)
        self.speed_x = speed_x  # px/frame
        self.speed_y = speed_y

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
            case 'zombie:ball':
                game_world.remove_object(self)