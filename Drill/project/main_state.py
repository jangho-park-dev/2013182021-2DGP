import random
import json
import os

from pico2d import *

import game_framework
import title_state
import high_grade_pause_state

name = "MainState"

enemy1 = None
enemy2 = None
enemy3 = None
grass = None
arrow = None
tower1 = None
tower2 = None
tower3 = None
font = None


flag = [False for i in range(0, 14)]
flag[0] = True

flag2 = [False for i in range(0, 14)]
flag2[0] = True

flag3 = [False for i in range(0, 14)]
flag3[0] = True

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


class Grass:
    def __init__(self):
        self.image = load_image('Track2B.png')

    def draw(self):
        self.image.draw(480, 320)


class Enemy1:
    global flag

    def __init__(self):
        self.x, self.y = 100, 640
        self.frame = 0
        self.image = load_image('Monsters.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        delay(0.005)
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
        #self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        self.image.clip_draw(self.frame * 40, 0, 40, 50, self.x, self.y)


class Enemy2:
    global flag2

    def __init__(self):
        self.x, self.y = 100, 700
        self.frame = 0
        self.image = load_image('Monsters.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        delay(0.005)
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
        if flag2[0]:
            if self.y >= 384:
                self.y -= 1
            else:
                flag2[0] = False
                flag2[1] = True

        if flag2[1]:
            if self.x <= 220:
                self.x += 1
            else:
                flag2[1] = False
                flag2[2] = True

        if flag2[2]:
            if self.y >= 256:
                self.y -= 1
            else:
                flag2[2] = False
                flag2[3] = True

        if flag2[3]:
            if self.x >= 100:
                self.x -= 1
            else:
                flag2[3] = False
                flag2[4] = True

        if flag2[4]:
            if self.y >= 114:
                self.y -= 1
            else:
                flag2[4] = False
                flag2[5] = True

        if flag2[5]:
            if self.x <= 333:
                self.x += 1
            else:
                flag2[5] = False
                flag2[6] = True

        if flag2[6]:
            if self.y <= 512:
                self.y += 1
            else:
                flag2[6] = False
                flag2[7] = True

        if flag2[7]:
            if self.x <= 580:
                self.x += 1
            else:
                flag2[7] = False
                flag2[8] = True

        if flag2[8]:
            if self.y >= 384:
                self.y -= 1
            else:
                flag2[8] = False
                flag2[9] = True

        if flag2[9]:
            if self.x >= 456:
                self.x -= 1
            else:
                flag2[9] = False
                flag2[10] = True

        if flag2[10]:
            if self.y >= 248:
                self.y -= 1
            else:
                flag2[10] = False
                flag2[11] = True

        if flag2[11]:
            if self.x <= 564:
                self.x += 1
            else:
                flag2[11] = False
                flag2[12] = True

        if flag2[12]:
            if self.y >= 0:
                self.y -= 1
            else:
                flag2[12] = False
                flag2[0] = True
                n = 0
                self.x, self.y = 100, 640


    def draw(self):
        self.image.clip_draw(self.frame * 40, 560, 40, 50, self.x, self.y)


class Enemy3:
    global flag3

    def __init__(self):
        self.x, self.y = 100, 760
        self.frame = 0
        self.image = load_image('Monsters.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        delay(0.005)
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
        if flag3[0]:
            if self.y >= 384:
                self.y -= 1
            else:
                flag3[0] = False
                flag3[1] = True

        if flag3[1]:
            if self.x <= 220:
                self.x += 1
            else:
                flag3[1] = False
                flag3[2] = True

        if flag3[2]:
            if self.y >= 256:
                self.y -= 1
            else:
                flag3[2] = False
                flag3[3] = True

        if flag3[3]:
            if self.x >= 100:
                self.x -= 1
            else:
                flag3[3] = False
                flag3[4] = True

        if flag3[4]:
            if self.y >= 114:
                self.y -= 1
            else:
                flag3[4] = False
                flag3[5] = True

        if flag3[5]:
            if self.x <= 333:
                self.x += 1
            else:
                flag3[5] = False
                flag3[6] = True

        if flag3[6]:
            if self.y <= 512:
                self.y += 1
            else:
                flag3[6] = False
                flag3[7] = True

        if flag3[7]:
            if self.x <= 580:
                self.x += 1
            else:
                flag3[7] = False
                flag3[8] = True

        if flag3[8]:
            if self.y >= 384:
                self.y -= 1
            else:
                flag3[8] = False
                flag3[9] = True

        if flag3[9]:
            if self.x >= 456:
                self.x -= 1
            else:
                flag3[9] = False
                flag3[10] = True

        if flag3[10]:
            if self.y >= 248:
                self.y -= 1
            else:
                flag3[10] = False
                flag3[11] = True

        if flag3[11]:
            if self.x <= 564:
                self.x += 1
            else:
                flag3[11] = False
                flag3[12] = True

        if flag3[12]:
            if self.y >= 0:
                self.y -= 1
            else:
                flag3[12] = False
                flag3[0] = True
                n = 0
                self.x, self.y = 100, 640


    def draw(self):
        self.image.clip_draw(self.frame * 40, 310, 40, 50, self.x, self.y)


class Arrow:
    def __init__(self):
        self.image = load_image('hand_arrow.png')

    def draw(self):
        self.image.draw_now(mouseX, mouseY)


class Tower1:
    def __init__(self):
        self.image = load_image('turret5.png')
        self.frame = 0

    def update(self):
        self.frame = 2#(self.frame + 1) % 1


    def draw(self):
        for i in range(mouseNum1):
            self.image.clip_draw(self.frame * 32, 0, 32, 32, mouseXsave1[i], mouseYsave1[i])


class Tower2:
    def __init__(self):
        self.image = load_image('turret1.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 1


    def draw(self):
        for i in range(mouseNum2):
            self.image.clip_draw(self.frame * 36, 200, 36, 40, mouseXsave2[i], mouseYsave2[i])


class Tower3:
    def __init__(self):
        self.image = load_image('turret1.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 1


    def draw(self):
        for i in range(mouseNum3):
            self.image.clip_draw(self.frame * 36, 120, 36, 40, mouseXsave3[i], mouseYsave3[i])


def enter():
    global enemy1, enemy2, enemy3, grass, arrow, tower1, tower2, tower3
    enemy1 = Enemy1()
    enemy2 = Enemy2()
    enemy3 = Enemy3()
    grass = Grass()
    arrow = Arrow()
    tower1 = Tower1()
    tower2 = Tower2()
    tower3 = Tower3()


def exit():
    global enemy1, enemy2, enemy3, tower1, tower2, tower3, grass
    del(enemy1)
    del(enemy2)
    del(enemy3)
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
                            print(mouseXsave1[mouseNum1], mouseYsave1[mouseNum1])
            if 718 <= event.x:
                if event.x <= 770:
                    if 175 <= event.y:
                        if event.y <= 245:
                            mouseFlag2[mouseNum2] = True
                            print(mouseXsave2[mouseNum2], mouseYsave2[mouseNum2])
            if 782 <= event.x:
                if event.x <= 830:
                    if 175 <= event.y:
                        if event.y <= 245:
                            mouseFlag3[mouseNum3] = True
                            print(mouseXsave3[mouseNum3], mouseYsave3[mouseNum3])


        elif event.type == SDL_MOUSEBUTTONUP:
            if mouseFlag1[mouseNum1]:
                mouseXsave1[mouseNum1], mouseYsave1[mouseNum1] = event.x, 640 - 1 - event.y
                print(mouseXsave1, mouseYsave1)
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


def update():
    enemy1.update()
    enemy2.update()
    enemy3.update()
    tower1.update()
    tower2.update()
    tower3.update()
    hide_cursor()


def draw():
    clear_canvas()
    grass.draw()
    enemy1.draw()
    enemy2.draw()
    enemy3.draw()
    arrow.draw()
    tower1.draw()
    tower2.draw()
    tower3.draw()
    update_canvas()





