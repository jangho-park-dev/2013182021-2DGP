import game_framework
from pico2d import *


name = "HighGradePauseState"
image = None


def enter():
    global image1, image2
    image1 = load_image('pause11.png')
    image2 = load_image('pause22.png')


def exit():
    global image1, image2
    del (image1)
    del (image2)


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
    clear_canvas()
    image1.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






