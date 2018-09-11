from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
flag = 0

while True:
    if (flag == 0):
        while (x < 800):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, 90)
            update_canvas()
            frame = (frame + 1) % 
            x += 5
            delay(0.05)
            flag = 1
            get_events()
    if (flag == 1):
        while (x > 0):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, 0, 100, 100, x, 90)
            update_canvas()
            frame = (frame + 1) % 32
            x -= 5
            delay(0.05)
            flag = 0
            get_events()

close_canvas()