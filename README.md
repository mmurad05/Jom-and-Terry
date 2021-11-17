# cs_project
CS 1110 Gamebox Project
Partners: Mohammad Murad (vdr4jr) and Matthew Galitz (ykk6rh)

Project Description:
The user will use arrow keys to move a mouse sprite on the screen. The user will try to get a cheese sprite that, if the mouse touches it, will increase the score for the user and then disappear and reappear in another random spot. There is also an “enemy”, which is a cat sprite that chases the mouse around. If the cat “catches” the mouse, the score resets and the game ends.

Required Features:
User Input
Implemented through the if statements with pygame.K_ in keys
Start Screen
Defaults to start screen
camera.clear()
camera.draw(some text)
game_on variable is initialized to False
if pygame.K_somekey game_on is reassigned True
if statement 
Game Over
Implemented through an If Else statement inside the main function
Small Enough Window
Implemented through the gamebox.Camera(800, 600) function
Graphics/Images
Implemented through the gamebox.from_image() and gamebox.from_url() functions

Optional Features:
Restart From Game Over
Implemented through a setup() function which can be called after the game ends to “Reset” the game
Collectables
Implemented through gambox.(), random module, .touches() 
Enemies
Implemented through gamebox.() move(), .x, .y, 
Sprite Sheet
Implemented through gamebox.loadspritesheet

