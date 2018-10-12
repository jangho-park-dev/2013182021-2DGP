import game_framework
from pico2d import *


name = "TitleState"
image = None
image2 = None
cnt = 0

def enter():
    global image, image2
    image = load_image('pause11.png')
    image2 = load_image('pause22.png')


def exit():
    global image, image2
    del(image)
    del(image2)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    global cnt
    if cnt >= 200:
        cnt = 0
    cnt += 1
    if cnt < 100:
        image.draw(480, 320)
    elif cnt < 200:
        image2.draw(480, 320)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






