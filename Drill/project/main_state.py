import random
import json
import os

from pico2d import *

import game_framework
import title_state
import high_grade_pause_state

name = "MainState"

RUN_SPEED = 150

enemy1 = [None for i in range(0, 100)]
enemy2 = [None for i in range(0, 100)]
enemy3 = [None for i in range(0, 100)]
bullet = None
bullet2 = None
bullet3 = None
bullet4 = None
bullet5 = None
bullet6 = None
bulletNum1 = 0

grass = None
arrow = None
tower1 = None
tower2 = None
tower3 = None
font = None
first_time = 0
start_time = 0
stage = 0


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
    global bullet, bullet2, bullet3, bullet4, bullet5, bullet6
    for i in range(0, 100):
        enemy1[i] = Enemy1()
    for i in range(0, 100):
        enemy2[i] = Enemy2()
    for i in range(0, 100):
        enemy3[i] = Enemy3()
    bullet = Bullet()
    bullet2 = Bullet2()
    bullet3 = Bullet3()
    bullet4 = Bullet4()
    bullet5 = Bullet5()
    bullet6 = Bullet6()
    grass = Grass()
    arrow = Arrow()
    tower1 = Tower1()
    tower2 = Tower2()
    tower3 = Tower3()
    first_time = get_time()


class Grass:
    def __init__(self):
        self.image = load_image('Track2B.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 100
        self.gold = 100
        self.bgm = load_music('map.mid')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        global stage
        self.image.draw(480, 320)
        #self.font.draw(440, 615, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        self.font.draw(700, 615, '%3.2f' % self.hp, (255, 0, 0))
        self.font.draw(700, 560, '%3.2f' % self.gold, (255, 255, 0))
        self.font.draw(480, 620, 'stage : %3d' % stage, (0, 0, 0))


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

    def collide(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[0] + 75: return False
        if right_a < mouseXsave1[0] - 75: return False
        if top_a < mouseYsave1[0] - 75: return False
        if bottom_a > mouseYsave1[0] + 75: return False

        return True

    def collide2(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[1] + 75: return False
        if right_a < mouseXsave1[1] - 75: return False
        if top_a < mouseYsave1[1] - 75: return False
        if bottom_a > mouseYsave1[1] + 75: return False

        return True

    def collide3(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[2] + 75: return False
        if right_a < mouseXsave1[2] - 75: return False
        if top_a < mouseYsave1[2] - 75: return False
        if bottom_a > mouseYsave1[2] + 75: return False

        return True

    def collide_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[0] + 75: return False
        if right_a < mouseXsave2[0] - 75: return False
        if top_a < mouseYsave2[0] - 75: return False
        if bottom_a > mouseYsave2[0] + 75: return False

        return True

    def collide2_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[1] + 75: return False
        if right_a < mouseXsave2[1] - 75: return False
        if top_a < mouseYsave2[1] - 75: return False
        if bottom_a > mouseYsave2[1] + 75: return False

        return True

    def collide3_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[2] + 75: return False
        if right_a < mouseXsave2[2] - 75: return False
        if top_a < mouseYsave2[2] - 75: return False
        if bottom_a > mouseYsave2[2] + 75: return False

        return True

    def collide_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[0] + 75: return False
        if right_a < mouseXsave3[0] - 75: return False
        if top_a < mouseYsave3[0] - 75: return False
        if bottom_a > mouseYsave3[0] + 75: return False

        return True

    def collide2_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[1] + 75: return False
        if right_a < mouseXsave3[1] - 75: return False
        if top_a < mouseYsave3[1] - 75: return False
        if bottom_a > mouseYsave3[1] + 75: return False

        return True

    def collide3_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[2] + 75: return False
        if right_a < mouseXsave3[2] - 75: return False
        if top_a < mouseYsave3[2] - 75: return False
        if bottom_a > mouseYsave3[2] + 75: return False

        return True

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

    def collide(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[0] + 75: return False
        if right_a < mouseXsave1[0] - 75: return False
        if top_a < mouseYsave1[0] - 75: return False
        if bottom_a > mouseYsave1[0] + 75: return False

        return True

    def collide2(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[1] + 75: return False
        if right_a < mouseXsave1[1] - 75: return False
        if top_a < mouseYsave1[1] - 75: return False
        if bottom_a > mouseYsave1[1] + 75: return False

        return True

    def collide3(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[2] + 75: return False
        if right_a < mouseXsave1[2] - 75: return False
        if top_a < mouseYsave1[2] - 75: return False
        if bottom_a > mouseYsave1[2] + 75: return False

        return True

    def collide_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[0] + 75: return False
        if right_a < mouseXsave2[0] - 75: return False
        if top_a < mouseYsave2[0] - 75: return False
        if bottom_a > mouseYsave2[0] + 75: return False

        return True

    def collide2_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[1] + 75: return False
        if right_a < mouseXsave2[1] - 75: return False
        if top_a < mouseYsave2[1] - 75: return False
        if bottom_a > mouseYsave2[1] + 75: return False

        return True

    def collide3_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[2] + 75: return False
        if right_a < mouseXsave2[2] - 75: return False
        if top_a < mouseYsave2[2] - 75: return False
        if bottom_a > mouseYsave2[2] + 75: return False

        return True

    def collide_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[0] + 75: return False
        if right_a < mouseXsave3[0] - 75: return False
        if top_a < mouseYsave3[0] - 75: return False
        if bottom_a > mouseYsave3[0] + 75: return False

        return True

    def collide2_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[1] + 75: return False
        if right_a < mouseXsave3[1] - 75: return False
        if top_a < mouseYsave3[1] - 75: return False
        if bottom_a > mouseYsave3[1] + 75: return False

        return True

    def collide3_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[2] + 75: return False
        if right_a < mouseXsave3[2] - 75: return False
        if top_a < mouseYsave3[2] - 75: return False
        if bottom_a > mouseYsave3[2] + 75: return False

        return True

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

    def collide(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[0] + 75: return False
        if right_a < mouseXsave1[0] - 75: return False
        if top_a < mouseYsave1[0] - 75: return False
        if bottom_a > mouseYsave1[0] + 75: return False

        return True

    def collide2(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[1] + 75: return False
        if right_a < mouseXsave1[1] - 75: return False
        if top_a < mouseYsave1[1] - 75: return False
        if bottom_a > mouseYsave1[1] + 75: return False

        return True

    def collide3(self):
        if mouseNum1 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave1[2] + 75: return False
        if right_a < mouseXsave1[2] - 75: return False
        if top_a < mouseYsave1[2] - 75: return False
        if bottom_a > mouseYsave1[2] + 75: return False

        return True

    def collide_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[0] + 75: return False
        if right_a < mouseXsave2[0] - 75: return False
        if top_a < mouseYsave2[0] - 75: return False
        if bottom_a > mouseYsave2[0] + 75: return False

        return True

    def collide2_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[1] + 75: return False
        if right_a < mouseXsave2[1] - 75: return False
        if top_a < mouseYsave2[1] - 75: return False
        if bottom_a > mouseYsave2[1] + 75: return False

        return True

    def collide3_1(self):
        if mouseNum2 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave2[2] + 75: return False
        if right_a < mouseXsave2[2] - 75: return False
        if top_a < mouseYsave2[2] - 75: return False
        if bottom_a > mouseYsave2[2] + 75: return False

        return True

    def collide_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[0] + 75: return False
        if right_a < mouseXsave3[0] - 75: return False
        if top_a < mouseYsave3[0] - 75: return False
        if bottom_a > mouseYsave3[0] + 75: return False

        return True

    def collide2_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[1] + 75: return False
        if right_a < mouseXsave3[1] - 75: return False
        if top_a < mouseYsave3[1] - 75: return False
        if bottom_a > mouseYsave3[1] + 75: return False

        return True

    def collide3_2(self):
        if mouseNum3 == 0:
            return False
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if left_a > mouseXsave3[2] + 75: return False
        if right_a < mouseXsave3[2] - 75: return False
        if top_a < mouseYsave3[2] - 75: return False
        if bottom_a > mouseYsave3[2] + 75: return False

        return True

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


class Bullet:
    def __init__(self):
        self.image = load_image('bullet.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.enemy_x = [0 for i in range(20)]
        self.enemy_y = [0 for i in range(20)]
        self.flag1 = 1
        self.dir = 0
        self.speed = 0
        self.time = 0
        self.cld1 = 0

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def setEnemy1List(self, enemy1):
        for i in range(0, 20):
            self.enemy_x[i] = enemy1[i].x
            self.enemy_y[i] = enemy1[i].y

    def setEnemy2List(self, enemy2):
        for i in range(0, 20):
            self.enemy_x[i] = enemy2[i].x
            self.enemy_y[i] = enemy2[i].y

    def setEnemy3List(self, enemy3):
        for i in range(0, 20):
            self.enemy_x[i] = enemy3[i].x
            self.enemy_y[i] = enemy3[i].y

    def collide_1(self):
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if self.cld1 == 0:
            if left_a > self.enemy_x[0] + 20: return False
            if right_a < self.enemy_x[0] - 20: return False
            if top_a < self.enemy_y[0] - 25: return False
            if bottom_a > self.enemy_y[0] + 25: return False
        if self.cld1 == 1:
            if left_a > self.enemy_x[1] + 20: return False
            if right_a < self.enemy_x[1] - 20: return False
            if top_a < self.enemy_y[1] - 25: return False
            if bottom_a > self.enemy_y[1] + 25: return False
        if self.cld1 == 2:
            if left_a > self.enemy_x[2] + 20: return False
            if right_a < self.enemy_x[2] - 20: return False
            if top_a < self.enemy_y[2] - 25: return False
            if bottom_a > self.enemy_y[2] + 25: return False
        if self.cld1 == 3:
            if left_a > self.enemy_x[3] + 20: return False
            if right_a < self.enemy_x[3] - 20: return False
            if top_a < self.enemy_y[3] - 25: return False
            if bottom_a > self.enemy_y[3] + 25: return False
        if self.cld1 == 4:
            if left_a > self.enemy_x[4] + 20: return False
            if right_a < self.enemy_x[4] - 20: return False
            if top_a < self.enemy_y[4] - 25: return False
            if bottom_a > self.enemy_y[4] + 25: return False
        if self.cld1 == 5:
            if left_a > self.enemy_x[5] + 20: return False
            if right_a < self.enemy_x[5] - 20: return False
            if top_a < self.enemy_y[5] - 25: return False
            if bottom_a > self.enemy_y[5] + 25: return False
        if self.cld1 == 6:
            if left_a > self.enemy_x[6] + 20: return False
            if right_a < self.enemy_x[6] - 20: return False
            if top_a < self.enemy_y[6] - 25: return False
            if bottom_a > self.enemy_y[6] + 25: return False
        if self.cld1 == 7:
            if left_a > self.enemy_x[7] + 20: return False
            if right_a < self.enemy_x[7] - 20: return False
            if top_a < self.enemy_y[7] - 25: return False
            if bottom_a > self.enemy_y[7] + 25: return False
        if self.cld1 == 8:
            if left_a > self.enemy_x[8] + 20: return False
            if right_a < self.enemy_x[8] - 20: return False
            if top_a < self.enemy_y[8] - 25: return False
            if bottom_a > self.enemy_y[8] + 25: return False
        if self.cld1 == 9:
            if left_a > self.enemy_x[9] + 20: return False
            if right_a < self.enemy_x[9] - 20: return False
            if top_a < self.enemy_y[9] - 25: return False
            if bottom_a > self.enemy_y[9] + 25: return False
        if self.cld1 == 10:
            if left_a > self.enemy_x[10] + 20: return False
            if right_a < self.enemy_x[10] - 20: return False
            if top_a < self.enemy_y[10] - 25: return False
            if bottom_a > self.enemy_y[10] + 25: return False
        if self.cld1 == 11:
            if left_a > self.enemy_x[11] + 20: return False
            if right_a < self.enemy_x[11] - 20: return False
            if top_a < self.enemy_y[11] - 25: return False
            if bottom_a > self.enemy_y[11] + 25: return False
        if self.cld1 == 12:
            if left_a > self.enemy_x[12] + 20: return False
            if right_a < self.enemy_x[12] - 20: return False
            if top_a < self.enemy_y[12] - 25: return False
            if bottom_a > self.enemy_y[12] + 25: return False
        if self.cld1 == 13:
            if left_a > self.enemy_x[13] + 20: return False
            if right_a < self.enemy_x[13] - 20: return False
            if top_a < self.enemy_y[13] - 25: return False
            if bottom_a > self.enemy_y[13] + 25: return False
        if self.cld1 == 14:
            if left_a > self.enemy_x[14] + 20: return False
            if right_a < self.enemy_x[14] - 20: return False
            if top_a < self.enemy_y[14] - 25: return False
            if bottom_a > self.enemy_y[14] + 25: return False
        if self.cld1 == 15:
            if left_a > self.enemy_x[15] + 20: return False
            if right_a < self.enemy_x[15] - 20: return False
            if top_a < self.enemy_y[15] - 25: return False
            if bottom_a > self.enemy_y[15] + 25: return False
        if self.cld1 == 16:
            if left_a > self.enemy_x[16] + 20: return False
            if right_a < self.enemy_x[16] - 20: return False
            if top_a < self.enemy_y[16] - 25: return False
            if bottom_a > self.enemy_y[16] + 25: return False
        if self.cld1 == 17:
            if left_a > self.enemy_x[17] + 20: return False
            if right_a < self.enemy_x[17] - 20: return False
            if top_a < self.enemy_y[17] - 25: return False
            if bottom_a > self.enemy_y[17] + 25: return False
        if self.cld1 == 18:
            if left_a > self.enemy_x[18] + 20: return False
            if right_a < self.enemy_x[18] - 20: return False
            if top_a < self.enemy_y[18] - 25: return False
            if bottom_a > self.enemy_y[18] + 25: return False
        if self.cld1 == 19:
            if left_a > self.enemy_x[19] + 20: return False
            if right_a < self.enemy_x[19] - 20: return False
            if top_a < self.enemy_y[19] - 25: return False
            if bottom_a > self.enemy_y[19] + 25: return False

        return True

    def update(self):
        global bulletNum1
        self.frame = (self.frame + 1) % 1
        if stage == 1:
            self.setEnemy1List(enemy1)
        if stage == 2:
            self.setEnemy1List(enemy1)
        if stage == 3:
            self.setEnemy2List(enemy2)
        if stage == 4:
            self.setEnemy2List(enemy2)
        if stage == 5:
            self.setEnemy3List(enemy3)
        if stage == 6:
            self.setEnemy3List(enemy3)

        if self.flag1:
            self.x = mouseXsave1[0]
            self.y = mouseYsave1[0]
            print(self.x, self.y)
            self.flag1 = 0

        self.speed = 96

        if self.cld1 == 0:
            self.dir = math.atan2(self.enemy_y[0] - self.y, self.enemy_x[0] - self.x)
        if self.cld1 == 1:
            self.dir = math.atan2(self.enemy_y[1] - self.y, self.enemy_x[1] - self.x)
        if self.cld1 == 2:
            self.dir = math.atan2(self.enemy_y[2] - self.y, self.enemy_x[2] - self.x)
        if self.cld1 == 3:
            self.dir = math.atan2(self.enemy_y[3] - self.y, self.enemy_x[3] - self.x)
        if self.cld1 == 4:
            self.dir = math.atan2(self.enemy_y[4] - self.y, self.enemy_x[4] - self.x)
        if self.cld1 == 5:
            self.dir = math.atan2(self.enemy_y[5] - self.y, self.enemy_x[5] - self.x)
        if self.cld1 == 6:
            self.dir = math.atan2(self.enemy_y[6] - self.y, self.enemy_x[6] - self.x)
        if self.cld1 == 7:
            self.dir = math.atan2(self.enemy_y[7] - self.y, self.enemy_x[7] - self.x)
        if self.cld1 == 8:
            self.dir = math.atan2(self.enemy_y[8] - self.y, self.enemy_x[8] - self.x)
        if self.cld1 == 9:
            self.dir = math.atan2(self.enemy_y[9] - self.y, self.enemy_x[9] - self.x)
        if self.cld1 == 10:
            self.dir = math.atan2(self.enemy_y[10] - self.y, self.enemy_x[10] - self.x)
        if self.cld1 == 11:
            self.dir = math.atan2(self.enemy_y[11] - self.y, self.enemy_x[11] - self.x)
        if self.cld1 == 12:
            self.dir = math.atan2(self.enemy_y[12] - self.y, self.enemy_x[12] - self.x)
        if self.cld1 == 13:
            self.dir = math.atan2(self.enemy_y[13] - self.y, self.enemy_x[13] - self.x)
        if self.cld1 == 14:
            self.dir = math.atan2(self.enemy_y[14] - self.y, self.enemy_x[14] - self.x)
        if self.cld1 == 15:
            self.dir = math.atan2(self.enemy_y[15] - self.y, self.enemy_x[15] - self.x)
        if self.cld1 == 16:
            self.dir = math.atan2(self.enemy_y[16] - self.y, self.enemy_x[16] - self.x)
        if self.cld1 == 17:
            self.dir = math.atan2(self.enemy_y[17] - self.y, self.enemy_x[17] - self.x)
        if self.cld1 == 18:
            self.dir = math.atan2(self.enemy_y[18] - self.y, self.enemy_x[18] - self.x)
        if self.cld1 == 19:
            self.dir = math.atan2(self.enemy_y[19] - self.y, self.enemy_x[19] - self.x)

        self.time = game_framework.frame_time
        #print(self.time)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.collide_1():
            if self.cld1 == 0:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[0].x = 100000000
                enemy1[0].y = 100000000
                enemy2[0].x = 100000000
                enemy2[0].y = 100000000
                enemy3[0].x = 100000000
                enemy3[0].y = 100000000
                bullet.cld1 = 1
                bullet2.cld1 = 1
                bullet3.cld1 = 1
                bullet4.cld1 = 1
                bullet5.cld1 = 1
                bullet6.cld1 = 1
                bulletNum1 = 1
                grass.gold += 10
            elif self.cld1 == 1:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[1].x = 100000000
                enemy1[1].y = 100000000
                enemy2[1].x = 100000000
                enemy2[1].y = 100000000
                enemy3[1].x = 100000000
                enemy3[1].y = 100000000
                bullet.cld1 = 2
                bullet2.cld1 = 2
                bullet3.cld1 = 2
                bullet4.cld1 = 2
                bullet5.cld1 = 2
                bullet6.cld1 = 2
                bulletNum1 = 2
                grass.gold += 10
            elif self.cld1 == 2:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[2].x = 100000000
                enemy1[2].y = 100000000
                enemy2[2].x = 100000000
                enemy2[2].y = 100000000
                enemy3[2].x = 100000000
                enemy3[2].y = 100000000
                bullet.cld1 = 3
                bullet2.cld1 = 3
                bullet3.cld1 = 3
                bullet4.cld1 = 3
                bullet5.cld1 = 3
                bullet6.cld1 = 3
                bulletNum1 = 3
                grass.gold += 10
            elif self.cld1 == 3:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[3].x = 100000000
                enemy1[3].y = 100000000
                enemy2[3].x = 100000000
                enemy2[3].y = 100000000
                enemy3[3].x = 100000000
                enemy3[3].y = 100000000
                bullet.cld1 = 4
                bullet2.cld1 = 4
                bullet3.cld1 = 4
                bullet4.cld1 = 4
                bullet5.cld1 = 4
                bullet6.cld1 = 4
                bulletNum1 = 4
                grass.gold += 10
            elif self.cld1 == 4:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[4].x = 100000000
                enemy1[4].y = 100000000
                enemy2[4].x = 100000000
                enemy2[4].y = 100000000
                enemy3[4].x = 100000000
                enemy3[4].y = 100000000
                bullet.cld1 = 5
                bullet2.cld1 = 5
                bullet3.cld1 = 5
                bullet4.cld1 = 5
                bullet5.cld1 = 5
                bullet6.cld1 = 5
                bulletNum1 = 5
                grass.gold += 10
            elif self.cld1 == 5:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[5].x = 100000000
                enemy1[5].y = 100000000
                enemy2[5].x = 100000000
                enemy2[5].y = 100000000
                enemy3[5].x = 100000000
                enemy3[5].y = 100000000
                bullet.cld1 = 6
                bullet2.cld1 = 6
                bullet3.cld1 = 6
                bullet4.cld1 = 6
                bullet5.cld1 = 6
                bullet6.cld1 = 6
                bulletNum1 = 6
                grass.gold += 10
            elif self.cld1 == 6:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[6].x = 100000000
                enemy1[6].y = 100000000
                enemy2[6].x = 100000000
                enemy2[6].y = 100000000
                enemy3[6].x = 100000000
                enemy3[6].y = 100000000
                bullet.cld1 = 7
                bullet2.cld1 = 7
                bullet3.cld1 = 7
                bullet4.cld1 = 7
                bullet5.cld1 = 7
                bullet6.cld1 = 7
                bulletNum1 = 7
                grass.gold += 10
            elif self.cld1 == 7:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[7].x = 100000000
                enemy1[7].y = 100000000
                enemy2[7].x = 100000000
                enemy2[7].y = 100000000
                enemy3[7].x = 100000000
                enemy3[7].y = 100000000
                bullet.cld1 = 8
                bullet2.cld1 = 8
                bullet3.cld1 = 8
                bullet4.cld1 = 8
                bullet5.cld1 = 8
                bullet6.cld1 = 1
                bulletNum1 = 8
                grass.gold += 10
            elif self.cld1 == 8:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[8].x = 100000000
                enemy1[8].y = 100000000
                enemy2[8].x = 100000000
                enemy2[8].y = 100000000
                enemy3[8].x = 100000000
                enemy3[8].y = 100000000
                bullet.cld1 = 9
                bullet2.cld1 = 9
                bullet3.cld1 = 9
                bullet4.cld1 = 9
                bullet5.cld1 = 9
                bullet6.cld1 = 9
                bulletNum1 = 9
                grass.gold += 10
            elif self.cld1 == 9:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[9].x = 100000000
                enemy1[9].y = 100000000
                enemy2[9].x = 100000000
                enemy2[9].y = 100000000
                enemy3[9].x = 100000000
                enemy3[9].y = 100000000
                bullet.cld1 = 10
                bullet2.cld1 = 10
                bullet3.cld1 = 10
                bullet4.cld1 = 10
                bullet5.cld1 = 10
                bullet6.cld1 = 10
                bulletNum1 = 10
                grass.gold += 10
            elif self.cld1 == 10:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[10].x = 100000000
                enemy1[10].y = 100000000
                enemy2[10].x = 100000000
                enemy2[10].y = 100000000
                enemy3[10].x = 100000000
                enemy3[10].y = 100000000
                bullet.cld1 = 11
                bullet2.cld1 = 11
                bullet3.cld1 = 11
                bullet4.cld1 = 11
                bullet5.cld1 = 11
                bullet6.cld1 = 11
                bulletNum1 = 11
                grass.gold += 10
            elif self.cld1 == 11:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[11].x = 100000000
                enemy1[11].y = 100000000
                enemy2[11].x = 100000000
                enemy2[11].y = 100000000
                enemy3[11].x = 100000000
                enemy3[11].y = 100000000
                bullet.cld1 = 12
                bullet2.cld1 = 12
                bullet3.cld1 = 12
                bullet4.cld1 = 12
                bullet5.cld1 = 12
                bullet6.cld1 = 12
                bulletNum1 = 2
                grass.gold += 10
            elif self.cld1 == 12:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[12].x = 100000000
                enemy1[12].y = 100000000
                enemy2[12].x = 100000000
                enemy2[12].y = 100000000
                enemy3[12].x = 100000000
                enemy3[12].y = 100000000
                bullet.cld1 = 13
                bullet2.cld1 = 13
                bullet3.cld1 = 13
                bullet4.cld1 = 13
                bullet5.cld1 = 13
                bullet6.cld1 = 13
                bulletNum1 = 3
                grass.gold += 10
            elif self.cld1 == 13:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[13].x = 100000000
                enemy1[13].y = 100000000
                enemy2[13].x = 100000000
                enemy2[13].y = 100000000
                enemy3[13].x = 100000000
                enemy3[13].y = 100000000
                bullet.cld1 = 14
                bullet2.cld1 = 14
                bullet3.cld1 = 14
                bullet4.cld1 = 14
                bullet5.cld1 = 14
                bullet6.cld1 = 14
                bulletNum1 = 4
                grass.gold += 10
            elif self.cld1 == 14:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[14].x = 100000000
                enemy1[14].y = 100000000
                enemy2[14].x = 100000000
                enemy2[14].y = 100000000
                enemy3[14].x = 100000000
                enemy3[14].y = 100000000
                bullet.cld1 = 15
                bullet2.cld1 = 15
                bullet3.cld1 = 15
                bullet4.cld1 = 15
                bullet5.cld1 = 15
                bullet6.cld1 = 15
                bulletNum1 = 5
                grass.gold += 10
            elif self.cld1 == 15:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[15].x = 100000000
                enemy1[15].y = 100000000
                enemy2[15].x = 100000000
                enemy2[15].y = 100000000
                enemy3[15].x = 100000000
                enemy3[15].y = 100000000
                bullet.cld1 = 16
                bullet2.cld1 = 16
                bullet3.cld1 = 16
                bullet4.cld1 = 16
                bullet5.cld1 = 16
                bullet6.cld1 = 16
                bulletNum1 = 6
                grass.gold += 10
            elif self.cld1 == 16:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[16].x = 100000000
                enemy1[16].y = 100000000
                enemy2[16].x = 100000000
                enemy2[16].y = 100000000
                enemy3[16].x = 100000000
                enemy3[16].y = 100000000
                bullet.cld1 = 17
                bullet2.cld1 = 17
                bullet3.cld1 = 17
                bullet4.cld1 = 17
                bullet5.cld1 = 17
                bullet6.cld1 = 17
                bulletNum1 = 7
                grass.gold += 10
            elif self.cld1 == 17:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[17].x = 100000000
                enemy1[17].y = 100000000
                enemy2[17].x = 100000000
                enemy2[17].y = 100000000
                enemy3[17].x = 100000000
                enemy3[17].y = 100000000
                bullet.cld1 = 18
                bullet2.cld1 = 18
                bullet3.cld1 = 18
                bullet4.cld1 = 18
                bullet5.cld1 = 18
                bullet6.cld1 = 18
                bulletNum1 = 8
                grass.gold += 10
            elif self.cld1 == 18:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[18].x = 100000000
                enemy1[18].y = 100000000
                enemy2[18].x = 100000000
                enemy2[18].y = 100000000
                enemy3[18].x = 100000000
                enemy3[18].y = 100000000
                bullet.cld1 = 19
                bullet2.cld1 = 19
                bullet3.cld1 = 19
                bullet4.cld1 = 19
                bullet5.cld1 = 19
                bullet6.cld1 = 19
                bulletNum1 = 9
                grass.gold += 10
            elif self.cld1 == 19:
                self.x = mouseXsave1[0]
                self.y = mouseYsave1[0]
                enemy1[19].x = 100000000
                enemy1[19].y = 100000000
                enemy2[19].x = 100000000
                enemy2[19].y = 100000000
                enemy3[19].x = 100000000
                enemy3[19].y = 100000000
                bullet.cld1 = 20
                bullet2.cld1 = 20
                bullet3.cld1 = 20
                bullet4.cld1 = 20
                bullet5.cld1 = 20
                bullet6.cld1 = 20
                bulletNum1 = 20
                grass.gold += 10

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(160, 180, 14, 14, self.x, self.y)


class Bullet2:
    global bulletNum1

    def __init__(self):
        self.image = load_image('bullet.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.enemy_x = [0 for i in range(20)]
        self.enemy_y = [0 for i in range(20)]
        self.flag1 = 1
        self.dir = 0
        self.speed = 0
        self.time = 0
        self.cld1 = 0

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def setEnemy1List(self, enemy1):
        for i in range(0, 20):
            self.enemy_x[i] = enemy1[i].x
            self.enemy_y[i] = enemy1[i].y

    def setEnemy2List(self, enemy2):
        for i in range(0, 20):
            self.enemy_x[i] = enemy2[i].x
            self.enemy_y[i] = enemy2[i].y

    def setEnemy3List(self, enemy3):
        for i in range(0, 20):
            self.enemy_x[i] = enemy3[i].x
            self.enemy_y[i] = enemy3[i].y

    def collide(self):
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if self.cld1 == 0:
            if left_a > self.enemy_x[0] + 20: return False
            if right_a < self.enemy_x[0] - 20: return False
            if top_a < self.enemy_y[0] - 25: return False
            if bottom_a > self.enemy_y[0] + 25: return False
        if self.cld1 == 1:
            if left_a > self.enemy_x[1] + 20: return False
            if right_a < self.enemy_x[1] - 20: return False
            if top_a < self.enemy_y[1] - 25: return False
            if bottom_a > self.enemy_y[1] + 25: return False
        if self.cld1 == 2:
            if left_a > self.enemy_x[2] + 20: return False
            if right_a < self.enemy_x[2] - 20: return False
            if top_a < self.enemy_y[2] - 25: return False
            if bottom_a > self.enemy_y[2] + 25: return False
        if self.cld1 == 3:
            if left_a > self.enemy_x[3] + 20: return False
            if right_a < self.enemy_x[3] - 20: return False
            if top_a < self.enemy_y[3] - 25: return False
            if bottom_a > self.enemy_y[3] + 25: return False
        if self.cld1 == 4:
            if left_a > self.enemy_x[4] + 20: return False
            if right_a < self.enemy_x[4] - 20: return False
            if top_a < self.enemy_y[4] - 25: return False
            if bottom_a > self.enemy_y[4] + 25: return False
        if self.cld1 == 5:
            if left_a > self.enemy_x[5] + 20: return False
            if right_a < self.enemy_x[5] - 20: return False
            if top_a < self.enemy_y[5] - 25: return False
            if bottom_a > self.enemy_y[5] + 25: return False
        if self.cld1 == 6:
            if left_a > self.enemy_x[6] + 20: return False
            if right_a < self.enemy_x[6] - 20: return False
            if top_a < self.enemy_y[6] - 25: return False
            if bottom_a > self.enemy_y[6] + 25: return False
        if self.cld1 == 7:
            if left_a > self.enemy_x[7] + 20: return False
            if right_a < self.enemy_x[7] - 20: return False
            if top_a < self.enemy_y[7] - 25: return False
            if bottom_a > self.enemy_y[7] + 25: return False
        if self.cld1 == 8:
            if left_a > self.enemy_x[8] + 20: return False
            if right_a < self.enemy_x[8] - 20: return False
            if top_a < self.enemy_y[8] - 25: return False
            if bottom_a > self.enemy_y[8] + 25: return False
        if self.cld1 == 9:
            if left_a > self.enemy_x[9] + 20: return False
            if right_a < self.enemy_x[9] - 20: return False
            if top_a < self.enemy_y[9] - 25: return False
            if bottom_a > self.enemy_y[9] + 25: return False
        if self.cld1 == 10:
            if left_a > self.enemy_x[10] + 20: return False
            if right_a < self.enemy_x[10] - 20: return False
            if top_a < self.enemy_y[10] - 25: return False
            if bottom_a > self.enemy_y[10] + 25: return False
        if self.cld1 == 11:
            if left_a > self.enemy_x[11] + 20: return False
            if right_a < self.enemy_x[11] - 20: return False
            if top_a < self.enemy_y[11] - 25: return False
            if bottom_a > self.enemy_y[11] + 25: return False
        if self.cld1 == 12:
            if left_a > self.enemy_x[12] + 20: return False
            if right_a < self.enemy_x[12] - 20: return False
            if top_a < self.enemy_y[12] - 25: return False
            if bottom_a > self.enemy_y[12] + 25: return False
        if self.cld1 == 13:
            if left_a > self.enemy_x[13] + 20: return False
            if right_a < self.enemy_x[13] - 20: return False
            if top_a < self.enemy_y[13] - 25: return False
            if bottom_a > self.enemy_y[13] + 25: return False
        if self.cld1 == 14:
            if left_a > self.enemy_x[14] + 20: return False
            if right_a < self.enemy_x[14] - 20: return False
            if top_a < self.enemy_y[14] - 25: return False
            if bottom_a > self.enemy_y[14] + 25: return False
        if self.cld1 == 15:
            if left_a > self.enemy_x[15] + 20: return False
            if right_a < self.enemy_x[15] - 20: return False
            if top_a < self.enemy_y[15] - 25: return False
            if bottom_a > self.enemy_y[15] + 25: return False
        if self.cld1 == 16:
            if left_a > self.enemy_x[16] + 20: return False
            if right_a < self.enemy_x[16] - 20: return False
            if top_a < self.enemy_y[16] - 25: return False
            if bottom_a > self.enemy_y[16] + 25: return False
        if self.cld1 == 17:
            if left_a > self.enemy_x[17] + 20: return False
            if right_a < self.enemy_x[17] - 20: return False
            if top_a < self.enemy_y[17] - 25: return False
            if bottom_a > self.enemy_y[17] + 25: return False
        if self.cld1 == 18:
            if left_a > self.enemy_x[18] + 20: return False
            if right_a < self.enemy_x[18] - 20: return False
            if top_a < self.enemy_y[18] - 25: return False
            if bottom_a > self.enemy_y[18] + 25: return False
        if self.cld1 == 19:
            if left_a > self.enemy_x[19] + 20: return False
            if right_a < self.enemy_x[19] - 20: return False
            if top_a < self.enemy_y[19] - 25: return False
            if bottom_a > self.enemy_y[19] + 25: return False

        return True

    def update(self):
        global bulletNum1, stage
        self.frame = (self.frame + 1) % 1
        if stage == 1:
            self.setEnemy1List(enemy1)
        if stage == 2:
            self.setEnemy1List(enemy1)
        if stage == 3:
            self.setEnemy2List(enemy2)
        if stage == 4:
            self.setEnemy2List(enemy2)
        if stage == 5:
            self.setEnemy3List(enemy3)
        if stage == 6:
            self.setEnemy3List(enemy3)

        if self.flag1:
            self.x = mouseXsave1[1]
            self.y = mouseYsave1[1]
            self.flag1 = 0

        self.speed = 96

        if self.cld1 == 0:
            self.dir = math.atan2(self.enemy_y[0] - self.y, self.enemy_x[0] - self.x)
        if self.cld1 == 1:
            self.dir = math.atan2(self.enemy_y[1] - self.y, self.enemy_x[1] - self.x)
        if self.cld1 == 2:
            self.dir = math.atan2(self.enemy_y[2] - self.y, self.enemy_x[2] - self.x)
        if self.cld1 == 3:
            self.dir = math.atan2(self.enemy_y[3] - self.y, self.enemy_x[3] - self.x)
        if self.cld1 == 4:
            self.dir = math.atan2(self.enemy_y[4] - self.y, self.enemy_x[4] - self.x)
        if self.cld1 == 5:
            self.dir = math.atan2(self.enemy_y[5] - self.y, self.enemy_x[5] - self.x)
        if self.cld1 == 6:
            self.dir = math.atan2(self.enemy_y[6] - self.y, self.enemy_x[6] - self.x)
        if self.cld1 == 7:
            self.dir = math.atan2(self.enemy_y[7] - self.y, self.enemy_x[7] - self.x)
        if self.cld1 == 8:
            self.dir = math.atan2(self.enemy_y[8] - self.y, self.enemy_x[8] - self.x)
        if self.cld1 == 9:
            self.dir = math.atan2(self.enemy_y[9] - self.y, self.enemy_x[9] - self.x)
        if self.cld1 == 10:
            self.dir = math.atan2(self.enemy_y[10] - self.y, self.enemy_x[10] - self.x)
        if self.cld1 == 11:
            self.dir = math.atan2(self.enemy_y[11] - self.y, self.enemy_x[11] - self.x)
        if self.cld1 == 12:
            self.dir = math.atan2(self.enemy_y[12] - self.y, self.enemy_x[12] - self.x)
        if self.cld1 == 13:
            self.dir = math.atan2(self.enemy_y[13] - self.y, self.enemy_x[13] - self.x)
        if self.cld1 == 14:
            self.dir = math.atan2(self.enemy_y[14] - self.y, self.enemy_x[14] - self.x)
        if self.cld1 == 15:
            self.dir = math.atan2(self.enemy_y[15] - self.y, self.enemy_x[15] - self.x)
        if self.cld1 == 16:
            self.dir = math.atan2(self.enemy_y[16] - self.y, self.enemy_x[16] - self.x)
        if self.cld1 == 17:
            self.dir = math.atan2(self.enemy_y[17] - self.y, self.enemy_x[17] - self.x)
        if self.cld1 == 18:
            self.dir = math.atan2(self.enemy_y[18] - self.y, self.enemy_x[18] - self.x)
        if self.cld1 == 19:
            self.dir = math.atan2(self.enemy_y[19] - self.y, self.enemy_x[19] - self.x)

        self.time = game_framework.frame_time
        #print(self.time)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.collide():
            if self.cld1 == 0:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[0].x = 100000000
                enemy1[0].y = 100000000
                enemy2[0].x = 100000000
                enemy2[0].y = 100000000
                enemy3[0].x = 100000000
                enemy3[0].y = 100000000
                bullet.cld1 = 1
                bullet2.cld1 = 1
                bullet3.cld1 = 1
                bullet4.cld1 = 1
                bullet5.cld1 = 1
                bullet6.cld1 = 1
                bulletNum1 = 1
                grass.gold += 10
            elif self.cld1 == 1:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[1].x = 100000000
                enemy1[1].y = 100000000
                enemy2[1].x = 100000000
                enemy2[1].y = 100000000
                enemy3[1].x = 100000000
                enemy3[1].y = 100000000
                bullet.cld1 = 2
                bullet2.cld1 = 2
                bullet3.cld1 = 2
                bullet4.cld1 = 2
                bullet5.cld1 = 2
                bullet6.cld1 = 2
                bulletNum1 = 2
                grass.gold += 10
            elif self.cld1 == 2:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[2].x = 100000000
                enemy1[2].y = 100000000
                enemy2[2].x = 100000000
                enemy2[2].y = 100000000
                enemy3[2].x = 100000000
                enemy3[2].y = 100000000
                bullet.cld1 = 3
                bullet2.cld1 = 3
                bullet3.cld1 = 3
                bullet4.cld1 = 3
                bullet5.cld1 = 3
                bullet6.cld1 = 3
                bulletNum1 = 3
                grass.gold += 10
            elif self.cld1 == 3:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[3].x = 100000000
                enemy1[3].y = 100000000
                enemy2[3].x = 100000000
                enemy2[3].y = 100000000
                enemy3[3].x = 100000000
                enemy3[3].y = 100000000
                bullet.cld1 = 4
                bullet2.cld1 = 4
                bullet3.cld1 = 4
                bullet4.cld1 = 4
                bullet5.cld1 = 4
                bullet6.cld1 = 4
                bulletNum1 = 4
                grass.gold += 10
            elif self.cld1 == 4:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[4].x = 100000000
                enemy1[4].y = 100000000
                enemy2[4].x = 100000000
                enemy2[4].y = 100000000
                enemy3[4].x = 100000000
                enemy3[4].y = 100000000
                bullet.cld1 = 5
                bullet2.cld1 = 5
                bullet3.cld1 = 5
                bullet4.cld1 = 5
                bullet5.cld1 = 5
                bullet6.cld1 = 5
                bulletNum1 = 5
                grass.gold += 10
            elif self.cld1 == 5:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[5].x = 100000000
                enemy1[5].y = 100000000
                enemy2[5].x = 100000000
                enemy2[5].y = 100000000
                enemy3[5].x = 100000000
                enemy3[5].y = 100000000
                bullet.cld1 = 6
                bullet2.cld1 = 6
                bullet3.cld1 = 6
                bullet4.cld1 = 6
                bullet5.cld1 = 6
                bullet6.cld1 = 6
                bulletNum1 = 6
                grass.gold += 10
            elif self.cld1 == 6:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[6].x = 100000000
                enemy1[6].y = 100000000
                enemy2[6].x = 100000000
                enemy2[6].y = 100000000
                enemy3[6].x = 100000000
                enemy3[6].y = 100000000
                bullet.cld1 = 7
                bullet2.cld1 = 7
                bullet3.cld1 = 7
                bullet4.cld1 = 7
                bullet5.cld1 = 7
                bullet6.cld1 = 7
                bulletNum1 = 7
                grass.gold += 10
            elif self.cld1 == 7:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[7].x = 100000000
                enemy1[7].y = 100000000
                enemy2[7].x = 100000000
                enemy2[7].y = 100000000
                enemy3[7].x = 100000000
                enemy3[7].y = 100000000
                bullet.cld1 = 8
                bullet2.cld1 = 8
                bullet3.cld1 = 8
                bullet4.cld1 = 8
                bullet5.cld1 = 8
                bullet6.cld1 = 1
                bulletNum1 = 8
                grass.gold += 10
            elif self.cld1 == 8:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[8].x = 100000000
                enemy1[8].y = 100000000
                enemy2[8].x = 100000000
                enemy2[8].y = 100000000
                enemy3[8].x = 100000000
                enemy3[8].y = 100000000
                bullet.cld1 = 9
                bullet2.cld1 = 9
                bullet3.cld1 = 9
                bullet4.cld1 = 9
                bullet5.cld1 = 9
                bullet6.cld1 = 9
                bulletNum1 = 9
                grass.gold += 10
            elif self.cld1 == 9:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[9].x = 100000000
                enemy1[9].y = 100000000
                enemy2[9].x = 100000000
                enemy2[9].y = 100000000
                enemy3[9].x = 100000000
                enemy3[9].y = 100000000
                bullet.cld1 = 10
                bullet2.cld1 = 10
                bullet3.cld1 = 10
                bullet4.cld1 = 10
                bullet5.cld1 = 10
                bullet6.cld1 = 10
                bulletNum1 = 10
                grass.gold += 10
            elif self.cld1 == 10:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[10].x = 100000000
                enemy1[10].y = 100000000
                enemy2[10].x = 100000000
                enemy2[10].y = 100000000
                enemy3[10].x = 100000000
                enemy3[10].y = 100000000
                bullet.cld1 = 11
                bullet2.cld1 = 11
                bullet3.cld1 = 11
                bullet4.cld1 = 11
                bullet5.cld1 = 11
                bullet6.cld1 = 11
                bulletNum1 = 11
                grass.gold += 10
            elif self.cld1 == 11:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[11].x = 100000000
                enemy1[11].y = 100000000
                enemy2[11].x = 100000000
                enemy2[11].y = 100000000
                enemy3[11].x = 100000000
                enemy3[11].y = 100000000
                bullet.cld1 = 12
                bullet2.cld1 = 12
                bullet3.cld1 = 12
                bullet4.cld1 = 12
                bullet5.cld1 = 12
                bullet6.cld1 = 12
                bulletNum1 = 2
                grass.gold += 10
            elif self.cld1 == 12:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[12].x = 100000000
                enemy1[12].y = 100000000
                enemy2[12].x = 100000000
                enemy2[12].y = 100000000
                enemy3[12].x = 100000000
                enemy3[12].y = 100000000
                bullet.cld1 = 13
                bullet2.cld1 = 13
                bullet3.cld1 = 13
                bullet4.cld1 = 13
                bullet5.cld1 = 13
                bullet6.cld1 = 13
                bulletNum1 = 3
                grass.gold += 10
            elif self.cld1 == 13:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[13].x = 100000000
                enemy1[13].y = 100000000
                enemy2[13].x = 100000000
                enemy2[13].y = 100000000
                enemy3[13].x = 100000000
                enemy3[13].y = 100000000
                bullet.cld1 = 14
                bullet2.cld1 = 14
                bullet3.cld1 = 14
                bullet4.cld1 = 14
                bullet5.cld1 = 14
                bullet6.cld1 = 14
                bulletNum1 = 4
                grass.gold += 10
            elif self.cld1 == 14:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[14].x = 100000000
                enemy1[14].y = 100000000
                enemy2[14].x = 100000000
                enemy2[14].y = 100000000
                enemy3[14].x = 100000000
                enemy3[14].y = 100000000
                bullet.cld1 = 15
                bullet2.cld1 = 15
                bullet3.cld1 = 15
                bullet4.cld1 = 15
                bullet5.cld1 = 15
                bullet6.cld1 = 15
                bulletNum1 = 5
                grass.gold += 10
            elif self.cld1 == 15:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[15].x = 100000000
                enemy1[15].y = 100000000
                enemy2[15].x = 100000000
                enemy2[15].y = 100000000
                enemy3[15].x = 100000000
                enemy3[15].y = 100000000
                bullet.cld1 = 16
                bullet2.cld1 = 16
                bullet3.cld1 = 16
                bullet4.cld1 = 16
                bullet5.cld1 = 16
                bullet6.cld1 = 16
                bulletNum1 = 6
                grass.gold += 10
            elif self.cld1 == 16:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[16].x = 100000000
                enemy1[16].y = 100000000
                enemy2[16].x = 100000000
                enemy2[16].y = 100000000
                enemy3[16].x = 100000000
                enemy3[16].y = 100000000
                bullet.cld1 = 17
                bullet2.cld1 = 17
                bullet3.cld1 = 17
                bullet4.cld1 = 17
                bullet5.cld1 = 17
                bullet6.cld1 = 17
                bulletNum1 = 7
                grass.gold += 10
            elif self.cld1 == 17:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[17].x = 100000000
                enemy1[17].y = 100000000
                enemy2[17].x = 100000000
                enemy2[17].y = 100000000
                enemy3[17].x = 100000000
                enemy3[17].y = 100000000
                bullet.cld1 = 18
                bullet2.cld1 = 18
                bullet3.cld1 = 18
                bullet4.cld1 = 18
                bullet5.cld1 = 18
                bullet6.cld1 = 18
                bulletNum1 = 8
                grass.gold += 10
            elif self.cld1 == 18:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[18].x = 100000000
                enemy1[18].y = 100000000
                enemy2[18].x = 100000000
                enemy2[18].y = 100000000
                enemy3[18].x = 100000000
                enemy3[18].y = 100000000
                bullet.cld1 = 19
                bullet2.cld1 = 19
                bullet3.cld1 = 19
                bullet4.cld1 = 19
                bullet5.cld1 = 19
                bullet6.cld1 = 19
                bulletNum1 = 9
                grass.gold += 10
            elif self.cld1 == 19:
                self.x = mouseXsave1[1]
                self.y = mouseYsave1[1]
                enemy1[19].x = 100000000
                enemy1[19].y = 100000000
                enemy2[19].x = 100000000
                enemy2[19].y = 100000000
                enemy3[19].x = 100000000
                enemy3[19].y = 100000000
                bullet.cld1 = 20
                bullet2.cld1 = 20
                bullet3.cld1 = 20
                bullet4.cld1 = 20
                bullet5.cld1 = 20
                bullet6.cld1 = 20
                bulletNum1 = 20
                grass.gold += 10

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(160, 180, 14, 14, self.x, self.y)


class Bullet3:
    global bulletNum1

    def __init__(self):
        self.image = load_image('bullet.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.enemy_x = [0 for i in range(20)]
        self.enemy_y = [0 for i in range(20)]
        self.flag = 1
        self.dir = 0
        self.speed = 0
        self.time = 0
        self.cld1 = 0

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def setEnemy1List(self, enemy1):
        for i in range(0, 20):
            self.enemy_x[i] = enemy1[i].x
            self.enemy_y[i] = enemy1[i].y

    def setEnemy2List(self, enemy2):
        for i in range(0, 20):
            self.enemy_x[i] = enemy2[i].x
            self.enemy_y[i] = enemy2[i].y

    def setEnemy3List(self, enemy3):
        for i in range(0, 20):
            self.enemy_x[i] = enemy3[i].x
            self.enemy_y[i] = enemy3[i].y

    def collide(self):
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if self.cld1 == 0:
            if left_a > self.enemy_x[0] + 20: return False
            if right_a < self.enemy_x[0] - 20: return False
            if top_a < self.enemy_y[0] - 25: return False
            if bottom_a > self.enemy_y[0] + 25: return False
        if self.cld1 == 1:
            if left_a > self.enemy_x[1] + 20: return False
            if right_a < self.enemy_x[1] - 20: return False
            if top_a < self.enemy_y[1] - 25: return False
            if bottom_a > self.enemy_y[1] + 25: return False
        if self.cld1 == 2:
            if left_a > self.enemy_x[2] + 20: return False
            if right_a < self.enemy_x[2] - 20: return False
            if top_a < self.enemy_y[2] - 25: return False
            if bottom_a > self.enemy_y[2] + 25: return False
        if self.cld1 == 3:
            if left_a > self.enemy_x[3] + 20: return False
            if right_a < self.enemy_x[3] - 20: return False
            if top_a < self.enemy_y[3] - 25: return False
            if bottom_a > self.enemy_y[3] + 25: return False
        if self.cld1 == 4:
            if left_a > self.enemy_x[4] + 20: return False
            if right_a < self.enemy_x[4] - 20: return False
            if top_a < self.enemy_y[4] - 25: return False
            if bottom_a > self.enemy_y[4] + 25: return False
        if self.cld1 == 5:
            if left_a > self.enemy_x[5] + 20: return False
            if right_a < self.enemy_x[5] - 20: return False
            if top_a < self.enemy_y[5] - 25: return False
            if bottom_a > self.enemy_y[5] + 25: return False
        if self.cld1 == 6:
            if left_a > self.enemy_x[6] + 20: return False
            if right_a < self.enemy_x[6] - 20: return False
            if top_a < self.enemy_y[6] - 25: return False
            if bottom_a > self.enemy_y[6] + 25: return False
        if self.cld1 == 7:
            if left_a > self.enemy_x[7] + 20: return False
            if right_a < self.enemy_x[7] - 20: return False
            if top_a < self.enemy_y[7] - 25: return False
            if bottom_a > self.enemy_y[7] + 25: return False
        if self.cld1 == 8:
            if left_a > self.enemy_x[8] + 20: return False
            if right_a < self.enemy_x[8] - 20: return False
            if top_a < self.enemy_y[8] - 25: return False
            if bottom_a > self.enemy_y[8] + 25: return False
        if self.cld1 == 9:
            if left_a > self.enemy_x[9] + 20: return False
            if right_a < self.enemy_x[9] - 20: return False
            if top_a < self.enemy_y[9] - 25: return False
            if bottom_a > self.enemy_y[9] + 25: return False
        if self.cld1 == 10:
            if left_a > self.enemy_x[10] + 20: return False
            if right_a < self.enemy_x[10] - 20: return False
            if top_a < self.enemy_y[10] - 25: return False
            if bottom_a > self.enemy_y[10] + 25: return False
        if self.cld1 == 11:
            if left_a > self.enemy_x[11] + 20: return False
            if right_a < self.enemy_x[11] - 20: return False
            if top_a < self.enemy_y[11] - 25: return False
            if bottom_a > self.enemy_y[11] + 25: return False
        if self.cld1 == 12:
            if left_a > self.enemy_x[12] + 20: return False
            if right_a < self.enemy_x[12] - 20: return False
            if top_a < self.enemy_y[12] - 25: return False
            if bottom_a > self.enemy_y[12] + 25: return False
        if self.cld1 == 13:
            if left_a > self.enemy_x[13] + 20: return False
            if right_a < self.enemy_x[13] - 20: return False
            if top_a < self.enemy_y[13] - 25: return False
            if bottom_a > self.enemy_y[13] + 25: return False
        if self.cld1 == 14:
            if left_a > self.enemy_x[14] + 20: return False
            if right_a < self.enemy_x[14] - 20: return False
            if top_a < self.enemy_y[14] - 25: return False
            if bottom_a > self.enemy_y[14] + 25: return False
        if self.cld1 == 15:
            if left_a > self.enemy_x[15] + 20: return False
            if right_a < self.enemy_x[15] - 20: return False
            if top_a < self.enemy_y[15] - 25: return False
            if bottom_a > self.enemy_y[15] + 25: return False
        if self.cld1 == 16:
            if left_a > self.enemy_x[16] + 20: return False
            if right_a < self.enemy_x[16] - 20: return False
            if top_a < self.enemy_y[16] - 25: return False
            if bottom_a > self.enemy_y[16] + 25: return False
        if self.cld1 == 17:
            if left_a > self.enemy_x[17] + 20: return False
            if right_a < self.enemy_x[17] - 20: return False
            if top_a < self.enemy_y[17] - 25: return False
            if bottom_a > self.enemy_y[17] + 25: return False
        if self.cld1 == 18:
            if left_a > self.enemy_x[18] + 20: return False
            if right_a < self.enemy_x[18] - 20: return False
            if top_a < self.enemy_y[18] - 25: return False
            if bottom_a > self.enemy_y[18] + 25: return False
        if self.cld1 == 19:
            if left_a > self.enemy_x[19] + 20: return False
            if right_a < self.enemy_x[19] - 20: return False
            if top_a < self.enemy_y[19] - 25: return False
            if bottom_a > self.enemy_y[19] + 25: return False

        return True

    def update(self):
        global bulletNum1, stage
        self.frame = (self.frame + 1) % 1
        if stage == 1:
            self.setEnemy1List(enemy1)
        if stage == 2:
            self.setEnemy1List(enemy1)
        if stage == 3:
            self.setEnemy2List(enemy2)
        if stage == 4:
            self.setEnemy2List(enemy2)
        if stage == 5:
            self.setEnemy3List(enemy3)
        if stage == 6:
            self.setEnemy3List(enemy3)

        if self.flag:
            self.x = mouseXsave2[0]
            self.y = mouseYsave2[0]
            self.flag = 0

        self.speed = 96

        if self.cld1 == 0:
            self.dir = math.atan2(self.enemy_y[0] - self.y, self.enemy_x[0] - self.x)
        if self.cld1 == 1:
            self.dir = math.atan2(self.enemy_y[1] - self.y, self.enemy_x[1] - self.x)
        if self.cld1 == 2:
            self.dir = math.atan2(self.enemy_y[2] - self.y, self.enemy_x[2] - self.x)
        if self.cld1 == 3:
            self.dir = math.atan2(self.enemy_y[3] - self.y, self.enemy_x[3] - self.x)
        if self.cld1 == 4:
            self.dir = math.atan2(self.enemy_y[4] - self.y, self.enemy_x[4] - self.x)
        if self.cld1 == 5:
            self.dir = math.atan2(self.enemy_y[5] - self.y, self.enemy_x[5] - self.x)
        if self.cld1 == 6:
            self.dir = math.atan2(self.enemy_y[6] - self.y, self.enemy_x[6] - self.x)
        if self.cld1 == 7:
            self.dir = math.atan2(self.enemy_y[7] - self.y, self.enemy_x[7] - self.x)
        if self.cld1 == 8:
            self.dir = math.atan2(self.enemy_y[8] - self.y, self.enemy_x[8] - self.x)
        if self.cld1 == 9:
            self.dir = math.atan2(self.enemy_y[9] - self.y, self.enemy_x[9] - self.x)
        if self.cld1 == 10:
            self.dir = math.atan2(self.enemy_y[10] - self.y, self.enemy_x[10] - self.x)
        if self.cld1 == 11:
            self.dir = math.atan2(self.enemy_y[11] - self.y, self.enemy_x[11] - self.x)
        if self.cld1 == 12:
            self.dir = math.atan2(self.enemy_y[12] - self.y, self.enemy_x[12] - self.x)
        if self.cld1 == 13:
            self.dir = math.atan2(self.enemy_y[13] - self.y, self.enemy_x[13] - self.x)
        if self.cld1 == 14:
            self.dir = math.atan2(self.enemy_y[14] - self.y, self.enemy_x[14] - self.x)
        if self.cld1 == 15:
            self.dir = math.atan2(self.enemy_y[15] - self.y, self.enemy_x[15] - self.x)
        if self.cld1 == 16:
            self.dir = math.atan2(self.enemy_y[16] - self.y, self.enemy_x[16] - self.x)
        if self.cld1 == 17:
            self.dir = math.atan2(self.enemy_y[17] - self.y, self.enemy_x[17] - self.x)
        if self.cld1 == 18:
            self.dir = math.atan2(self.enemy_y[18] - self.y, self.enemy_x[18] - self.x)
        if self.cld1 == 19:
            self.dir = math.atan2(self.enemy_y[19] - self.y, self.enemy_x[19] - self.x)

        self.time = game_framework.frame_time
        #print(self.time)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.collide():
            if self.cld1 == 0:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[0].x = 100000000
                enemy1[0].y = 100000000
                enemy2[0].x = 100000000
                enemy2[0].y = 100000000
                enemy3[0].x = 100000000
                enemy3[0].y = 100000000
                bullet.cld1 = 1
                bullet2.cld1 = 1
                bullet3.cld1 = 1
                bullet4.cld1 = 1
                bullet5.cld1 = 1
                bullet6.cld1 = 1
                bulletNum1 = 1
                grass.gold += 20
            elif self.cld1 == 1:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[1].x = 100000000
                enemy1[1].y = 100000000
                enemy2[1].x = 100000000
                enemy2[1].y = 100000000
                enemy3[1].x = 100000000
                enemy3[1].y = 100000000
                bullet.cld1 = 2
                bullet2.cld1 = 2
                bullet3.cld1 = 2
                bullet4.cld1 = 2
                bullet5.cld1 = 2
                bullet6.cld1 = 2
                bulletNum1 = 2
                grass.gold += 20
            elif self.cld1 == 2:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[2].x = 100000000
                enemy1[2].y = 100000000
                enemy2[2].x = 100000000
                enemy2[2].y = 100000000
                enemy3[2].x = 100000000
                enemy3[2].y = 100000000
                bullet.cld1 = 3
                bullet2.cld1 = 3
                bullet3.cld1 = 3
                bullet4.cld1 = 3
                bullet5.cld1 = 3
                bullet6.cld1 = 3
                bulletNum1 = 3
                grass.gold += 20
            elif self.cld1 == 3:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[3].x = 100000000
                enemy1[3].y = 100000000
                enemy2[3].x = 100000000
                enemy2[3].y = 100000000
                enemy3[3].x = 100000000
                enemy3[3].y = 100000000
                bullet.cld1 = 4
                bullet2.cld1 = 4
                bullet3.cld1 = 4
                bullet4.cld1 = 4
                bullet5.cld1 = 4
                bullet6.cld1 = 4
                bulletNum1 = 4
                grass.gold += 20
            elif self.cld1 == 4:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[4].x = 100000000
                enemy1[4].y = 100000000
                enemy2[4].x = 100000000
                enemy2[4].y = 100000000
                enemy3[4].x = 100000000
                enemy3[4].y = 100000000
                bullet.cld1 = 5
                bullet2.cld1 = 5
                bullet3.cld1 = 5
                bullet4.cld1 = 5
                bullet5.cld1 = 5
                bullet6.cld1 = 5
                bulletNum1 = 5
                grass.gold += 20
            elif self.cld1 == 5:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[5].x = 100000000
                enemy1[5].y = 100000000
                enemy2[5].x = 100000000
                enemy2[5].y = 100000000
                enemy3[5].x = 100000000
                enemy3[5].y = 100000000
                bullet.cld1 = 6
                bullet2.cld1 = 6
                bullet3.cld1 = 6
                bullet4.cld1 = 6
                bullet5.cld1 = 6
                bullet6.cld1 = 6
                bulletNum1 = 6
                grass.gold +=20
            elif self.cld1 == 6:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[6].x = 100000000
                enemy1[6].y = 100000000
                enemy2[6].x = 100000000
                enemy2[6].y = 100000000
                enemy3[6].x = 100000000
                enemy3[6].y = 100000000
                bullet.cld1 = 7
                bullet2.cld1 = 7
                bullet3.cld1 = 7
                bullet4.cld1 = 7
                bullet5.cld1 = 7
                bullet6.cld1 = 7
                bulletNum1 = 7
                grass.gold += 20
            elif self.cld1 == 7:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[7].x = 100000000
                enemy1[7].y = 100000000
                enemy2[7].x = 100000000
                enemy2[7].y = 100000000
                enemy3[7].x = 100000000
                enemy3[7].y = 100000000
                bullet.cld1 = 8
                bullet2.cld1 = 8
                bullet3.cld1 = 8
                bullet4.cld1 = 8
                bullet5.cld1 = 8
                bullet6.cld1 = 1
                bulletNum1 = 8
                grass.gold += 20
            elif self.cld1 == 8:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[8].x = 100000000
                enemy1[8].y = 100000000
                enemy2[8].x = 100000000
                enemy2[8].y = 100000000
                enemy3[8].x = 100000000
                enemy3[8].y = 100000000
                bullet.cld1 = 9
                bullet2.cld1 = 9
                bullet3.cld1 = 9
                bullet4.cld1 = 9
                bullet5.cld1 = 9
                bullet6.cld1 = 9
                bulletNum1 = 9
                grass.gold += 20
            elif self.cld1 == 9:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[9].x = 100000000
                enemy1[9].y = 100000000
                enemy2[9].x = 100000000
                enemy2[9].y = 100000000
                enemy3[9].x = 100000000
                enemy3[9].y = 100000000
                bullet.cld1 = 10
                bullet2.cld1 = 10
                bullet3.cld1 = 10
                bullet4.cld1 = 10
                bullet5.cld1 = 10
                bullet6.cld1 = 10
                bulletNum1 = 10
                grass.gold += 20
            elif self.cld1 == 10:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[10].x = 100000000
                enemy1[10].y = 100000000
                enemy2[10].x = 100000000
                enemy2[10].y = 100000000
                enemy3[10].x = 100000000
                enemy3[10].y = 100000000
                bullet.cld1 = 11
                bullet2.cld1 = 11
                bullet3.cld1 = 11
                bullet4.cld1 = 11
                bullet5.cld1 = 11
                bullet6.cld1 = 11
                bulletNum1 = 11
                grass.gold += 20
            elif self.cld1 == 11:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[11].x = 100000000
                enemy1[11].y = 100000000
                enemy2[11].x = 100000000
                enemy2[11].y = 100000000
                enemy3[11].x = 100000000
                enemy3[11].y = 100000000
                bullet.cld1 = 12
                bullet2.cld1 = 12
                bullet3.cld1 = 12
                bullet4.cld1 = 12
                bullet5.cld1 = 12
                bullet6.cld1 = 12
                bulletNum1 = 2
                grass.gold += 20
            elif self.cld1 == 12:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[12].x = 100000000
                enemy1[12].y = 100000000
                enemy2[12].x = 100000000
                enemy2[12].y = 100000000
                enemy3[12].x = 100000000
                enemy3[12].y = 100000000
                bullet.cld1 = 13
                bullet2.cld1 = 13
                bullet3.cld1 = 13
                bullet4.cld1 = 13
                bullet5.cld1 = 13
                bullet6.cld1 = 13
                bulletNum1 = 3
                grass.gold +=20
            elif self.cld1 == 13:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[13].x = 100000000
                enemy1[13].y = 100000000
                enemy2[13].x = 100000000
                enemy2[13].y = 100000000
                enemy3[13].x = 100000000
                enemy3[13].y = 100000000
                bullet.cld1 = 14
                bullet2.cld1 = 14
                bullet3.cld1 = 14
                bullet4.cld1 = 14
                bullet5.cld1 = 14
                bullet6.cld1 = 14
                bulletNum1 = 4
                grass.gold += 20
            elif self.cld1 == 14:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[14].x = 100000000
                enemy1[14].y = 100000000
                enemy2[14].x = 100000000
                enemy2[14].y = 100000000
                enemy3[14].x = 100000000
                enemy3[14].y = 100000000
                bullet.cld1 = 15
                bullet2.cld1 = 15
                bullet3.cld1 = 15
                bullet4.cld1 = 15
                bullet5.cld1 = 15
                bullet6.cld1 = 15
                bulletNum1 = 5
                grass.gold += 20
            elif self.cld1 == 15:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[15].x = 100000000
                enemy1[15].y = 100000000
                enemy2[15].x = 100000000
                enemy2[15].y = 100000000
                enemy3[15].x = 100000000
                enemy3[15].y = 100000000
                bullet.cld1 = 16
                bullet2.cld1 = 16
                bullet3.cld1 = 16
                bullet4.cld1 = 16
                bullet5.cld1 = 16
                bullet6.cld1 = 16
                bulletNum1 = 6
                grass.gold += 20
            elif self.cld1 == 16:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[16].x = 100000000
                enemy1[16].y = 100000000
                enemy2[16].x = 100000000
                enemy2[16].y = 100000000
                enemy3[16].x = 100000000
                enemy3[16].y = 100000000
                bullet.cld1 = 17
                bullet2.cld1 = 17
                bullet3.cld1 = 17
                bullet4.cld1 = 17
                bullet5.cld1 = 17
                bullet6.cld1 = 17
                bulletNum1 = 7
                grass.gold +=20
            elif self.cld1 == 17:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[17].x = 100000000
                enemy1[17].y = 100000000
                enemy2[17].x = 100000000
                enemy2[17].y = 100000000
                enemy3[17].x = 100000000
                enemy3[17].y = 100000000
                bullet.cld1 = 18
                bullet2.cld1 = 18
                bullet3.cld1 = 18
                bullet4.cld1 = 18
                bullet5.cld1 = 18
                bullet6.cld1 = 18
                bulletNum1 = 8
                grass.gold += 20
            elif self.cld1 == 18:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[18].x = 100000000
                enemy1[18].y = 100000000
                enemy2[18].x = 100000000
                enemy2[18].y = 100000000
                enemy3[18].x = 100000000
                enemy3[18].y = 100000000
                bullet.cld1 = 19
                bullet2.cld1 = 19
                bullet3.cld1 = 19
                bullet4.cld1 = 19
                bullet5.cld1 = 19
                bullet6.cld1 = 19
                bulletNum1 = 9
                grass.gold += 20
            elif self.cld1 == 19:
                self.x = mouseXsave2[0]
                self.y = mouseYsave2[0]
                enemy1[19].x = 100000000
                enemy1[19].y = 100000000
                enemy2[19].x = 100000000
                enemy2[19].y = 100000000
                enemy3[19].x = 100000000
                enemy3[19].y = 100000000
                bullet.cld1 = 20
                bullet2.cld1 = 20
                bullet3.cld1 = 20
                bullet4.cld1 = 20
                bullet5.cld1 = 20
                bullet6.cld1 = 20
                bulletNum1 = 20
                grass.gold += 20

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(206, 225, 14, 14, self.x, self.y)


class Bullet4:
    global bulletNum1

    def __init__(self):
        self.image = load_image('bullet.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.enemy_x = [0 for i in range(20)]
        self.enemy_y = [0 for i in range(20)]
        self.flag1 = 1
        self.dir = 0
        self.speed = 0
        self.time = 0
        self.cld1 = 0

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def setEnemy1List(self, enemy1):
        for i in range(0, 20):
            self.enemy_x[i] = enemy1[i].x
            self.enemy_y[i] = enemy1[i].y

    def setEnemy2List(self, enemy2):
        for i in range(0, 20):
            self.enemy_x[i] = enemy2[i].x
            self.enemy_y[i] = enemy2[i].y

    def setEnemy3List(self, enemy3):
        for i in range(0, 20):
            self.enemy_x[i] = enemy3[i].x
            self.enemy_y[i] = enemy3[i].y

    def collide(self):
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if self.cld1 == 0:
            if left_a > self.enemy_x[0] + 20: return False
            if right_a < self.enemy_x[0] - 20: return False
            if top_a < self.enemy_y[0] - 25: return False
            if bottom_a > self.enemy_y[0] + 25: return False
        if self.cld1 == 1:
            if left_a > self.enemy_x[1] + 20: return False
            if right_a < self.enemy_x[1] - 20: return False
            if top_a < self.enemy_y[1] - 25: return False
            if bottom_a > self.enemy_y[1] + 25: return False
        if self.cld1 == 2:
            if left_a > self.enemy_x[2] + 20: return False
            if right_a < self.enemy_x[2] - 20: return False
            if top_a < self.enemy_y[2] - 25: return False
            if bottom_a > self.enemy_y[2] + 25: return False
        if self.cld1 == 3:
            if left_a > self.enemy_x[3] + 20: return False
            if right_a < self.enemy_x[3] - 20: return False
            if top_a < self.enemy_y[3] - 25: return False
            if bottom_a > self.enemy_y[3] + 25: return False
        if self.cld1 == 4:
            if left_a > self.enemy_x[4] + 20: return False
            if right_a < self.enemy_x[4] - 20: return False
            if top_a < self.enemy_y[4] - 25: return False
            if bottom_a > self.enemy_y[4] + 25: return False
        if self.cld1 == 5:
            if left_a > self.enemy_x[5] + 20: return False
            if right_a < self.enemy_x[5] - 20: return False
            if top_a < self.enemy_y[5] - 25: return False
            if bottom_a > self.enemy_y[5] + 25: return False
        if self.cld1 == 6:
            if left_a > self.enemy_x[6] + 20: return False
            if right_a < self.enemy_x[6] - 20: return False
            if top_a < self.enemy_y[6] - 25: return False
            if bottom_a > self.enemy_y[6] + 25: return False
        if self.cld1 == 7:
            if left_a > self.enemy_x[7] + 20: return False
            if right_a < self.enemy_x[7] - 20: return False
            if top_a < self.enemy_y[7] - 25: return False
            if bottom_a > self.enemy_y[7] + 25: return False
        if self.cld1 == 8:
            if left_a > self.enemy_x[8] + 20: return False
            if right_a < self.enemy_x[8] - 20: return False
            if top_a < self.enemy_y[8] - 25: return False
            if bottom_a > self.enemy_y[8] + 25: return False
        if self.cld1 == 9:
            if left_a > self.enemy_x[9] + 20: return False
            if right_a < self.enemy_x[9] - 20: return False
            if top_a < self.enemy_y[9] - 25: return False
            if bottom_a > self.enemy_y[9] + 25: return False
        if self.cld1 == 10:
            if left_a > self.enemy_x[10] + 20: return False
            if right_a < self.enemy_x[10] - 20: return False
            if top_a < self.enemy_y[10] - 25: return False
            if bottom_a > self.enemy_y[10] + 25: return False
        if self.cld1 == 11:
            if left_a > self.enemy_x[11] + 20: return False
            if right_a < self.enemy_x[11] - 20: return False
            if top_a < self.enemy_y[11] - 25: return False
            if bottom_a > self.enemy_y[11] + 25: return False
        if self.cld1 == 12:
            if left_a > self.enemy_x[12] + 20: return False
            if right_a < self.enemy_x[12] - 20: return False
            if top_a < self.enemy_y[12] - 25: return False
            if bottom_a > self.enemy_y[12] + 25: return False
        if self.cld1 == 13:
            if left_a > self.enemy_x[13] + 20: return False
            if right_a < self.enemy_x[13] - 20: return False
            if top_a < self.enemy_y[13] - 25: return False
            if bottom_a > self.enemy_y[13] + 25: return False
        if self.cld1 == 14:
            if left_a > self.enemy_x[14] + 20: return False
            if right_a < self.enemy_x[14] - 20: return False
            if top_a < self.enemy_y[14] - 25: return False
            if bottom_a > self.enemy_y[14] + 25: return False
        if self.cld1 == 15:
            if left_a > self.enemy_x[15] + 20: return False
            if right_a < self.enemy_x[15] - 20: return False
            if top_a < self.enemy_y[15] - 25: return False
            if bottom_a > self.enemy_y[15] + 25: return False
        if self.cld1 == 16:
            if left_a > self.enemy_x[16] + 20: return False
            if right_a < self.enemy_x[16] - 20: return False
            if top_a < self.enemy_y[16] - 25: return False
            if bottom_a > self.enemy_y[16] + 25: return False
        if self.cld1 == 17:
            if left_a > self.enemy_x[17] + 20: return False
            if right_a < self.enemy_x[17] - 20: return False
            if top_a < self.enemy_y[17] - 25: return False
            if bottom_a > self.enemy_y[17] + 25: return False
        if self.cld1 == 18:
            if left_a > self.enemy_x[18] + 20: return False
            if right_a < self.enemy_x[18] - 20: return False
            if top_a < self.enemy_y[18] - 25: return False
            if bottom_a > self.enemy_y[18] + 25: return False
        if self.cld1 == 19:
            if left_a > self.enemy_x[19] + 20: return False
            if right_a < self.enemy_x[19] - 20: return False
            if top_a < self.enemy_y[19] - 25: return False
            if bottom_a > self.enemy_y[19] + 25: return False

        return True

    def update(self):
        global bulletNum1, stage
        self.frame = (self.frame + 1) % 1
        if stage == 1:
            self.setEnemy1List(enemy1)
        if stage == 2:
            self.setEnemy1List(enemy1)
        if stage == 3:
            self.setEnemy2List(enemy2)
        if stage == 4:
            self.setEnemy2List(enemy2)
        if stage == 5:
            self.setEnemy3List(enemy3)
        if stage == 6:
            self.setEnemy3List(enemy3)

        if self.flag1:
            self.x = mouseXsave2[1]
            self.y = mouseYsave2[1]
            self.flag1 = 0

        self.speed = 96

        if self.cld1 == 0:
            self.dir = math.atan2(self.enemy_y[0] - self.y, self.enemy_x[0] - self.x)
        if self.cld1 == 1:
            self.dir = math.atan2(self.enemy_y[1] - self.y, self.enemy_x[1] - self.x)
        if self.cld1 == 2:
            self.dir = math.atan2(self.enemy_y[2] - self.y, self.enemy_x[2] - self.x)
        if self.cld1 == 3:
            self.dir = math.atan2(self.enemy_y[3] - self.y, self.enemy_x[3] - self.x)
        if self.cld1 == 4:
            self.dir = math.atan2(self.enemy_y[4] - self.y, self.enemy_x[4] - self.x)
        if self.cld1 == 5:
            self.dir = math.atan2(self.enemy_y[5] - self.y, self.enemy_x[5] - self.x)
        if self.cld1 == 6:
            self.dir = math.atan2(self.enemy_y[6] - self.y, self.enemy_x[6] - self.x)
        if self.cld1 == 7:
            self.dir = math.atan2(self.enemy_y[7] - self.y, self.enemy_x[7] - self.x)
        if self.cld1 == 8:
            self.dir = math.atan2(self.enemy_y[8] - self.y, self.enemy_x[8] - self.x)
        if self.cld1 == 9:
            self.dir = math.atan2(self.enemy_y[9] - self.y, self.enemy_x[9] - self.x)
        if self.cld1 == 10:
            self.dir = math.atan2(self.enemy_y[10] - self.y, self.enemy_x[10] - self.x)
        if self.cld1 == 11:
            self.dir = math.atan2(self.enemy_y[11] - self.y, self.enemy_x[11] - self.x)
        if self.cld1 == 12:
            self.dir = math.atan2(self.enemy_y[12] - self.y, self.enemy_x[12] - self.x)
        if self.cld1 == 13:
            self.dir = math.atan2(self.enemy_y[13] - self.y, self.enemy_x[13] - self.x)
        if self.cld1 == 14:
            self.dir = math.atan2(self.enemy_y[14] - self.y, self.enemy_x[14] - self.x)
        if self.cld1 == 15:
            self.dir = math.atan2(self.enemy_y[15] - self.y, self.enemy_x[15] - self.x)
        if self.cld1 == 16:
            self.dir = math.atan2(self.enemy_y[16] - self.y, self.enemy_x[16] - self.x)
        if self.cld1 == 17:
            self.dir = math.atan2(self.enemy_y[17] - self.y, self.enemy_x[17] - self.x)
        if self.cld1 == 18:
            self.dir = math.atan2(self.enemy_y[18] - self.y, self.enemy_x[18] - self.x)
        if self.cld1 == 19:
            self.dir = math.atan2(self.enemy_y[19] - self.y, self.enemy_x[19] - self.x)

        self.time = game_framework.frame_time
        #print(self.time)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.collide():
            if self.cld1 == 0:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[0].x = 100000000
                enemy1[0].y = 100000000
                enemy2[0].x = 100000000
                enemy2[0].y = 100000000
                enemy3[0].x = 100000000
                enemy3[0].y = 100000000
                bullet.cld1 = 1
                bullet2.cld1 = 1
                bullet3.cld1 = 1
                bullet4.cld1 = 1
                bullet5.cld1 = 1
                bullet6.cld1 = 1
                bulletNum1 = 1
                grass.gold += 20
            elif self.cld1 == 1:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[1].x = 100000000
                enemy1[1].y = 100000000
                enemy2[1].x = 100000000
                enemy2[1].y = 100000000
                enemy3[1].x = 100000000
                enemy3[1].y = 100000000
                bullet.cld1 = 2
                bullet2.cld1 = 2
                bullet3.cld1 = 2
                bullet4.cld1 = 2
                bullet5.cld1 = 2
                bullet6.cld1 = 2
                bulletNum1 = 2
                grass.gold += 20
            elif self.cld1 == 2:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[2].x = 100000000
                enemy1[2].y = 100000000
                enemy2[2].x = 100000000
                enemy2[2].y = 100000000
                enemy3[2].x = 100000000
                enemy3[2].y = 100000000
                bullet.cld1 = 3
                bullet2.cld1 = 3
                bullet3.cld1 = 3
                bullet4.cld1 = 3
                bullet5.cld1 = 3
                bullet6.cld1 = 3
                bulletNum1 = 3
                grass.gold += 20
            elif self.cld1 == 3:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[3].x = 100000000
                enemy1[3].y = 100000000
                enemy2[3].x = 100000000
                enemy2[3].y = 100000000
                enemy3[3].x = 100000000
                enemy3[3].y = 100000000
                bullet.cld1 = 4
                bullet2.cld1 = 4
                bullet3.cld1 = 4
                bullet4.cld1 = 4
                bullet5.cld1 = 4
                bullet6.cld1 = 4
                bulletNum1 = 4
                grass.gold += 20
            elif self.cld1 == 4:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[4].x = 100000000
                enemy1[4].y = 100000000
                enemy2[4].x = 100000000
                enemy2[4].y = 100000000
                enemy3[4].x = 100000000
                enemy3[4].y = 100000000
                bullet.cld1 = 5
                bullet2.cld1 = 5
                bullet3.cld1 = 5
                bullet4.cld1 = 5
                bullet5.cld1 = 5
                bullet6.cld1 = 5
                bulletNum1 = 5
                grass.gold += 20
            elif self.cld1 == 5:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[5].x = 100000000
                enemy1[5].y = 100000000
                enemy2[5].x = 100000000
                enemy2[5].y = 100000000
                enemy3[5].x = 100000000
                enemy3[5].y = 100000000
                bullet.cld1 = 6
                bullet2.cld1 = 6
                bullet3.cld1 = 6
                bullet4.cld1 = 6
                bullet5.cld1 = 6
                bullet6.cld1 = 6
                bulletNum1 = 6
                grass.gold +=20
            elif self.cld1 == 6:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[6].x = 100000000
                enemy1[6].y = 100000000
                enemy2[6].x = 100000000
                enemy2[6].y = 100000000
                enemy3[6].x = 100000000
                enemy3[6].y = 100000000
                bullet.cld1 = 7
                bullet2.cld1 = 7
                bullet3.cld1 = 7
                bullet4.cld1 = 7
                bullet5.cld1 = 7
                bullet6.cld1 = 7
                bulletNum1 = 7
                grass.gold += 20
            elif self.cld1 == 7:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[7].x = 100000000
                enemy1[7].y = 100000000
                enemy2[7].x = 100000000
                enemy2[7].y = 100000000
                enemy3[7].x = 100000000
                enemy3[7].y = 100000000
                bullet.cld1 = 8
                bullet2.cld1 = 8
                bullet3.cld1 = 8
                bullet4.cld1 = 8
                bullet5.cld1 = 8
                bullet6.cld1 = 1
                bulletNum1 = 8
                grass.gold += 20
            elif self.cld1 == 8:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[8].x = 100000000
                enemy1[8].y = 100000000
                enemy2[8].x = 100000000
                enemy2[8].y = 100000000
                enemy3[8].x = 100000000
                enemy3[8].y = 100000000
                bullet.cld1 = 9
                bullet2.cld1 = 9
                bullet3.cld1 = 9
                bullet4.cld1 = 9
                bullet5.cld1 = 9
                bullet6.cld1 = 9
                bulletNum1 = 9
                grass.gold += 20
            elif self.cld1 == 9:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[9].x = 100000000
                enemy1[9].y = 100000000
                enemy2[9].x = 100000000
                enemy2[9].y = 100000000
                enemy3[9].x = 100000000
                enemy3[9].y = 100000000
                bullet.cld1 = 10
                bullet2.cld1 = 10
                bullet3.cld1 = 10
                bullet4.cld1 = 10
                bullet5.cld1 = 10
                bullet6.cld1 = 10
                bulletNum1 = 10
                grass.gold += 20
            elif self.cld1 == 10:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[10].x = 100000000
                enemy1[10].y = 100000000
                enemy2[10].x = 100000000
                enemy2[10].y = 100000000
                enemy3[10].x = 100000000
                enemy3[10].y = 100000000
                bullet.cld1 = 11
                bullet2.cld1 = 11
                bullet3.cld1 = 11
                bullet4.cld1 = 11
                bullet5.cld1 = 11
                bullet6.cld1 = 11
                bulletNum1 = 11
                grass.gold += 20
            elif self.cld1 == 11:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[11].x = 100000000
                enemy1[11].y = 100000000
                enemy2[11].x = 100000000
                enemy2[11].y = 100000000
                enemy3[11].x = 100000000
                enemy3[11].y = 100000000
                bullet.cld1 = 12
                bullet2.cld1 = 12
                bullet3.cld1 = 12
                bullet4.cld1 = 12
                bullet5.cld1 = 12
                bullet6.cld1 = 12
                bulletNum1 = 2
                grass.gold += 20
            elif self.cld1 == 12:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[12].x = 100000000
                enemy1[12].y = 100000000
                enemy2[12].x = 100000000
                enemy2[12].y = 100000000
                enemy3[12].x = 100000000
                enemy3[12].y = 100000000
                bullet.cld1 = 13
                bullet2.cld1 = 13
                bullet3.cld1 = 13
                bullet4.cld1 = 13
                bullet5.cld1 = 13
                bullet6.cld1 = 13
                bulletNum1 = 3
                grass.gold +=20
            elif self.cld1 == 13:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[13].x = 100000000
                enemy1[13].y = 100000000
                enemy2[13].x = 100000000
                enemy2[13].y = 100000000
                enemy3[13].x = 100000000
                enemy3[13].y = 100000000
                bullet.cld1 = 14
                bullet2.cld1 = 14
                bullet3.cld1 = 14
                bullet4.cld1 = 14
                bullet5.cld1 = 14
                bullet6.cld1 = 14
                bulletNum1 = 4
                grass.gold += 20
            elif self.cld1 == 14:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[14].x = 100000000
                enemy1[14].y = 100000000
                enemy2[14].x = 100000000
                enemy2[14].y = 100000000
                enemy3[14].x = 100000000
                enemy3[14].y = 100000000
                bullet.cld1 = 15
                bullet2.cld1 = 15
                bullet3.cld1 = 15
                bullet4.cld1 = 15
                bullet5.cld1 = 15
                bullet6.cld1 = 15
                bulletNum1 = 5
                grass.gold += 20
            elif self.cld1 == 15:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[15].x = 100000000
                enemy1[15].y = 100000000
                enemy2[15].x = 100000000
                enemy2[15].y = 100000000
                enemy3[15].x = 100000000
                enemy3[15].y = 100000000
                bullet.cld1 = 16
                bullet2.cld1 = 16
                bullet3.cld1 = 16
                bullet4.cld1 = 16
                bullet5.cld1 = 16
                bullet6.cld1 = 16
                bulletNum1 = 6
                grass.gold += 20
            elif self.cld1 == 16:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[16].x = 100000000
                enemy1[16].y = 100000000
                enemy2[16].x = 100000000
                enemy2[16].y = 100000000
                enemy3[16].x = 100000000
                enemy3[16].y = 100000000
                bullet.cld1 = 17
                bullet2.cld1 = 17
                bullet3.cld1 = 17
                bullet4.cld1 = 17
                bullet5.cld1 = 17
                bullet6.cld1 = 17
                bulletNum1 = 7
                grass.gold +=20
            elif self.cld1 == 17:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[17].x = 100000000
                enemy1[17].y = 100000000
                enemy2[17].x = 100000000
                enemy2[17].y = 100000000
                enemy3[17].x = 100000000
                enemy3[17].y = 100000000
                bullet.cld1 = 18
                bullet2.cld1 = 18
                bullet3.cld1 = 18
                bullet4.cld1 = 18
                bullet5.cld1 = 18
                bullet6.cld1 = 18
                bulletNum1 = 8
                grass.gold += 20
            elif self.cld1 == 18:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[18].x = 100000000
                enemy1[18].y = 100000000
                enemy2[18].x = 100000000
                enemy2[18].y = 100000000
                enemy3[18].x = 100000000
                enemy3[18].y = 100000000
                bullet.cld1 = 19
                bullet2.cld1 = 19
                bullet3.cld1 = 19
                bullet4.cld1 = 19
                bullet5.cld1 = 19
                bullet6.cld1 = 19
                bulletNum1 = 9
                grass.gold += 20
            elif self.cld1 == 19:
                self.x = mouseXsave2[1]
                self.y = mouseYsave2[1]
                enemy1[19].x = 100000000
                enemy1[19].y = 100000000
                enemy2[19].x = 100000000
                enemy2[19].y = 100000000
                enemy3[19].x = 100000000
                enemy3[19].y = 100000000
                bullet.cld1 = 20
                bullet2.cld1 = 20
                bullet3.cld1 = 20
                bullet4.cld1 = 20
                bullet5.cld1 = 20
                bullet6.cld1 = 20
                bulletNum1 = 20
                grass.gold += 20

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(206, 225, 14, 14, self.x, self.y)


class Bullet5:
    global bulletNum1

    def __init__(self):
        self.image = load_image('bullet.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.enemy_x = [0 for i in range(20)]
        self.enemy_y = [0 for i in range(20)]
        self.flag1 = 1
        self.dir = 0
        self.speed = 0
        self.time = 0
        self.cld1 = 0

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def setEnemy1List(self, enemy1):
        for i in range(0, 20):
            self.enemy_x[i] = enemy1[i].x
            self.enemy_y[i] = enemy1[i].y

    def setEnemy2List(self, enemy2):
        for i in range(0, 20):
            self.enemy_x[i] = enemy2[i].x
            self.enemy_y[i] = enemy2[i].y

    def setEnemy3List(self, enemy3):
        for i in range(0, 20):
            self.enemy_x[i] = enemy3[i].x
            self.enemy_y[i] = enemy3[i].y

    def collide(self):
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if self.cld1 == 0:
            if left_a > self.enemy_x[0] + 20: return False
            if right_a < self.enemy_x[0] - 20: return False
            if top_a < self.enemy_y[0] - 25: return False
            if bottom_a > self.enemy_y[0] + 25: return False
        if self.cld1 == 1:
            if left_a > self.enemy_x[1] + 20: return False
            if right_a < self.enemy_x[1] - 20: return False
            if top_a < self.enemy_y[1] - 25: return False
            if bottom_a > self.enemy_y[1] + 25: return False
        if self.cld1 == 2:
            if left_a > self.enemy_x[2] + 20: return False
            if right_a < self.enemy_x[2] - 20: return False
            if top_a < self.enemy_y[2] - 25: return False
            if bottom_a > self.enemy_y[2] + 25: return False
        if self.cld1 == 3:
            if left_a > self.enemy_x[3] + 20: return False
            if right_a < self.enemy_x[3] - 20: return False
            if top_a < self.enemy_y[3] - 25: return False
            if bottom_a > self.enemy_y[3] + 25: return False
        if self.cld1 == 4:
            if left_a > self.enemy_x[4] + 20: return False
            if right_a < self.enemy_x[4] - 20: return False
            if top_a < self.enemy_y[4] - 25: return False
            if bottom_a > self.enemy_y[4] + 25: return False
        if self.cld1 == 5:
            if left_a > self.enemy_x[5] + 20: return False
            if right_a < self.enemy_x[5] - 20: return False
            if top_a < self.enemy_y[5] - 25: return False
            if bottom_a > self.enemy_y[5] + 25: return False
        if self.cld1 == 6:
            if left_a > self.enemy_x[6] + 20: return False
            if right_a < self.enemy_x[6] - 20: return False
            if top_a < self.enemy_y[6] - 25: return False
            if bottom_a > self.enemy_y[6] + 25: return False
        if self.cld1 == 7:
            if left_a > self.enemy_x[7] + 20: return False
            if right_a < self.enemy_x[7] - 20: return False
            if top_a < self.enemy_y[7] - 25: return False
            if bottom_a > self.enemy_y[7] + 25: return False
        if self.cld1 == 8:
            if left_a > self.enemy_x[8] + 20: return False
            if right_a < self.enemy_x[8] - 20: return False
            if top_a < self.enemy_y[8] - 25: return False
            if bottom_a > self.enemy_y[8] + 25: return False
        if self.cld1 == 9:
            if left_a > self.enemy_x[9] + 20: return False
            if right_a < self.enemy_x[9] - 20: return False
            if top_a < self.enemy_y[9] - 25: return False
            if bottom_a > self.enemy_y[9] + 25: return False
        if self.cld1 == 10:
            if left_a > self.enemy_x[10] + 20: return False
            if right_a < self.enemy_x[10] - 20: return False
            if top_a < self.enemy_y[10] - 25: return False
            if bottom_a > self.enemy_y[10] + 25: return False
        if self.cld1 == 11:
            if left_a > self.enemy_x[11] + 20: return False
            if right_a < self.enemy_x[11] - 20: return False
            if top_a < self.enemy_y[11] - 25: return False
            if bottom_a > self.enemy_y[11] + 25: return False
        if self.cld1 == 12:
            if left_a > self.enemy_x[12] + 20: return False
            if right_a < self.enemy_x[12] - 20: return False
            if top_a < self.enemy_y[12] - 25: return False
            if bottom_a > self.enemy_y[12] + 25: return False
        if self.cld1 == 13:
            if left_a > self.enemy_x[13] + 20: return False
            if right_a < self.enemy_x[13] - 20: return False
            if top_a < self.enemy_y[13] - 25: return False
            if bottom_a > self.enemy_y[13] + 25: return False
        if self.cld1 == 14:
            if left_a > self.enemy_x[14] + 20: return False
            if right_a < self.enemy_x[14] - 20: return False
            if top_a < self.enemy_y[14] - 25: return False
            if bottom_a > self.enemy_y[14] + 25: return False
        if self.cld1 == 15:
            if left_a > self.enemy_x[15] + 20: return False
            if right_a < self.enemy_x[15] - 20: return False
            if top_a < self.enemy_y[15] - 25: return False
            if bottom_a > self.enemy_y[15] + 25: return False
        if self.cld1 == 16:
            if left_a > self.enemy_x[16] + 20: return False
            if right_a < self.enemy_x[16] - 20: return False
            if top_a < self.enemy_y[16] - 25: return False
            if bottom_a > self.enemy_y[16] + 25: return False
        if self.cld1 == 17:
            if left_a > self.enemy_x[17] + 20: return False
            if right_a < self.enemy_x[17] - 20: return False
            if top_a < self.enemy_y[17] - 25: return False
            if bottom_a > self.enemy_y[17] + 25: return False
        if self.cld1 == 18:
            if left_a > self.enemy_x[18] + 20: return False
            if right_a < self.enemy_x[18] - 20: return False
            if top_a < self.enemy_y[18] - 25: return False
            if bottom_a > self.enemy_y[18] + 25: return False
        if self.cld1 == 19:
            if left_a > self.enemy_x[19] + 20: return False
            if right_a < self.enemy_x[19] - 20: return False
            if top_a < self.enemy_y[19] - 25: return False
            if bottom_a > self.enemy_y[19] + 25: return False

        return True

    def update(self):
        global bulletNum1, stage
        self.frame = (self.frame + 1) % 1
        if stage == 1:
            self.setEnemy1List(enemy1)
        if stage == 2:
            self.setEnemy1List(enemy1)
        if stage == 3:
            self.setEnemy2List(enemy2)
        if stage == 4:
            self.setEnemy2List(enemy2)
        if stage == 5:
            self.setEnemy3List(enemy3)
        if stage == 6:
            self.setEnemy3List(enemy3)

        if self.flag1:
            self.x = mouseXsave3[0]
            self.y = mouseYsave3[0]
            self.flag1 = 0

        self.speed = 96

        if self.cld1 == 0:
            self.dir = math.atan2(self.enemy_y[0] - self.y, self.enemy_x[0] - self.x)
        if self.cld1 == 1:
            self.dir = math.atan2(self.enemy_y[1] - self.y, self.enemy_x[1] - self.x)
        if self.cld1 == 2:
            self.dir = math.atan2(self.enemy_y[2] - self.y, self.enemy_x[2] - self.x)
        if self.cld1 == 3:
            self.dir = math.atan2(self.enemy_y[3] - self.y, self.enemy_x[3] - self.x)
        if self.cld1 == 4:
            self.dir = math.atan2(self.enemy_y[4] - self.y, self.enemy_x[4] - self.x)
        if self.cld1 == 5:
            self.dir = math.atan2(self.enemy_y[5] - self.y, self.enemy_x[5] - self.x)
        if self.cld1 == 6:
            self.dir = math.atan2(self.enemy_y[6] - self.y, self.enemy_x[6] - self.x)
        if self.cld1 == 7:
            self.dir = math.atan2(self.enemy_y[7] - self.y, self.enemy_x[7] - self.x)
        if self.cld1 == 8:
            self.dir = math.atan2(self.enemy_y[8] - self.y, self.enemy_x[8] - self.x)
        if self.cld1 == 9:
            self.dir = math.atan2(self.enemy_y[9] - self.y, self.enemy_x[9] - self.x)
        if self.cld1 == 10:
            self.dir = math.atan2(self.enemy_y[10] - self.y, self.enemy_x[10] - self.x)
        if self.cld1 == 11:
            self.dir = math.atan2(self.enemy_y[11] - self.y, self.enemy_x[11] - self.x)
        if self.cld1 == 12:
            self.dir = math.atan2(self.enemy_y[12] - self.y, self.enemy_x[12] - self.x)
        if self.cld1 == 13:
            self.dir = math.atan2(self.enemy_y[13] - self.y, self.enemy_x[13] - self.x)
        if self.cld1 == 14:
            self.dir = math.atan2(self.enemy_y[14] - self.y, self.enemy_x[14] - self.x)
        if self.cld1 == 15:
            self.dir = math.atan2(self.enemy_y[15] - self.y, self.enemy_x[15] - self.x)
        if self.cld1 == 16:
            self.dir = math.atan2(self.enemy_y[16] - self.y, self.enemy_x[16] - self.x)
        if self.cld1 == 17:
            self.dir = math.atan2(self.enemy_y[17] - self.y, self.enemy_x[17] - self.x)
        if self.cld1 == 18:
            self.dir = math.atan2(self.enemy_y[18] - self.y, self.enemy_x[18] - self.x)
        if self.cld1 == 19:
            self.dir = math.atan2(self.enemy_y[19] - self.y, self.enemy_x[19] - self.x)

        self.time = game_framework.frame_time
        #print(self.time)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.collide():
            if self.cld1 == 0:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[0].x = 100000000
                enemy1[0].y = 100000000
                enemy2[0].x = 100000000
                enemy2[0].y = 100000000
                enemy3[0].x = 100000000
                enemy3[0].y = 100000000
                bullet.cld1 = 1
                bullet2.cld1 = 1
                bullet3.cld1 = 1
                bullet4.cld1 = 1
                bullet5.cld1 = 1
                bullet6.cld1 = 1
                bulletNum1 = 1
                grass.gold += 30
            elif self.cld1 == 1:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[1].x = 100000000
                enemy1[1].y = 100000000
                enemy2[1].x = 100000000
                enemy2[1].y = 100000000
                enemy3[1].x = 100000000
                enemy3[1].y = 100000000
                bullet.cld1 = 2
                bullet2.cld1 = 2
                bullet3.cld1 = 2
                bullet4.cld1 = 2
                bullet5.cld1 = 2
                bullet6.cld1 = 2
                bulletNum1 = 2
                grass.gold += 30
            elif self.cld1 == 2:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[2].x = 100000000
                enemy1[2].y = 100000000
                enemy2[2].x = 100000000
                enemy2[2].y = 100000000
                enemy3[2].x = 100000000
                enemy3[2].y = 100000000
                bullet.cld1 = 3
                bullet2.cld1 = 3
                bullet3.cld1 = 3
                bullet4.cld1 = 3
                bullet5.cld1 = 3
                bullet6.cld1 = 3
                bulletNum1 = 3
                grass.gold += 30
            elif self.cld1 == 3:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[3].x = 100000000
                enemy1[3].y = 100000000
                enemy2[3].x = 100000000
                enemy2[3].y = 100000000
                enemy3[3].x = 100000000
                enemy3[3].y = 100000000
                bullet.cld1 = 4
                bullet2.cld1 = 4
                bullet3.cld1 = 4
                bullet4.cld1 = 4
                bullet5.cld1 = 4
                bullet6.cld1 = 4
                bulletNum1 = 4
                grass.gold += 30
            elif self.cld1 == 4:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[4].x = 100000000
                enemy1[4].y = 100000000
                enemy2[4].x = 100000000
                enemy2[4].y = 100000000
                enemy3[4].x = 100000000
                enemy3[4].y = 100000000
                bullet.cld1 = 5
                bullet2.cld1 = 5
                bullet3.cld1 = 5
                bullet4.cld1 = 5
                bullet5.cld1 = 5
                bullet6.cld1 = 5
                bulletNum1 = 5
                grass.gold += 30
            elif self.cld1 == 5:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[5].x = 100000000
                enemy1[5].y = 100000000
                enemy2[5].x = 100000000
                enemy2[5].y = 100000000
                enemy3[5].x = 100000000
                enemy3[5].y = 100000000
                bullet.cld1 = 6
                bullet2.cld1 = 6
                bullet3.cld1 = 6
                bullet4.cld1 = 6
                bullet5.cld1 = 6
                bullet6.cld1 = 6
                bulletNum1 = 6
                grass.gold += 30
            elif self.cld1 == 6:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[6].x = 100000000
                enemy1[6].y = 100000000
                enemy2[6].x = 100000000
                enemy2[6].y = 100000000
                enemy3[6].x = 100000000
                enemy3[6].y = 100000000
                bullet.cld1 = 7
                bullet2.cld1 = 7
                bullet3.cld1 = 7
                bullet4.cld1 = 7
                bullet5.cld1 = 7
                bullet6.cld1 = 7
                bulletNum1 = 7
                grass.gold += 30
            elif self.cld1 == 7:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[7].x = 100000000
                enemy1[7].y = 100000000
                enemy2[7].x = 100000000
                enemy2[7].y = 100000000
                enemy3[7].x = 100000000
                enemy3[7].y = 100000000
                bullet.cld1 = 8
                bullet2.cld1 = 8
                bullet3.cld1 = 8
                bullet4.cld1 = 8
                bullet5.cld1 = 8
                bullet6.cld1 = 1
                bulletNum1 = 8
                grass.gold += 30
            elif self.cld1 == 8:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[8].x = 100000000
                enemy1[8].y = 100000000
                enemy2[8].x = 100000000
                enemy2[8].y = 100000000
                enemy3[8].x = 100000000
                enemy3[8].y = 100000000
                bullet.cld1 = 9
                bullet2.cld1 = 9
                bullet3.cld1 = 9
                bullet4.cld1 = 9
                bullet5.cld1 = 9
                bullet6.cld1 = 9
                bulletNum1 = 9
                grass.gold += 30
            elif self.cld1 == 9:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[9].x = 100000000
                enemy1[9].y = 100000000
                enemy2[9].x = 100000000
                enemy2[9].y = 100000000
                enemy3[9].x = 100000000
                enemy3[9].y = 100000000
                bullet.cld1 = 10
                bullet2.cld1 = 10
                bullet3.cld1 = 10
                bullet4.cld1 = 10
                bullet5.cld1 = 10
                bullet6.cld1 = 10
                bulletNum1 = 10
                grass.gold += 30
            elif self.cld1 == 10:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[10].x = 100000000
                enemy1[10].y = 100000000
                enemy2[10].x = 100000000
                enemy2[10].y = 100000000
                enemy3[10].x = 100000000
                enemy3[10].y = 100000000
                bullet.cld1 = 11
                bullet2.cld1 = 11
                bullet3.cld1 = 11
                bullet4.cld1 = 11
                bullet5.cld1 = 11
                bullet6.cld1 = 11
                bulletNum1 = 11
                grass.gold += 30
            elif self.cld1 == 11:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[11].x = 100000000
                enemy1[11].y = 100000000
                enemy2[11].x = 100000000
                enemy2[11].y = 100000000
                enemy3[11].x = 100000000
                enemy3[11].y = 100000000
                bullet.cld1 = 12
                bullet2.cld1 = 12
                bullet3.cld1 = 12
                bullet4.cld1 = 12
                bullet5.cld1 = 12
                bullet6.cld1 = 12
                bulletNum1 = 2
                grass.gold += 30
            elif self.cld1 == 12:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[12].x = 100000000
                enemy1[12].y = 100000000
                enemy2[12].x = 100000000
                enemy2[12].y = 100000000
                enemy3[12].x = 100000000
                enemy3[12].y = 100000000
                bullet.cld1 = 13
                bullet2.cld1 = 13
                bullet3.cld1 = 13
                bullet4.cld1 = 13
                bullet5.cld1 = 13
                bullet6.cld1 = 13
                bulletNum1 = 3
                grass.gold += 30
            elif self.cld1 == 13:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[13].x = 100000000
                enemy1[13].y = 100000000
                enemy2[13].x = 100000000
                enemy2[13].y = 100000000
                enemy3[13].x = 100000000
                enemy3[13].y = 100000000
                bullet.cld1 = 14
                bullet2.cld1 = 14
                bullet3.cld1 = 14
                bullet4.cld1 = 14
                bullet5.cld1 = 14
                bullet6.cld1 = 14
                bulletNum1 = 4
                grass.gold += 30
            elif self.cld1 == 14:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[14].x = 100000000
                enemy1[14].y = 100000000
                enemy2[14].x = 100000000
                enemy2[14].y = 100000000
                enemy3[14].x = 100000000
                enemy3[14].y = 100000000
                bullet.cld1 = 15
                bullet2.cld1 = 15
                bullet3.cld1 = 15
                bullet4.cld1 = 15
                bullet5.cld1 = 15
                bullet6.cld1 = 15
                bulletNum1 = 5
                grass.gold += 30
            elif self.cld1 == 15:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[15].x = 100000000
                enemy1[15].y = 100000000
                enemy2[15].x = 100000000
                enemy2[15].y = 100000000
                enemy3[15].x = 100000000
                enemy3[15].y = 100000000
                bullet.cld1 = 16
                bullet2.cld1 = 16
                bullet3.cld1 = 16
                bullet4.cld1 = 16
                bullet5.cld1 = 16
                bullet6.cld1 = 16
                bulletNum1 = 6
                grass.gold += 30
            elif self.cld1 == 16:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[16].x = 100000000
                enemy1[16].y = 100000000
                enemy2[16].x = 100000000
                enemy2[16].y = 100000000
                enemy3[16].x = 100000000
                enemy3[16].y = 100000000
                bullet.cld1 = 17
                bullet2.cld1 = 17
                bullet3.cld1 = 17
                bullet4.cld1 = 17
                bullet5.cld1 = 17
                bullet6.cld1 = 17
                bulletNum1 = 7
                grass.gold += 30
            elif self.cld1 == 17:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[17].x = 100000000
                enemy1[17].y = 100000000
                enemy2[17].x = 100000000
                enemy2[17].y = 100000000
                enemy3[17].x = 100000000
                enemy3[17].y = 100000000
                bullet.cld1 = 18
                bullet2.cld1 = 18
                bullet3.cld1 = 18
                bullet4.cld1 = 18
                bullet5.cld1 = 18
                bullet6.cld1 = 18
                bulletNum1 = 8
                grass.gold += 30
            elif self.cld1 == 18:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[18].x = 100000000
                enemy1[18].y = 100000000
                enemy2[18].x = 100000000
                enemy2[18].y = 100000000
                enemy3[18].x = 100000000
                enemy3[18].y = 100000000
                bullet.cld1 = 19
                bullet2.cld1 = 19
                bullet3.cld1 = 19
                bullet4.cld1 = 19
                bullet5.cld1 = 19
                bullet6.cld1 = 19
                bulletNum1 = 9
                grass.gold += 30
            elif self.cld1 == 19:
                self.x = mouseXsave3[0]
                self.y = mouseYsave3[0]
                enemy1[19].x = 100000000
                enemy1[19].y = 100000000
                enemy2[19].x = 100000000
                enemy2[19].y = 100000000
                enemy3[19].x = 100000000
                enemy3[19].y = 100000000
                bullet.cld1 = 20
                bullet2.cld1 = 20
                bullet3.cld1 = 20
                bullet4.cld1 = 20
                bullet5.cld1 = 20
                bullet6.cld1 = 20
                bulletNum1 = 20
                grass.gold += 30

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(236, 180, 14, 14, self.x, self.y)


class Bullet6:
    global bulletNum1

    def __init__(self):
        self.image = load_image('bullet.png')
        self.frame = 0
        self.x = 0
        self.y = 0
        self.enemy_x = [0 for i in range(20)]
        self.enemy_y = [0 for i in range(20)]
        self.flag1 = 1
        self.dir = 0
        self.speed = 0
        self.time = 0
        self.cld1 = 0

    def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7

    def setEnemy1List(self, enemy1):
        for i in range(0, 20):
            self.enemy_x[i] = enemy1[i].x
            self.enemy_y[i] = enemy1[i].y

    def setEnemy2List(self, enemy2):
        for i in range(0, 20):
            self.enemy_x[i] = enemy2[i].x
            self.enemy_y[i] = enemy2[i].y

    def setEnemy3List(self, enemy3):
        for i in range(0, 20):
            self.enemy_x[i] = enemy3[i].x
            self.enemy_y[i] = enemy3[i].y

    def collide(self):
        left_a, bottom_a, right_a, top_a = self.get_bb()

        if self.cld1 == 0:
            if left_a > self.enemy_x[0] + 20: return False
            if right_a < self.enemy_x[0] - 20: return False
            if top_a < self.enemy_y[0] - 25: return False
            if bottom_a > self.enemy_y[0] + 25: return False
        if self.cld1 == 1:
            if left_a > self.enemy_x[1] + 20: return False
            if right_a < self.enemy_x[1] - 20: return False
            if top_a < self.enemy_y[1] - 25: return False
            if bottom_a > self.enemy_y[1] + 25: return False
        if self.cld1 == 2:
            if left_a > self.enemy_x[2] + 20: return False
            if right_a < self.enemy_x[2] - 20: return False
            if top_a < self.enemy_y[2] - 25: return False
            if bottom_a > self.enemy_y[2] + 25: return False
        if self.cld1 == 3:
            if left_a > self.enemy_x[3] + 20: return False
            if right_a < self.enemy_x[3] - 20: return False
            if top_a < self.enemy_y[3] - 25: return False
            if bottom_a > self.enemy_y[3] + 25: return False
        if self.cld1 == 4:
            if left_a > self.enemy_x[4] + 20: return False
            if right_a < self.enemy_x[4] - 20: return False
            if top_a < self.enemy_y[4] - 25: return False
            if bottom_a > self.enemy_y[4] + 25: return False
        if self.cld1 == 5:
            if left_a > self.enemy_x[5] + 20: return False
            if right_a < self.enemy_x[5] - 20: return False
            if top_a < self.enemy_y[5] - 25: return False
            if bottom_a > self.enemy_y[5] + 25: return False
        if self.cld1 == 6:
            if left_a > self.enemy_x[6] + 20: return False
            if right_a < self.enemy_x[6] - 20: return False
            if top_a < self.enemy_y[6] - 25: return False
            if bottom_a > self.enemy_y[6] + 25: return False
        if self.cld1 == 7:
            if left_a > self.enemy_x[7] + 20: return False
            if right_a < self.enemy_x[7] - 20: return False
            if top_a < self.enemy_y[7] - 25: return False
            if bottom_a > self.enemy_y[7] + 25: return False
        if self.cld1 == 8:
            if left_a > self.enemy_x[8] + 20: return False
            if right_a < self.enemy_x[8] - 20: return False
            if top_a < self.enemy_y[8] - 25: return False
            if bottom_a > self.enemy_y[8] + 25: return False
        if self.cld1 == 9:
            if left_a > self.enemy_x[9] + 20: return False
            if right_a < self.enemy_x[9] - 20: return False
            if top_a < self.enemy_y[9] - 25: return False
            if bottom_a > self.enemy_y[9] + 25: return False
        if self.cld1 == 10:
            if left_a > self.enemy_x[10] + 20: return False
            if right_a < self.enemy_x[10] - 20: return False
            if top_a < self.enemy_y[10] - 25: return False
            if bottom_a > self.enemy_y[10] + 25: return False
        if self.cld1 == 11:
            if left_a > self.enemy_x[11] + 20: return False
            if right_a < self.enemy_x[11] - 20: return False
            if top_a < self.enemy_y[11] - 25: return False
            if bottom_a > self.enemy_y[11] + 25: return False
        if self.cld1 == 12:
            if left_a > self.enemy_x[12] + 20: return False
            if right_a < self.enemy_x[12] - 20: return False
            if top_a < self.enemy_y[12] - 25: return False
            if bottom_a > self.enemy_y[12] + 25: return False
        if self.cld1 == 13:
            if left_a > self.enemy_x[13] + 20: return False
            if right_a < self.enemy_x[13] - 20: return False
            if top_a < self.enemy_y[13] - 25: return False
            if bottom_a > self.enemy_y[13] + 25: return False
        if self.cld1 == 14:
            if left_a > self.enemy_x[14] + 20: return False
            if right_a < self.enemy_x[14] - 20: return False
            if top_a < self.enemy_y[14] - 25: return False
            if bottom_a > self.enemy_y[14] + 25: return False
        if self.cld1 == 15:
            if left_a > self.enemy_x[15] + 20: return False
            if right_a < self.enemy_x[15] - 20: return False
            if top_a < self.enemy_y[15] - 25: return False
            if bottom_a > self.enemy_y[15] + 25: return False
        if self.cld1 == 16:
            if left_a > self.enemy_x[16] + 20: return False
            if right_a < self.enemy_x[16] - 20: return False
            if top_a < self.enemy_y[16] - 25: return False
            if bottom_a > self.enemy_y[16] + 25: return False
        if self.cld1 == 17:
            if left_a > self.enemy_x[17] + 20: return False
            if right_a < self.enemy_x[17] - 20: return False
            if top_a < self.enemy_y[17] - 25: return False
            if bottom_a > self.enemy_y[17] + 25: return False
        if self.cld1 == 18:
            if left_a > self.enemy_x[18] + 20: return False
            if right_a < self.enemy_x[18] - 20: return False
            if top_a < self.enemy_y[18] - 25: return False
            if bottom_a > self.enemy_y[18] + 25: return False
        if self.cld1 == 19:
            if left_a > self.enemy_x[19] + 20: return False
            if right_a < self.enemy_x[19] - 20: return False
            if top_a < self.enemy_y[19] - 25: return False
            if bottom_a > self.enemy_y[19] + 25: return False

        return True

    def update(self):
        global bulletNum1, stage
        self.frame = (self.frame + 1) % 1
        if stage == 1:
            self.setEnemy1List(enemy1)
        if stage == 2:
            self.setEnemy1List(enemy1)
        if stage == 3:
            self.setEnemy2List(enemy2)
        if stage == 4:
            self.setEnemy2List(enemy2)
        if stage == 5:
            self.setEnemy3List(enemy3)
        if stage == 6:
            self.setEnemy3List(enemy3)

        if self.flag1:
            self.x = mouseXsave3[1]
            self.y = mouseYsave3[1]
            self.flag1 = 0

        self.speed = 96

        if self.cld1 == 0:
            self.dir = math.atan2(self.enemy_y[0] - self.y, self.enemy_x[0] - self.x)
        if self.cld1 == 1:
            self.dir = math.atan2(self.enemy_y[1] - self.y, self.enemy_x[1] - self.x)
        if self.cld1 == 2:
            self.dir = math.atan2(self.enemy_y[2] - self.y, self.enemy_x[2] - self.x)
        if self.cld1 == 3:
            self.dir = math.atan2(self.enemy_y[3] - self.y, self.enemy_x[3] - self.x)
        if self.cld1 == 4:
            self.dir = math.atan2(self.enemy_y[4] - self.y, self.enemy_x[4] - self.x)
        if self.cld1 == 5:
            self.dir = math.atan2(self.enemy_y[5] - self.y, self.enemy_x[5] - self.x)
        if self.cld1 == 6:
            self.dir = math.atan2(self.enemy_y[6] - self.y, self.enemy_x[6] - self.x)
        if self.cld1 == 7:
            self.dir = math.atan2(self.enemy_y[7] - self.y, self.enemy_x[7] - self.x)
        if self.cld1 == 8:
            self.dir = math.atan2(self.enemy_y[8] - self.y, self.enemy_x[8] - self.x)
        if self.cld1 == 9:
            self.dir = math.atan2(self.enemy_y[9] - self.y, self.enemy_x[9] - self.x)
        if self.cld1 == 10:
            self.dir = math.atan2(self.enemy_y[10] - self.y, self.enemy_x[10] - self.x)
        if self.cld1 == 11:
            self.dir = math.atan2(self.enemy_y[11] - self.y, self.enemy_x[11] - self.x)
        if self.cld1 == 12:
            self.dir = math.atan2(self.enemy_y[12] - self.y, self.enemy_x[12] - self.x)
        if self.cld1 == 13:
            self.dir = math.atan2(self.enemy_y[13] - self.y, self.enemy_x[13] - self.x)
        if self.cld1 == 14:
            self.dir = math.atan2(self.enemy_y[14] - self.y, self.enemy_x[14] - self.x)
        if self.cld1 == 15:
            self.dir = math.atan2(self.enemy_y[15] - self.y, self.enemy_x[15] - self.x)
        if self.cld1 == 16:
            self.dir = math.atan2(self.enemy_y[16] - self.y, self.enemy_x[16] - self.x)
        if self.cld1 == 17:
            self.dir = math.atan2(self.enemy_y[17] - self.y, self.enemy_x[17] - self.x)
        if self.cld1 == 18:
            self.dir = math.atan2(self.enemy_y[18] - self.y, self.enemy_x[18] - self.x)
        if self.cld1 == 19:
            self.dir = math.atan2(self.enemy_y[19] - self.y, self.enemy_x[19] - self.x)

        self.time = game_framework.frame_time
        #print(self.time)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        if self.collide():
            if self.cld1 == 0:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[0].x = 100000000
                enemy1[0].y = 100000000
                enemy2[0].x = 100000000
                enemy2[0].y = 100000000
                enemy3[0].x = 100000000
                enemy3[0].y = 100000000
                bullet.cld1 = 1
                bullet2.cld1 = 1
                bullet3.cld1 = 1
                bullet4.cld1 = 1
                bullet5.cld1 = 1
                bullet6.cld1 = 1
                bulletNum1 = 1
                grass.gold += 30
            elif self.cld1 == 1:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[1].x = 100000000
                enemy1[1].y = 100000000
                enemy2[1].x = 100000000
                enemy2[1].y = 100000000
                enemy3[1].x = 100000000
                enemy3[1].y = 100000000
                bullet.cld1 = 2
                bullet2.cld1 = 2
                bullet3.cld1 = 2
                bullet4.cld1 = 2
                bullet5.cld1 = 2
                bullet6.cld1 = 2
                bulletNum1 = 2
                grass.gold += 30
            elif self.cld1 == 2:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[2].x = 100000000
                enemy1[2].y = 100000000
                enemy2[2].x = 100000000
                enemy2[2].y = 100000000
                enemy3[2].x = 100000000
                enemy3[2].y = 100000000
                bullet.cld1 = 3
                bullet2.cld1 = 3
                bullet3.cld1 = 3
                bullet4.cld1 = 3
                bullet5.cld1 = 3
                bullet6.cld1 = 3
                bulletNum1 = 3
                grass.gold += 30
            elif self.cld1 == 3:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[3].x = 100000000
                enemy1[3].y = 100000000
                enemy2[3].x = 100000000
                enemy2[3].y = 100000000
                enemy3[3].x = 100000000
                enemy3[3].y = 100000000
                bullet.cld1 = 4
                bullet2.cld1 = 4
                bullet3.cld1 = 4
                bullet4.cld1 = 4
                bullet5.cld1 = 4
                bullet6.cld1 = 4
                bulletNum1 = 4
                grass.gold += 30
            elif self.cld1 == 4:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[4].x = 100000000
                enemy1[4].y = 100000000
                enemy2[4].x = 100000000
                enemy2[4].y = 100000000
                enemy3[4].x = 100000000
                enemy3[4].y = 100000000
                bullet.cld1 = 5
                bullet2.cld1 = 5
                bullet3.cld1 = 5
                bullet4.cld1 = 5
                bullet5.cld1 = 5
                bullet6.cld1 = 5
                bulletNum1 = 5
                grass.gold += 30
            elif self.cld1 == 5:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[5].x = 100000000
                enemy1[5].y = 100000000
                enemy2[5].x = 100000000
                enemy2[5].y = 100000000
                enemy3[5].x = 100000000
                enemy3[5].y = 100000000
                bullet.cld1 = 6
                bullet2.cld1 = 6
                bullet3.cld1 = 6
                bullet4.cld1 = 6
                bullet5.cld1 = 6
                bullet6.cld1 = 6
                bulletNum1 = 6
                grass.gold += 30
            elif self.cld1 == 6:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[6].x = 100000000
                enemy1[6].y = 100000000
                enemy2[6].x = 100000000
                enemy2[6].y = 100000000
                enemy3[6].x = 100000000
                enemy3[6].y = 100000000
                bullet.cld1 = 7
                bullet2.cld1 = 7
                bullet3.cld1 = 7
                bullet4.cld1 = 7
                bullet5.cld1 = 7
                bullet6.cld1 = 7
                bulletNum1 = 7
                grass.gold += 30
            elif self.cld1 == 7:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[7].x = 100000000
                enemy1[7].y = 100000000
                enemy2[7].x = 100000000
                enemy2[7].y = 100000000
                enemy3[7].x = 100000000
                enemy3[7].y = 100000000
                bullet.cld1 = 8
                bullet2.cld1 = 8
                bullet3.cld1 = 8
                bullet4.cld1 = 8
                bullet5.cld1 = 8
                bullet6.cld1 = 1
                bulletNum1 = 8
                grass.gold += 30
            elif self.cld1 == 8:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[8].x = 100000000
                enemy1[8].y = 100000000
                enemy2[8].x = 100000000
                enemy2[8].y = 100000000
                enemy3[8].x = 100000000
                enemy3[8].y = 100000000
                bullet.cld1 = 9
                bullet2.cld1 = 9
                bullet3.cld1 = 9
                bullet4.cld1 = 9
                bullet5.cld1 = 9
                bullet6.cld1 = 9
                bulletNum1 = 9
                grass.gold += 30
            elif self.cld1 == 9:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[9].x = 100000000
                enemy1[9].y = 100000000
                enemy2[9].x = 100000000
                enemy2[9].y = 100000000
                enemy3[9].x = 100000000
                enemy3[9].y = 100000000
                bullet.cld1 = 10
                bullet2.cld1 = 10
                bullet3.cld1 = 10
                bullet4.cld1 = 10
                bullet5.cld1 = 10
                bullet6.cld1 = 10
                bulletNum1 = 10
                grass.gold += 30
            elif self.cld1 == 10:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[10].x = 100000000
                enemy1[10].y = 100000000
                enemy2[10].x = 100000000
                enemy2[10].y = 100000000
                enemy3[10].x = 100000000
                enemy3[10].y = 100000000
                bullet.cld1 = 11
                bullet2.cld1 = 11
                bullet3.cld1 = 11
                bullet4.cld1 = 11
                bullet5.cld1 = 11
                bullet6.cld1 = 11
                bulletNum1 = 11
                grass.gold += 30
            elif self.cld1 == 11:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[11].x = 100000000
                enemy1[11].y = 100000000
                enemy2[11].x = 100000000
                enemy2[11].y = 100000000
                enemy3[11].x = 100000000
                enemy3[11].y = 100000000
                bullet.cld1 = 12
                bullet2.cld1 = 12
                bullet3.cld1 = 12
                bullet4.cld1 = 12
                bullet5.cld1 = 12
                bullet6.cld1 = 12
                bulletNum1 = 2
                grass.gold += 30
            elif self.cld1 == 12:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[12].x = 100000000
                enemy1[12].y = 100000000
                enemy2[12].x = 100000000
                enemy2[12].y = 100000000
                enemy3[12].x = 100000000
                enemy3[12].y = 100000000
                bullet.cld1 = 13
                bullet2.cld1 = 13
                bullet3.cld1 = 13
                bullet4.cld1 = 13
                bullet5.cld1 = 13
                bullet6.cld1 = 13
                bulletNum1 = 3
                grass.gold += 30
            elif self.cld1 == 13:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[13].x = 100000000
                enemy1[13].y = 100000000
                enemy2[13].x = 100000000
                enemy2[13].y = 100000000
                enemy3[13].x = 100000000
                enemy3[13].y = 100000000
                bullet.cld1 = 14
                bullet2.cld1 = 14
                bullet3.cld1 = 14
                bullet4.cld1 = 14
                bullet5.cld1 = 14
                bullet6.cld1 = 14
                bulletNum1 = 4
                grass.gold += 30
            elif self.cld1 == 14:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[14].x = 100000000
                enemy1[14].y = 100000000
                enemy2[14].x = 100000000
                enemy2[14].y = 100000000
                enemy3[14].x = 100000000
                enemy3[14].y = 100000000
                bullet.cld1 = 15
                bullet2.cld1 = 15
                bullet3.cld1 = 15
                bullet4.cld1 = 15
                bullet5.cld1 = 15
                bullet6.cld1 = 15
                bulletNum1 = 5
                grass.gold += 30
            elif self.cld1 == 15:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[15].x = 100000000
                enemy1[15].y = 100000000
                enemy2[15].x = 100000000
                enemy2[15].y = 100000000
                enemy3[15].x = 100000000
                enemy3[15].y = 100000000
                bullet.cld1 = 16
                bullet2.cld1 = 16
                bullet3.cld1 = 16
                bullet4.cld1 = 16
                bullet5.cld1 = 16
                bullet6.cld1 = 16
                bulletNum1 = 6
                grass.gold += 30
            elif self.cld1 == 16:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[16].x = 100000000
                enemy1[16].y = 100000000
                enemy2[16].x = 100000000
                enemy2[16].y = 100000000
                enemy3[16].x = 100000000
                enemy3[16].y = 100000000
                bullet.cld1 = 17
                bullet2.cld1 = 17
                bullet3.cld1 = 17
                bullet4.cld1 = 17
                bullet5.cld1 = 17
                bullet6.cld1 = 17
                bulletNum1 = 7
                grass.gold += 30
            elif self.cld1 == 17:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[17].x = 100000000
                enemy1[17].y = 100000000
                enemy2[17].x = 100000000
                enemy2[17].y = 100000000
                enemy3[17].x = 100000000
                enemy3[17].y = 100000000
                bullet.cld1 = 18
                bullet2.cld1 = 18
                bullet3.cld1 = 18
                bullet4.cld1 = 18
                bullet5.cld1 = 18
                bullet6.cld1 = 18
                bulletNum1 = 8
                grass.gold += 30
            elif self.cld1 == 18:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[18].x = 100000000
                enemy1[18].y = 100000000
                enemy2[18].x = 100000000
                enemy2[18].y = 100000000
                enemy3[18].x = 100000000
                enemy3[18].y = 100000000
                bullet.cld1 = 19
                bullet2.cld1 = 19
                bullet3.cld1 = 19
                bullet4.cld1 = 19
                bullet5.cld1 = 19
                bullet6.cld1 = 19
                bulletNum1 = 9
                grass.gold += 30
            elif self.cld1 == 19:
                self.x = mouseXsave3[1]
                self.y = mouseYsave3[1]
                enemy1[19].x = 100000000
                enemy1[19].y = 100000000
                enemy2[19].x = 100000000
                enemy2[19].y = 100000000
                enemy3[19].x = 100000000
                enemy3[19].y = 100000000
                bullet.cld1 = 20
                bullet2.cld1 = 20
                bullet3.cld1 = 20
                bullet4.cld1 = 20
                bullet5.cld1 = 20
                bullet6.cld1 = 20
                bulletNum1 = 20
                grass.gold += 30

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(236, 180, 14, 14, self.x, self.y)


def exit():
    global enemy1, enemy2, enemy3, tower1, tower2, tower3, grass
    for i in range(0, 100):
        del(enemy1[i])
    for i in range(0, 100):
        del(enemy2[i])
    for i in range(0, 100):
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
    global mouseXsave2, mouseYsave2, mouseFlag2, mouseNum2
    global mouseXsave3, mouseYsave3, mouseFlag3, mouseNum3
    global start_time, stage, bulletNum1
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
                            if grass.gold > 0:
                                mouseFlag1[mouseNum1] = True
            if 718 <= event.x:
                if event.x <= 770:
                    if 175 <= event.y:
                        if event.y <= 245:
                            if grass.gold > 0:
                                mouseFlag2[mouseNum2] = True
            if 782 <= event.x:
                if event.x <= 830:
                    if 175 <= event.y:
                        if event.y <= 245:
                            if grass.gold > 0:
                                mouseFlag3[mouseNum3] = True
            if 640 <= event.x:
                if event.x <= 890:
                    if 340 <= event.y:
                        if event.y <= 395:
                            start_time = get_time()
                            stage += 1
                            for i in range(20):
                                enemy1[i].x, enemy1[i].y = 100, 640
                                enemy2[i].x, enemy2[i].y = 100, 640
                                enemy3[i].x, enemy3[i].y = 100, 640

                                for j in range(14):
                                    enemy1[i].flag[j] = False
                                    enemy2[i].flag[j] = False
                                    enemy3[i].flag[j] = False

                                enemy1[i].flag[0] = True
                                enemy2[i].flag[0] = True
                                enemy3[i].flag[0] = True
                            bullet.cld1 = 0
                            bullet2.cld1 = 0
                            bullet3.cld1 = 0
                            bullet4.cld1 = 0
                            bullet5.cld1 = 0
                            bullet6.cld1 = 0
                            bulletNum1 = 0

        elif event.type == SDL_MOUSEBUTTONUP:
            if mouseFlag1[mouseNum1]:
                mouseXsave1[mouseNum1], mouseYsave1[mouseNum1] = event.x, 640 - 1 - event.y
                print(mouseXsave1[mouseNum1], mouseYsave1[mouseNum1])
                mouseNum1 += 1
                grass.gold -= 100
            elif mouseFlag2[mouseNum2]:
                mouseXsave2[mouseNum2], mouseYsave2[mouseNum2] = event.x, 640 - 1 - event.y
                print(mouseXsave2[mouseNum2], mouseYsave2[mouseNum2])
                mouseNum2 += 1
                grass.gold -= 200
            elif mouseFlag3[mouseNum3]:
                mouseXsave3[mouseNum3], mouseYsave3[mouseNum3] = event.x, 640 - 1 - event.y
                print(mouseXsave3[mouseNum3], mouseYsave3[mouseNum3])
                mouseNum3 += 1
                grass.gold -= 300
            else:
                pass


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_a: return False
    if bottom_a > top_b: return False

    return True


time = 0


def update():
    global time, first_time, start_time, bulletNum1, stage

    if start_time > 0:
        time = get_time() - first_time - start_time
    #print(time)

    if stage == 1:
        for i in range(10):
            if time > i:
                enemy1[i].update()

    if stage == 2:
        for i in range(20):
            if time > i:
                enemy1[i].update()

    if stage == 3:
        for i in range(10):
            if time > i:
                enemy2[i].update()

    if stage == 4:
        for i in range(20):
            if time > i:
                enemy2[i].update()

    if stage == 5:
        for i in range(10):
            if time > i:
                enemy3[i].update()

    if stage == 6:
        for i in range(20):
            if time > i:
                enemy3[i].update()

    for i in range(20):
        i += bulletNum1
        if enemy1[i].collide():
            bullet.update()
        if enemy1[i].collide2():
            bullet2.update()
        if enemy1[i].collide_1():
            bullet.update()
        if enemy1[i].collide2_1():
            bullet2.update()
        if enemy1[i].collide_2():
            bullet.update()
        if enemy1[i].collide2_2():
            bullet2.update()
        #if enemy1[i].collide3():
        #    bullet.update()
        if enemy2[i].collide():
            bullet3.update()
        if enemy2[i].collide2():
            bullet4.update()
        if enemy2[i].collide_1():
            bullet3.update()
        if enemy2[i].collide2_1():
            bullet4.update()
        if enemy2[i].collide_2():
            bullet3.update()
        if enemy2[i].collide2_2():
            bullet4.update()
        #if enemy1[i].collide3_1():
        #    bullet.update()
        if enemy3[i].collide():
            bullet5.update()
        if enemy3[i].collide2():
            bullet6.update()
        if enemy3[i].collide_1():
            bullet5.update()
        if enemy3[i].collide2_1():
            bullet6.update()
        if enemy3[i].collide_2():
            bullet5.update()
        if enemy3[i].collide2_2():
            bullet6.update()
        #if enemy1[i].collide3_2():
        #    bullet.update()

    tower1.update()
    tower2.update()
    tower3.update()
    hide_cursor()


def draw():
    global time, bulletNum1
    clear_canvas()
    grass.draw()

    if stage == 1:
        for i in range(10):
            if time > i:
                enemy1[i].draw()

    if stage == 2:
        for i in range(20):
            if time > i:
                enemy1[i].draw()

    if stage == 3:
        for i in range(10):
            if time > i:
                enemy2[i].draw()

    if stage == 4:
        for i in range(20):
            if time > i:
                enemy2[i].draw()

    if stage == 5:
        for i in range(10):
            if time > i:
                enemy3[i].draw()

    if stage == 6:
        for i in range(20):
            if time > i:
                enemy3[i].draw()

    for i in range(20):
        i += bulletNum1
        if enemy1[i].collide():
            bullet.draw()
        if enemy1[i].collide2():
            bullet2.draw()
        if enemy2[i].collide():
            bullet3.draw()
        if enemy2[i].collide2():
            bullet4.draw()
        if enemy3[i].collide():
            bullet5.draw()
        if enemy3[i].collide2():
            bullet6.draw()
        #if enemy1[i].collide3():
        #    bullet.draw()
        if enemy1[i].collide_1():
            bullet.draw()
        if enemy1[i].collide2_1():
            bullet2.draw()
        if enemy2[i].collide_1():
            bullet3.draw()
        if enemy2[i].collide2_1():
            bullet4.draw()
        if enemy3[i].collide_1():
            bullet5.draw()
        if enemy3[i].collide2_1():
            bullet6.draw()
        #if enemy1[i].collide3_1():
        #    bullet.draw()
        if enemy1[i].collide_2():
            bullet.draw()
        if enemy1[i].collide2_2():
            bullet2.draw()
        if enemy2[i].collide_2():
            bullet3.draw()
        if enemy2[i].collide2_2():
            bullet4.draw()
        if enemy3[i].collide_2():
            bullet5.draw()
        if enemy3[i].collide2_2():
            bullet6.draw()
        #if enemy1[i].collide3_2():
        #    bullet.draw()

    arrow.draw()

    tower1.draw()
    tower2.draw()
    tower3.draw()


    update_canvas()





