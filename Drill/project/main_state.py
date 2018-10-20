import random
import json
import os

from pico2d import *

import game_framework
import title_state
import high_grade_pause_state

name = "MainState"

boy = None
grass = None
arrow = None
tower1 = None
font = None

flag = [False for i in range(0, 14)]
flag[0] = True

mouseX, mouseY = 0, 0
mouseXsave, mouseYsave = 0, 0


class Grass:
    def __init__(self):
        self.image = load_image('Track2B.png')

    def draw(self):
        self.image.draw(480, 320)


class Boy:
    global flag

    def __init__(self):
        self.x, self.y = 100, 640
        self.frame = 0
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        delay(0.01)
        # enemy location set
        # 1. y == 384  y--
        # 2. x == 220  x++
        # 3. y == 256  y--
        # 4. x == 100  x--
        # 5. y == 114  y--
        # 6. x == 333  x++
        # 7. y == 512  y++
        # 8. x == 580  x++
        # 9. y == 384  y--
        # 10. x == 456  x--
        # 11. y == 248  y--
        # 12. x == 564  x++
        # 13. y == 0  y--
        if flag[0]:
            if self.y >= 384:
                self.y -= 1
            else:
                flag[0] = False
                flag[1] = True

        if flag[1]:
            if self.x <= 220:
                self.x += 1
            else:
                flag[1] = False
                flag[2] = True

        if flag[2]:
            if self.y >= 256:
                self.y -= 1
            else:
                flag[2] = False
                flag[3] = True

        if flag[3]:
            if self.x >= 100:
                self.x -= 1
            else:
                flag[3] = False
                flag[4] = True

        if flag[4]:
            if self.y >= 114:
                self.y -= 1
            else:
                flag[4] = False
                flag[5] = True

        if flag[5]:
            if self.x <= 333:
                self.x += 1
            else:
                flag[5] = False
                flag[6] = True

        if flag[6]:
            if self.y <= 512:
                self.y += 1
            else:
                flag[6] = False
                flag[7] = True

        if flag[7]:
            if self.x <= 580:
                self.x += 1
            else:
                flag[7] = False
                flag[8] = True

        if flag[8]:
            if self.y >= 384:
                self.y -= 1
            else:
                flag[8] = False
                flag[9] = True

        if flag[9]:
            if self.x >= 456:
                self.x -= 1
            else:
                flag[9] = False
                flag[10] = True

        if flag[10]:
            if self.y >= 248:
                self.y -= 1
            else:
                flag[10] = False
                flag[11] = True

        if flag[11]:
            if self.x <= 564:
                self.x += 1
            else:
                flag[11] = False
                flag[12] = True

        if flag[12]:
            if self.y >= 0:
                self.y -= 1
            else:
                flag[12] = False
                flag[0] = True
                n = 0
                self.x, self.y = 100, 640


    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class Arrow:
    def __init__(self):
        self.image = load_image('hand_arrow.png')

    def draw(self):
        self.image.draw_now(mouseX, mouseY)


class Tower1:
    def __init__(self):
        self.image = load_image('turret5.png')

    def draw(self):
        self.image.draw_now(mouseXsave, mouseYsave)

def enter():
    global boy, grass, arrow, tower1
    boy = Boy()
    grass = Grass()
    arrow = Arrow()
    tower1 = Tower1()


def exit():
    global boy, grass
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    global mouseX, mouseY, mouseXsave, mouseYsave
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(high_grade_pause_state)
        elif event.type == SDL_MOUSEMOTION:
            mouseX, mouseY = event.x + 25, 640 - 1 - event.y - 25
        elif event.type == SDL_MOUSEBUTTONDOWN:
            print(123)
            if 660 <= event.x:
                if event.x <= 705:
                    if 175 <= event.y:
                        if event.y <= 245:
                            mouseXsave, mouseYsave = event.x, 640 - 1 - event.y
                            print(mouseXsave, mouseYsave)
        elif event.type == SDL_MOUSEBUTTONUP:
            pass


def update():
    boy.update()
    hide_cursor()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    arrow.draw()
    tower1.draw()
    update_canvas()





