import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Exploding Potato')
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 252, 0)
GREY = (220, 220, 220)
RED = (255, 0, 0)
LIGHT_GRAY = (211, 211, 211)

# Fonts
Title_Font = pygame.font.SysFont('arial', 100)

# Sound
countdown_sound = pygame.mixer.Sound('countdown.wav')
bomb_sound = pygame.mixer.Sound('bomb.wav')


# Button class
class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('googleFont.ttf', 40)
            text = font.render(self.text, 1, BLACK)
            win.blit(text, (int(
                self.x + (self.width / 2 - text.get_width() / 2)),
                            int(self.y + (self.height / 2 - text.get_height() / 2))))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


# print text
def print_message(message, place):
    text = Title_Font.render(f'{message}', 1, BLACK)
    if place == 'center':
        width = round(WIDTH / 2 - text.get_width() / 2)
        height = round(HEIGHT / 2 - text.get_height() / 2)
    return win.blit(text, (width, height))


# Buttons
start_button = Button(GREEN, int(WIDTH / 2 - 80), int(HEIGHT * 0.8), 160, 60, "Start Game")

# time variables
countdown_time = 4


# Meny loop
def start_meny():
    run = True

    while run:
        win.fill(WHITE)

        print_message('Exploding Potato', 'center')
        start_button.draw(win)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isOver(pos):
                    game()
            if event.type == pygame.MOUSEMOTION:
                if start_button.isOver(pos):
                    start_button.color = GREEN
                else:
                    start_button.color = RED

        pygame.display.update()
        clock.tick(30)


# game loop
def game():
    run = True
    start_time = time.time()
    random_time = random.randint(5, 40)
    while run:
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        elapsed_time = time.time() - start_time

        if elapsed_time < 4:
            if elapsed_time < 1:
                countdown_sound.play()
            print_message(int(countdown_time - elapsed_time), 'center')
        else:
            game_time = time.time() - start_time
            countdown = int(random_time - game_time)
            print(countdown)
            if countdown < 0:
                bomb_sound.play()
                start_meny()
            print_message('Start', 'center')

        pygame.display.update()
        clock.tick(30)


start_meny()
game()
pygame.quit()
