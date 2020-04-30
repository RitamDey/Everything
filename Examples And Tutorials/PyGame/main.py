import pygame


# Initialize the pygame. Needed before doing anything
pygame.init()

# Creates a screen of 800x600 dimensions
screen = pygame.display.set_mode((800, 600))

# Sets a title to the window
pygame.display.set_caption("Space Invaders")

# Loads a image and sets it icon to the window
ufo_icon = pygame.image.load("ufo.png")
pygame.display.set_icon(ufo_icon)

# Loads the icon for the player
player_icon = pygame.image.load("player.png")
playerX = 370.0
playerY = 480.0
playerX_change = 0
playerY_change = 0

def player(x, y):
    # Draw the image on the screen
    screen.blit(player_icon, (x, y))

running = True
while running:
    # Sets and persists the background colour of the windows
    screen.fill((0, 0, 0))

    # Gets all the events from the queue and sees if it's PyGame quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        print(event)
        
        # Checks for the keystrokes from PyGame
        if event.type == pygame.KEYDOWN:
            # Checks for what key was pressed
            if event.unicode == 'q':
                running = False

            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            elif event.key == pygame.K_UP:
                playerY_change = -0.3
            elif event.key == pygame.K_DOWN:
                playerY_change = 0.3
        
        if event.type == pygame.KEYUP:
            # These are required to reset the movement paramters, otherwise the icon will keep moving
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Call this function to draw the player on each iteration of the redraw
    playerX = (playerX + playerX_change) % 800
    playerY = (playerY + playerY_change) % 600
    player(playerX, playerY)
    
    # Instructs PyGame to update the screen to reflect changes on the screen
    pygame.display.update()

# Recommended way to end PyGame
pygame.display.quit()
pygame.quit()
