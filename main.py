import pygame
from button import Button
from const import POINTS_TO_WIN
# Screen params
WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 60


# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# pygame initialization
pygame.init()

# Screen settings
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pig Dice Game')
clock = pygame.time.Clock()


# main game loop
def game():
    # Gaming pre-settings
    human_total, bot_total = 0, 0
    running = True
    # Buttons initialize
    button_roll = Button(300, 400, 200, 50, color=RED, text='Roll')
    button_hold = Button(300, 500, 200, 50, color=BLUE, text='Hold')
    while running:
        # Fill the screen
        screen.fill(WHITE)
        # Draw buttons
        button_roll.draw(screen)
        button_hold.draw(screen)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if button_roll.isOver(event.pos):
                    pass # do a barrel roll
                
                if button_hold.isOver(event.pos):
                    pass # hold back


        clock.tick(FPS)
        pygame.display.flip()



# Play game
game()