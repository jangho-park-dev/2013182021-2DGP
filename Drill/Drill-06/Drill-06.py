from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 720


def handle_events():
    global MoveCheck
    global Crunning     # Cursor Running
    global Cx, Cy
    global CxSave, CySave
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Crunning = False
        elif event.type == SDL_MOUSEMOTION:
            Cx, Cy = event.x + 25, KPU_HEIGHT - 1 - event.y - 25
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Crunning = False
        elif event.type == SDL_MOUSEBUTTONUP:
            pass
        elif event.type == SDL_MOUSEBUTTONDOWN:
            CxSave, CySave = event.x, KPU_HEIGHT - 1 - event.y
            MoveCheck = True



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

MoveCheck = False
Crunning = True
Cx, Cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
CxSave, CySave = Cx, Cy;
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
hide_cursor()       # 커서 숨김

while Crunning:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw_now(Cx, Cy)
    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8


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




