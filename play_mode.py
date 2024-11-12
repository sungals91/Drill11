import random

from pico2d import *
import game_framework

import game_world
from game_world import add_collision_pair
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    #global balls

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    balls = [Ball(random.randint(100, 1500), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1) # 게임 월드에 추가.

    # 충돌 대상물을 등록해주기
    add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        add_collision_pair('boy:ball', None, ball)
        # boy가 반복되면 비효율적

    # 딕셔너리의 구조
    # {'boy:ball' : [ [boy], [ball1, ball2, ... , ball30] ]

    # zombie 생성
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)
    # 충돌 대상물 등록
    for zombie in zombies:
        add_collision_pair('zombie:ball', zombie, None)
    # boy:zombie 충돌 대상물 등록
    add_collision_pair('boy:zombie', boy, None)
    for zombie in zombies:
        add_collision_pair('boy:zombie', None, zombie)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # 객체들의 위치가 다 결정됨. 따라서 이어서 충돌 검사를 실행
    # fill here
    game_world.handle_collisions()
    '''
    for ball in balls.copy():
        if game_world.collide(boy, ball):
            print('COLLISION boy:ball')
            boy.ball_count += 1
            game_world.remove_object(ball) # 게임월드에서 ball 삭제 but, balls 리스트에 볼은 남아있음
            balls.remove(ball) # 좋지 않은 표현 -> balls 리스트를 balls.copy()로
    '''
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

