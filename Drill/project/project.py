from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 960, 640
open_canvas(KPU_WIDTH, KPU_HEIGHT)
grass = load_image('Track2B.png')
character = load_image('animation_sheet.png')

frame = 0
MoveCheck = False
Crunning = True
Cx, Cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
CxSave, CySave = Cx, Cy;
dir = 0
# location set
# enemy first location
x = 100
y = 640
# 1. y == 384  y--
# 2. x == 220  x++
# 3. y == 256  y--
# 4. x == 100  x--
# 5. y == 114  y--
# 6. x == 333  x++
# 7. y == 512  y++
# 8. x == 580  x++
# 9. y == 384  y--
# 10. x == 456  x--
# 11. y == 248  y--
# 12. x == 564  x++
# 13. y == 0  y--

def handle_events():
    global MoveCheck
    global Cx, Cy
    global CxSave, CySave
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Crunning = False
        elif event.type == SDL_MOUSEMOTION:
            Cx, Cy = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Crunning = False
        elif event.type == SDL_MOUSEBUTTONUP:
            pass
        elif event.type == SDL_MOUSEBUTTONDOWN:
            CxSave, CySave = event.x, KPU_HEIGHT - 1 - event.y
            MoveCheck = True

while Crunning:
    clear_canvas()
    grass.draw(480, 320)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.03)

    handle_events()

    if MoveCheck:
        if x < CxSave:
            x += 1
            dir = 1
        if x > CxSave:
            x -= 1
            dir = 0
        if y < CySave:
            y += 1
        if y > CySave:
            y -= 1

    if x == Cx and y == Cy:
        MoveCheck == False

close_canvas()