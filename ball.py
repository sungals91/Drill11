from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity
        #self.font = load_font('ENCR10B.TTF', 16)

    def draw(self):
        self.image.draw(self.x, self.y)
        #self.font.draw(self.x - 10, self.y + 20, f'{self.is_flying}', (255, 255, 0))
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'zombie:ball':
            game_world.remove_object(self)
        elif group == 'boy:ball':
            game_world.remove_object(self)

