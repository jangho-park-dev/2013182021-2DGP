import game_framework
from pico2d import *
import main_state
import random

name = "TitleState"
image = None
bgm = None
font = None
r, g, b = 0, 0, 0

def enter():
    global image, bgm, font
    image = load_image('title.png')
    bgm = load_music('title.mid')
    bgm.set_volume(64)
    bgm.repeat_play()
    font = load_font('ENCR10B.TTF', 16)

def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(480, 320)
    update()
    font.draw(420, 320, 'Please ESC Key', (r, g, b))
    update_canvas()


def update():
    global r, g, b
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


def pause():
    pass


def resume():
    pass






