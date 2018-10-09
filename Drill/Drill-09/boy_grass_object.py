from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class smallBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.image = load_image('ball21x21.png')
        self.speedY = random.randint(1, 3)

    def update(self):
        for i in range(0, smallballnum):
            if self.y >= 60:
                self.y -= self.speedY / 3

    def draw(self):
        self.image.draw(self.x, self.y)


class bigBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.image = load_image('ball41x41.png')
        self.speedY = random.randint(1, 3)

    def update(self):
        for i in range(0, bigballnum):
            if self.y >= 70:
                self.y -= self.speedY / 3

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()

smallballnum = random.randint(0, 20)
bigballnum = 20 - smallballnum
print(smallballnum, bigballnum)

grass = Grass()
boy = Boy()
sball = smallBall()
bball = bigBall()

team = [Boy() for i in range(11)]
Sballs = [smallBall() for i in range(smallballnum)]
Bballs = [bigBall() for i in range(bigballnum)]

running = True;

# game main loop code
while running:
    handle_events()

    for sball in Sballs:
        sball.update()
    for bball in Bballs:
        bball.update()
    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for sball in Sballs:
        sball.draw()
    for bball in Bballs:
        bball.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)



# finalization code
close_canvas()