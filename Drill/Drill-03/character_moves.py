from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 50
y = 90
flag = 0

theta = -90
radian = math.radians(theta)

while True:
    if (flag == 0):
        while (x < 750):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x += 5
            delay(0.005)
        while (y < 520):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(750, y)
            y += 5
            delay(0.005)
        while (x > 50):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 520)
            x -= 5
            delay(0.005)
        while (y > 90):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(50, y)
            y -= 5
            delay(0.005)
        while (x < 400):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x += 5
            flag = 1
            delay(0.005)
    if (flag == 1):
        while True:
            clear_canvas_now()
            grass.draw_now(400, 30)
            x = 400 + 220 * math.cos(radian)
            y = 300 + 220 * math.sin(radian)
            character.draw_now(x, y)
            theta += 1
            delay(0.005)
            radian = math.radians(theta)
            if (theta >= 270):
                x = 400
                y = 90
                flag = 0
                theta = -90
                break
    

close_canvas()
