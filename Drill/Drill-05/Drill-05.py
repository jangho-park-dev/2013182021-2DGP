from pico2d import *
# drill-05 완성
open_canvas()
grass = load_image('KPU_GROUND_FULL.png')
character = load_image('animation_sheet.png')

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
def check5():
    x, y = 477, 203
    frame = 0
    while x < 715:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
    while y > 136:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.03)
def check6():
    x, y = 715, 136
    frame = 0
    while x > 316:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.03)
    while y < 225:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.03)
def check7():
    x, y = 316, 225
    frame = 0
    while x < 510:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
    while y > 92:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.03)
def check8():
    x, y = 510, 92
    frame = 0
    while x < 692:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
    while y < 518:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.03)
def check9():
    x, y = 692, 518
    frame = 0
    while x > 682:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.03)
    while y > 336:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.03)
def check10():
    x, y = 682, 336
    frame = 0
    while x < 712:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.03)
    while y < 349:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.03)
while True:
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
    check7()
    check8()
    check9()
    check10()

close_canvas()