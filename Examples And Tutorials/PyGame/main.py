import pygame


if __name__ == "__main__":
    # Initialize the pygame. Needed before doing anything
    pygame.init()

    # Creates a screen of 800x600 dimensions
    screen = pygame.display.set_mode((800, 600))

    running = True
    while running:
        # Gets all the events from the queue and sees if it's PyGame quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
