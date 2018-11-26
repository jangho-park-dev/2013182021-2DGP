import random
import json
import os

from pico2d import *

import game_framework
import title_state
import high_grade_pause_state

name = "MainState"

RUN_SPEED = 50

enemy1 = [None for i in range(0, 5)]
enemy2 = [None for i in range(0, 5)]
enemy3 = [None for i in range(0, 5)]

grass = None
arrow = None
tower1 = None
tower2 = None
tower3 = None
font = None
first_time = 0

mouseFlag1 = [False for i in range(0, 30)]
mouseNum1 = 0
mouseXsave1 = [0 for i in range(0, 30)]
mouseYsave1 = [0 for i in range(0, 30)]

mouseFlag2 = [False for i in range(0, 30)]
mouseNum2 = 0
mouseXsave2 = [0 for i in range(0, 30)]
mouseYsave2 = [0 for i in range(0, 30)]

mouseFlag3 = [False for i in range(0, 30)]
mouseNum3 = 0
mouseXsave3 = [0 for i in range(0, 30)]
mouseYsave3 = [0 for i in range(0, 30)]

mouseX, mouseY = 0, 0


def enter():
    global enemy1, enemy2, enemy3, grass, arrow, tower1, tower2, tower3, first_time
    for i in range(0, 5):
        enemy1[i] = Enemy1()
    for i in range(0, 5):
        enemy2[i] = Enemy2()
    for i in range(0, 5):
        enemy3[i] = Enemy3()
    grass = Grass()
    arrow = Arrow()
    tower1 = Tower1()
    tower2 = Tower2()
    tower3 = Tower3()
    first_time = get_time()


class Grass:
    def __init__(self):
        self.image = load_image('Track2B.png')

    def draw(self):
        self.image.draw(480, 320)


class Enemy1:
    image = None

    def __init__(self):
        self.x, self.y = 100, 640
        self.frame = 0
        if Enemy1.image == None:
            Enemy1.image = load_image('Monsters.png')
        self.flag = [False for i in range(0, 14)]
        self.flag[0] = True
        self.time = get_time()
        self.timer = 0
        self.FRT = 0

    def get_bb(self):
        return self.x - 20, self.y - 25, self.x + 20, self.y + 25

    def update(self):
        self.frame = (self.frame + 1) % 2
        #delay(0.001)
        self.timer = get_time()
        self.FRT = self.timer - self.time
        #print(self.FRT)
        self.time = self.timer
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
        if self.flag[0]:
            if self.y >= 384:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[0] = False
                self.flag[1] = True

        if self.flag[1]:
            if self.x <= 220:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[1] = False
                self.flag[2] = True

        if self.flag[2]:
            if self.y >= 256:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[2] = False
                self.flag[3] = True

        if self.flag[3]:
            if self.x >= 100:
                self.x -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[3] = False
                self.flag[4] = True

        if self.flag[4]:
            if self.y >= 114:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[4] = False
                self.flag[5] = True

        if self.flag[5]:
            if self.x <= 333:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[5] = False
                self.flag[6] = True

        if self.flag[6]:
            if self.y <= 512:
                self.y += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[6] = False
                self.flag[7] = True

        if self.flag[7]:
            if self.x <= 580:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[7] = False
                self.flag[8] = True

        if self.flag[8]:
            if self.y >= 384:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[8] = False
                self.flag[9] = True

        if self.flag[9]:
            if self.x >= 456:
                self.x -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[9] = False
                self.flag[10] = True

        if self.flag[10]:
            if self.y >= 248:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[10] = False
                self.flag[11] = True

        if self.flag[11]:
            if self.x <= 564:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[11] = False
                self.flag[12] = True

        if self.flag[12]:
            if self.y >= 0:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[12] = False
                self.flag[0] = True
                self.x, self.y = 100, 640


    def draw(self):
        self.image.clip_draw(self.frame * 40, 0, 40, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())


class Enemy2:
    image = None

    def __init__(self):
        self.x, self.y = 100, 640
        self.frame = 0
        if Enemy2.image == None:
            Enemy2.image = load_image('Monsters.png')
        self.flag = [False for i in range(0, 14)]
        self.flag[0] = True

    def get_bb(self):
        return self.x - 20, self.y - 10, self.x + 10, self.y + 25

    def update(self):
        self.frame = (self.frame + 1) % 2
        #delay(0.001)
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
        if self.flag[0]:
            if self.y >= 384:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[0] = False
                self.flag[1] = True

        if self.flag[1]:
            if self.x <= 220:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[1] = False
                self.flag[2] = True

        if self.flag[2]:
            if self.y >= 256:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[2] = False
                self.flag[3] = True

        if self.flag[3]:
            if self.x >= 100:
                self.x -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[3] = False
                self.flag[4] = True

        if self.flag[4]:
            if self.y >= 114:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[4] = False
                self.flag[5] = True

        if self.flag[5]:
            if self.x <= 333:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[5] = False
                self.flag[6] = True

        if self.flag[6]:
            if self.y <= 512:
                self.y += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[6] = False
                self.flag[7] = True

        if self.flag[7]:
            if self.x <= 580:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[7] = False
                self.flag[8] = True

        if self.flag[8]:
            if self.y >= 384:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[8] = False
                self.flag[9] = True

        if self.flag[9]:
            if self.x >= 456:
                self.x -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[9] = False
                self.flag[10] = True

        if self.flag[10]:
            if self.y >= 248:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[10] = False
                self.flag[11] = True

        if self.flag[11]:
            if self.x <= 564:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[11] = False
                self.flag[12] = True

        if self.flag[12]:
            if self.y >= 0:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[12] = False
                self.flag[0] = True
                n = 0
                self.x, self.y = 100, 640


    def draw(self):
        self.image.clip_draw(self.frame * 40, 560, 40, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())


class Enemy3:
    image = None

    def __init__(self):
        self.x, self.y = 100, 640
        self.frame = 0
        if Enemy3.image == None:
            Enemy3.image = load_image('Monsters.png')
        self.flag = [False for i in range(0, 14)]
        self.flag[0] = True

    def get_bb(self):
        return self.x - 20, self.y - 15, self.x + 10, self.y + 15

    def update(self):
        self.frame = (self.frame + 1) % 2
        #delay(0.001)
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
        if self.flag[0]:
            if self.y >= 384:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[0] = False
                self.flag[1] = True

        if self.flag[1]:
            if self.x <= 220:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[1] = False
                self.flag[2] = True

        if self.flag[2]:
            if self.y >= 256:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[2] = False
                self.flag[3] = True

        if self.flag[3]:
            if self.x >= 100:
                self.x -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[3] = False
                self.flag[4] = True

        if self.flag[4]:
            if self.y >= 114:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[4] = False
                self.flag[5] = True

        if self.flag[5]:
            if self.x <= 333:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[5] = False
                self.flag[6] = True

        if self.flag[6]:
            if self.y <= 512:
                self.y += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[6] = False
                self.flag[7] = True

        if self.flag[7]:
            if self.x <= 580:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[7] = False
                self.flag[8] = True

        if self.flag[8]:
            if self.y >= 384:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[8] = False
                self.flag[9] = True

        if self.flag[9]:
            if self.x >= 456:
                self.x -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[9] = False
                self.flag[10] = True

        if self.flag[10]:
            if self.y >= 248:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[10] = False
                self.flag[11] = True

        if self.flag[11]:
            if self.x <= 564:
                self.x += 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[11] = False
                self.flag[12] = True

        if self.flag[12]:
            if self.y >= 0:
                self.y -= 1 * game_framework.frame_time * RUN_SPEED
            else:
                self.flag[12] = False
                self.flag[0] = True
                n = 0
                self.x, self.y = 100, 640


    def draw(self):
        self.image.clip_draw(self.frame * 40, 310, 40, 50, self.x, self.y)
        draw_rectangle(*self.get_bb())


class Arrow:
    def __init__(self):
        self.image = load_image('hand_arrow.png')

    def draw(self):
        self.image.draw_now(mouseX, mouseY)


class Tower1:

    def __init__(self):
        self.image = load_image('turret5.png')
        self.frame = 0
        self.x = [10000 for i in range(0, 30)]
        self.y = [10000 for i in range(0, 30)]

    def get_bb(self):
        return self.x[mouseNum1 - 1] - 50, self.y[mouseNum1 - 1] - 50,\
               self.x[mouseNum1 - 1] + 50, self.y[mouseNum1 - 1] + 50

    def update(self):
        self.frame = 2#(self.frame + 1) % 1
        self.x[mouseNum1 - 1] = mouseXsave1[mouseNum1 - 1]
        self.y[mouseNum1 - 1] = mouseYsave1[mouseNum1 - 1]

    def draw(self):
        for i in range(mouseNum1):
            self.image.clip_draw(self.frame * 32, 0, 32, 32, self.x[i], self.y[i])
            draw_rectangle(self.x[i] - 75, self.y[i] - 75, self.x[i] + 75, self.y[i] + 75)


class Tower2:
    def __init__(self):
        self.image = load_image('turret1.png')
        self.frame = 0
        self.x = [10000 for i in range(0, 30)]
        self.y = [10000 for i in range(0, 30)]

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.x[mouseNum2 - 1] = mouseXsave2[mouseNum2 - 1]
        self.y[mouseNum2 - 1] = mouseYsave2[mouseNum2 - 1]

    def draw(self):
        for i in range(mouseNum2):
            self.image.clip_draw(self.frame * 36, 200, 36, 40, mouseXsave2[i], mouseYsave2[i])
            draw_rectangle(self.x[i] - 75, self.y[i] - 75, self.x[i] + 75, self.y[i] + 75)


class Tower3:
    def __init__(self):
        self.image = load_image('turret1.png')
        self.frame = 0
        self.x = [10000 for i in range(0, 30)]
        self.y = [10000 for i in range(0, 30)]

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.x[mouseNum3 - 1] = mouseXsave3[mouseNum3 - 1]
        self.y[mouseNum3 - 1] = mouseYsave3[mouseNum3 - 1]

    def draw(self):
        for i in range(mouseNum3):
            self.image.clip_draw(self.frame * 36, 120, 36, 40, mouseXsave3[i], mouseYsave3[i])
            draw_rectangle(self.x[i] - 75, self.y[i] - 75, self.x[i] + 75, self.y[i] + 75)


def exit():
    global enemy1, enemy2, enemy3, tower1, tower2, tower3, grass
    for i in range(0, 5):
        del(enemy1[i])
    for i in range(0, 5):
        del(enemy2[i])
    for i in range(0, 5):
        del(enemy3[i])
    del(tower1)
    del(tower2)
    del(tower3)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    global mouseX, mouseY, mouseXsave1, mouseYsave1, mouseFlag1, mouseNum1
    global mouseXsave2, mouseYsave2, mouseFlag2, mouseNum2, mouseXsave3, mouseYsave3, mouseFlag3, mouseNum3
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
            if 660 <= event.x:
                if event.x <= 705:
                    if 175 <= event.y:
                        if event.y <= 245:
                            mouseFlag1[mouseNum1] = True
            if 718 <= event.x:
                if event.x <= 770:
                    if 175 <= event.y:
                        if event.y <= 245:
                            mouseFlag2[mouseNum2] = True
            if 782 <= event.x:
                if event.x <= 830:
                    if 175 <= event.y:
                        if event.y <= 245:
                            mouseFlag3[mouseNum3] = True


        elif event.type == SDL_MOUSEBUTTONUP:
            if mouseFlag1[mouseNum1]:
                mouseXsave1[mouseNum1], mouseYsave1[mouseNum1] = event.x, 640 - 1 - event.y
                print(mouseXsave1[mouseNum1], mouseYsave1[mouseNum1])
                mouseNum1 += 1
            elif mouseFlag2[mouseNum2]:
                mouseXsave2[mouseNum2], mouseYsave2[mouseNum2] = event.x, 640 - 1 - event.y
                print(mouseXsave2, mouseYsave2)
                mouseNum2 += 1
            elif mouseFlag3[mouseNum3]:
                mouseXsave3[mouseNum3], mouseYsave3[mouseNum3] = event.x, 640 - 1 - event.y
                print(mouseXsave3, mouseYsave3)
                mouseNum3 += 1
            else:
                pass


time = 0

def update():
    global time, first_time
    enemy1[0].update()
    time = get_time() - first_time
    #print(time)
    if time >= 1:
        enemy1[1].update()
    if time >= 2:
        enemy1[2].update()
    if time >= 3:
        enemy1[3].update()
    if time >= 4:
        enemy1[4].update()
    if time >= 5:
        enemy2[0].update()
    if time >= 6:
        enemy2[1].update()
    if time >= 7:
        enemy2[2].update()
    if time >= 8:
        enemy2[3].update()
    if time >= 9:
        enemy2[4].update()
    if time >= 10:
        enemy3[0].update()
    if time >= 11:
        enemy3[1].update()
    if time >= 12:
        enemy3[2].update()
    if time >= 13:
        enemy3[3].update()
    if time >= 14:
        enemy3[4].update()

    tower1.update()
    tower2.update()
    tower3.update()
    hide_cursor()


def draw():
    global time
    clear_canvas()
    grass.draw()
    enemy1[0].draw()
    if time >= 1:
        enemy1[1].draw()
    if time >= 2:
        enemy1[2].draw()
    if time >= 3:
        enemy1[3].draw()
    if time >= 4:
        enemy1[4].draw()
    if time >= 5:
        enemy2[0].draw()
    if time >= 6:
        enemy2[1].draw()
    if time >= 7:
        enemy2[2].draw()
    if time >= 8:
        enemy2[3].draw()
    if time >= 9:
        enemy2[4].draw()
    if time >= 10:
        enemy3[0].draw()
    if time >= 11:
        enemy3[1].draw()
    if time >= 12:
        enemy3[2].draw()
    if time >= 13:
        enemy3[3].draw()
    if time >= 14:
        enemy3[4].draw()
    arrow.draw()

    tower1.draw()
    tower2.draw()
    tower3.draw()
    update_canvas()





