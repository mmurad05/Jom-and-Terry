# Partners: Mohammad Murad (vdr4jr) and Matthew Galitz (ykk6rh)
# All sprite sheets from https://forums.rpgmakerweb.com/ and https://www.pngfind.com/
# Project Description:
# The user will use arrow keys to move a mouse sprite on the screen. The user will try to get a cheese sprite that, if the mouse touches it, will increase the score for the user and then disappear and reappear in another random spot. There is also an “cat”, which is a cat sprite that chases the mouse around. If the cat “catches” the mouse, the score resets and the game ends.
# Required Features:
# User Input - Implemented through the if statements with pygame.K_ in keys
# Start Screen - Defaults to start screen, camera.clear(), camera.draw(some text), game_on variable is initialized to False, if pygame.K_somekey game_on is reassigned True if statement
# Game Over - Implemented through an If Else statement inside the main function
# Small Enough Window - Implemented through the gamebox.Camera(800, 600) function
# Graphics/Images - Implemented through the gamebox.from_image() and gamebox.from_url() functions
# Optional Features:
# Restart From Game Over - Implemented through a setup() function which can be called after the game ends to “Reset” the game
# Collectables - Implemented through gambox.(), random module, .touches()
# Enemies - Implemented through gamebox.() move(), .x, .y,
# Sprite Sheet - Implemented through gamebox.loadspritesheet

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
mouse_sheet = None
cat_sheet = None
cat_speed = 3
mouse_speed = 10
cat = None
mouse = None
cheeses = []
game_over = None
start_page = None
score = 0
alive = True
started = False
start_page = gamebox.from_image(400,300, "Start Page.jpg")
def setup():
    global mouse_sheet, cat_sheet, cat, mouse, cheeses, game_over, score, alive, cat_speed, mouse_speed
    mouse_sheet = gamebox.load_sprite_sheet("mouse_sprite1.png", 4, 1)
    cat_sheet = gamebox.load_sprite_sheet("cat.png", 1, 1)
    cat = gamebox.from_image(100, 100, cat_sheet[0])
    mouse = gamebox.from_image(400, 300, mouse_sheet[0])
    cheeses = [gamebox.from_image(200, 500, "cheese.png"),
               gamebox.from_image(450, 700, "cheese.png"),
               gamebox.from_image(100, 200, "cheese.png"),
               gamebox.from_image(600, 100, "cheese.png")
               ]
    game_over = gamebox.from_text(400, 300, "Game Over", 72, "red")
    score = 0
    cat_speed = 3
    mouse_speed = 10
    alive = True
setup()

def tick(keys):
    global alive, score, started, start_page
    camera.clear("white")
    score_display = gamebox.from_text(40, camera.y + 250, str(score), 50, "red")
    for cheese in cheeses:
        camera.draw(cheese)
        if mouse.touches(cheese):
            cheese.x = random.randint(20, 780)
            cheese.y = random.randint(20, 580)
            score += 1
    camera.draw(score_display)
    camera.draw(cat)
    camera.draw(mouse)
    if started != True:
        camera.draw(start_page)
        if pygame.K_r in keys:
            started = True
    elif alive:
        mouse_movement(keys)
        cat_movement(keys)
    else:
        camera.draw(game_over)
        if pygame.K_SPACE in keys:
            alive = True
            setup()
    camera.display()

def mouse_movement(keys):
    global score, mouse_speed
    if score >= 15 and score < 20:
        mouse_speed = 12
    if score >= 20:
        mouse_speed = 14
    if pygame.K_UP in keys:
        mouse.y -= mouse_speed
        mouse.image = mouse_sheet[3]
        if mouse.y < camera.y - 290:
            mouse.y = camera.y - 290
    if pygame.K_DOWN in keys:
        mouse.image = mouse_sheet[0]
        mouse.y += mouse_speed
        if mouse.y > camera.y + 290:
            mouse.y = camera.y + 290
    if pygame.K_LEFT in keys:
        mouse.x -= mouse_speed
        mouse.image = mouse_sheet[1]
        if mouse.x < 10:
            mouse.x = 10
    if pygame.K_RIGHT in keys:
        mouse.x += mouse_speed
        mouse.image = mouse_sheet[2]
        if mouse.x > 790:
            mouse.x = 790
def cat_movement(keys):
    global alive, cat_speed, score
    if score >= 10 and score < 15:
        cat_speed = 4
    if score >= 15 and score < 20:
        cat_speed = 6
    if score >= 20:
        cat_speed = 8
    if mouse.x < cat.x:
        cat.x -= cat_speed
    if mouse.x > cat.x:
        cat.x += cat_speed
    if mouse.y < cat.y:
        cat.y -= cat_speed
    if mouse.y > cat.y:
        cat.y += cat_speed
    if cat.touches(mouse):
        alive = False
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)
