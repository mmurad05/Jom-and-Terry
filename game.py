# Mohammad Murad
# vdr4jr
# All sprite sheets from https://forums.rpgmakerweb.com/
import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
mouse_sheet = gamebox.load_sprite_sheet("mouse_sprite1.png", 4, 1)
cat_sheet = gamebox.load_sprite_sheet("cat_sheet.png", 4, 1)
cat = gamebox.from_image(100,100, cat_sheet[0])
mouse = gamebox.from_image(400, 300, mouse_sheet[0])
cheese = gamebox.from_image(200,200, "cheese.png")
score = 0
alive = True
def tick(keys):
    global alive, score
    if alive:
        mouse_movement(keys)
        cat_movement(keys)
        if mouse.touches(cheese):
            cheese.x = random.randint(20, 780)
            cheese.y = random.randint(20, 580)
            score += 1
    score_display = gamebox.from_text(40, camera.y + 250, str(score), 50, "red")
    camera.clear("white")
    camera.draw(cheese)
    camera.draw(score_display)
    camera.draw(cat)
    camera.draw(mouse)
    camera.display()

def mouse_movement(keys):
    if pygame.K_UP in keys:
        mouse.y -= 10
        mouse.image = mouse_sheet[3]
        if mouse.y < camera.y - 290:
            mouse.y = camera.y - 290
    if pygame.K_DOWN in keys:
        mouse.image = mouse_sheet[0]
        mouse.y += 10
        if mouse.y > camera.y + 290:
            mouse.y = camera.y + 290
    if pygame.K_LEFT in keys:
        mouse.x -= 10
        mouse.image = mouse_sheet[1]
        if mouse.x < 10:
            mouse.x = 10
    if pygame.K_RIGHT in keys:
        mouse.x += 10
        mouse.image = mouse_sheet[2]
        if mouse.x > 790:
            mouse.x = 790

def cat_movement(keys):
    if pygame.K_w in keys:
        cat.y -= 10
        cat.image = cat_sheet[3]
        if cat.y < camera.y - 290:
            cat.y = camera.y - 290
    if pygame.K_s in keys:
        cat.image = cat_sheet[0]
        cat.y += 10
        if cat.y > camera.y + 290:
            cat.y = camera.y + 290
    if pygame.K_a in keys:
        cat.x -= 10
        cat.image = cat_sheet[1]
        if cat.x < 10:
            cat.x = 10
    if pygame.K_d in keys:
        cat.x += 10
        cat.image = cat_sheet[2]
        if cat.x > 790:
            cat.x = 790
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
