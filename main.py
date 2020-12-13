import pygame


from button import Button
from const import POINTS_TO_WIN
from const import TURN_HUMAN, TURN_BOT
from const import FONT_SIZE


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


# Show human stats at game screen
def print_human_stats(human_total, human_turn_score, screen, font):
    text = f'HUMAN\nTotal score: {human_total}\nTurn score: {human_turn_score}'
    offset = 0

    for line in text.split('\n'):
        rendered = font.render(line, 1, BLACK)
        screen.blit(rendered, (50, 100+4*offset))
        offset += FONT_SIZE



# Show bot stats at game screen
def print_bot_stats(bot_total, bot_turn_score, screen, font):
    text = f'BOT\nTotal score: {bot_total}\nTurn score: {bot_turn_score}'
    offset = 0

    for line in text.split('\n'):
        rendered = font.render(line, 1, BLACK)
        screen.blit(rendered, (600, 100+4*offset))
        offset += FONT_SIZE


# load images of dice
def load_dice_images(path):
    dct = dict()
    for i in range(1, 7):
        img = pygame.image.load(f'{path}dice{i}.png').convert()

        dct[i] = img
    
    return dct




# main game loop
def game():
    # Pre-loading of resource
    status_font = pygame.font.Font('resources/font/consola.ttf', FONT_SIZE)
    dice_imgs = load_dice_images('resources/img/')

    # Gaming pre-settings
    human_total, bot_total = 0, 0
    human_turn_score, bot_turn_score = 0, 0 
    turn = TURN_HUMAN
    current_dice = 1

    # Buttons initialize
    button_roll = Button(300, 400, 200, 50, color=RED, text='Roll')
    button_hold = Button(300, 500, 200, 50, color=BLUE, text='Hold')
    
    # Main cycle control
    running = True
    while running:
        # Fill the screen
        screen.fill(WHITE)
        # Draw buttons
        button_roll.draw(screen)
        button_hold.draw(screen)
        # Show statuses of human and bot
        print_human_stats(human_total, human_turn_score, screen, status_font)
        print_bot_stats(bot_total, bot_turn_score, screen, status_font)
        # Show current dice as a picture
        screen.blit(dice_imgs[current_dice], (350, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if turn == TURN_HUMAN:   # if it's a human to roll then reasonable to check pressing buttons
                
                    if button_roll.isOver(event.pos):
                        pass # do a barrel roll
                    
                    if button_hold.isOver(event.pos):
                        pass # hold back
                        turn = TURN_BOT  # give turn to bot if end of move

        # After every check of human action, it's time for bot actions
        if turn == TURN_BOT:
            pass # bot does things

        clock.tick(FPS)
        pygame.display.flip()





# Play game
game()