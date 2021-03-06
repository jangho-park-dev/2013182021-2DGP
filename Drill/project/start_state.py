import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
bgm = None
logo_time = 0.0


def enter():
    global image, bgm
    image = load_image('kpu_credit.png')
    bgm = load_music('happyend.mid')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image
    del(image)


def update():
    global logo_time

    if (logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
        # game_framework.quit()
        game_framework.change_state(title_state)

    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(480, 320)
    update_canvas()


def handle_events():
    events = get_events()


def pause(): pass


def resume(): pass




