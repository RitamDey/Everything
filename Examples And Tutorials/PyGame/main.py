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
playerX = 370
playerY = 480

def player(player_icon, screen):
    # Draw the image on the screen
    screen.blit(player_icon, (playerX, playerY))

running = True
while running:
    # Sets and persists the background colour of the windows
    screen.fill((0, 0, 0))
    # Gets all the events from the queue and sees if it's PyGame quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call this function to draw the player on each iteration of the redraw
    player(player_icon, screen)
    
    # Instructs PyGame to update the screen to reflect changes on the screen
    pygame.display.update()

