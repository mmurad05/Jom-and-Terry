# Mohammad Murad
# vdr4jr

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
frame = 0
sheet = gamebox.load_sprite_sheet("mouse_sprite1.png", 4, 1)
character = gamebox.from_image(400, 300, sheet[frame])
alive = True
def tick(keys):
    global frame, alive
    if alive:
        if pygame.K_UP in keys:
            character.y -= 10
            character.image = sheet[3]
            if character.y < camera.y - 290:
                character.y = camera.y - 290
        if pygame.K_DOWN in keys:
            character.image = sheet[0]
            character.y += 10
            if character.y > camera.y + 290:
                character.y = camera.y + 290
        if pygame.K_LEFT in keys:
            character.x -= 10
            character.image = sheet[1]
            if character.x < 10:
                character.x = 10
        if pygame.K_RIGHT in keys:
            character.x += 10
            character.image = sheet[2]
            if character.x > 790:
                character.x = 790
    camera.clear("white")
    camera.draw(character)
    camera.display()
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
