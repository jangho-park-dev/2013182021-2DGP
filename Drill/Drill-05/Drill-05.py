from pico2d import *

open_canvas()
grass = load_image('KPU_GROUND_FULL.png')
character = load_image('animation_sheet.png')

running = True
frame = 0



def check1():
    x, y = 0, 90
    frame = 0
    while x < 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
    while y < 535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.03)




while True:
    check1()


close_canvas()

