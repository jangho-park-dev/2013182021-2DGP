from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 720
open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('KPU_GROUND_FULL.png')
character = load_image('animation_sheet.png')

frame = 0
dir = 0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

n = 1
size = 11
points = [(random.randint(0, 1000), random.randint(0, 600))
          for i in range(size)]


def draw_Drill07():
    global frame
    global n

    for i in range(0, 50, 2):
        if (points[n - 1])[0] > (points[n])[0]:
            dir = 0
        if (points[n - 1])[0] < (points[n])[0]:
            dir = 1

        t = i / 100
        x = (2*t**2-3*t+1)*(points[n - 1])[0]+(-4*t**2+4*t)*(points[n])[0]+(2*t**2-t)*(points[n + 1])[0]
        y = (2*t**2-3*t+1)*(points[n - 1])[1]+(-4*t**2+4*t)*(points[n])[1]+(2*t**2-t)*(points[n + 1])[1]
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.03)

    for i in range(0, 8):
        draw_Drill07_2()

    for i in range(50, 100, 2):
        if (points[n - 1])[0] < (points[n])[0]:
            dir = 0
        if (points[n - 1])[0] > (points[n])[0]:
            dir = 1

        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * (points[n])[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * (points[0])[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * (points[1])[0] + (t ** 3 - t ** 2) * (points[2])[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * (points[n])[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * (points[0])[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * (points[1])[1] + (t ** 3 - t ** 2) * (points[2])[1]) / 2

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.03)

    n = 1


def draw_Drill07_2():
    global frame
    global n

    for i in range(0, 50, 2):
        if (points[n - 1])[0] < (points[n])[0]:
            dir = 0
        if (points[n - 1])[0] > (points[n])[0]:
            dir = 1

        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*(points[n - 1])[0] + (3*t**3 - 5*t**2 + 2)*(points[n])[0] + (-3*t**3 + 4*t**2 + t)*(points[n + 1])[0] + (t**3 - t**2)*(points[n + 2])[0])/2
        y = ((-t**3 + 2*t**2 - t)*(points[n - 1])[1] + (3*t**3 - 5*t**2 + 2)*(points[n])[1] + (-3*t**3 + 4*t**2 + t)*(points[n + 1])[1] + (t**3 - t**2)*(points[n + 2])[1])/2
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.03)

    for i in range(50, 100, 2):
        if (points[n - 1])[0] < (points[n])[0]:
            dir = 0
        if (points[n - 1])[0] > (points[n])[0]:
            dir = 1

        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*(points[n - 1])[0] + (3*t**3 - 5*t**2 + 2)*(points[n])[0] + (-3*t**3 + 4*t**2 + t)*(points[n + 1])[0] + (t**3 - t**2)*(points[n + 2])[0])/2
        y = ((-t**3 + 2*t**2 - t)*(points[n - 1])[1] + (3*t**3 - 5*t**2 + 2)*(points[n])[1] + (-3*t**3 + 4*t**2 + t)*(points[n + 1])[1] + (t**3 - t**2)*(points[n + 2])[1])/2
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.03)
    n = n + 1
    print(n)


while True:
    draw_Drill07()


turtle.done()
