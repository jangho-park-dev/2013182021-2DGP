from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 720
open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('KPU_GROUND_FULL.png')
character = load_image('animation_sheet.png')

running = True
frame = 0

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

n = 1
size = 5
points = [(random.randint(0, 1000), random.randint(0, 600))
          for i in range(size)]

count = 0

x = (points[n-1])[0]
y = (points[n-1])[1]

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    t = count / 100
    x = (1 - t) * (points[n - 1])[0] + t * (points[n])[0]
    y = (1 - t) * (points[n - 1])[1] + t * (points[n])[1]
    count = count + 2

    if count >= 100:
        n = (n + 1) % size
        count = 0

    delay(0.01)