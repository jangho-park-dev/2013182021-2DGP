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
def check2():
    x, y = 203, 535
    frame = 0
    while x > 132:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.03)
    while y > 243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.03)
def check3():
    x, y = 132, 243
    frame = 0
    while x < 535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
    while y < 470:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.03)
def check4():
    x, y = 535, 470
    frame = 0
    while x > 477:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.03)
    while y > 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.03)

while True:
    #check1()
    #check2()
    #check3()
    check4()
close_canvas()

