import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption('Snake Game - by. odgiedev')

clock = pygame.time.Clock()

pygame.mixer.music.set_volume(0.1)
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

collision_sound = pygame.mixer.Sound('sound.wav')

#<variables>
width = 640
height = 480

x_apple = randint(40,600)
y_apple = randint(50,430)

velocity = 10
x_control = velocity
y_control = 0

x_snake = int(width / 2)
y_snake = int(height / 2)

font = pygame.font.SysFont('arial', 35, True, True)

points = 0
highscore = 0

die = False

snake_list = []

lenght = 5
#</variables>

#<functions>
def increases_snake(snake_list):
    for XeY in snake_list:
        pygame.draw.rect(windows, (0,255,0), (XeY[0], XeY[1], 20, 20))

def restart_game():
    global points, lenght, x_snake, y_snake, snake_list, head_list, x_apple, y_apple, die, velocity
    velocity = 10
    points = 0
    lenght = 5
    x_snake = int(width / 2)
    y_snake = int(height / 2)
    snake_list = []
    head_list = []
    x_apple = randint(40,600)
    y_apple = randint(50,430)
    die = False

def restart_game_hard():
    global points, lenght, x_snake, y_snake, snake_list, head_list, x_apple, y_apple, die, velocity
    velocity = 23
    points = 0
    lenght = 2
    x_snake = int(width / 2)
    y_snake = int(height / 2)
    snake_list = []
    head_list = []
    x_apple = randint(40,600)
    y_apple = randint(50,430)
    die = False
#</functions>

windows = pygame.display.set_mode((width, height))
while True:
    clock.tick(30)
    
    windows.fill((0,0,0))

    message = f'points: {points}'
    highscoreM = f'highscore: {highscore}'

    formated_text = font.render(message, False, (255,255,255))
    formated_text_highscore = font.render(highscoreM, False, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == velocity:
                    pass
                else:
                    x_control = -velocity
                    y_control = 0
            
            if event.key == K_d:
                if x_control == -velocity:
                    pass
                else:
                    x_control = velocity
                    y_control = 0

            if event.key == K_w:
                if y_control == velocity:
                    pass
                else:
                    y_control = -velocity
                    x_control = 0

            if event.key == K_s:
                if y_control == -velocity:
                    pass
                else:
                    y_control = velocity
                    x_control = 0

    x_snake = x_snake + x_control 
    y_snake = y_snake + y_control 

    snake = pygame.draw.rect(windows, (0,255,0), (x_snake,y_snake,20,20))
    apple = pygame.draw.rect(windows, (255,0,0), (x_apple,y_apple,20,20))
    
    if snake.colliderect(apple):
        points += 1
        collision_sound.play()
        x_apple = randint(40,600)
        y_apple = randint(50,430)
        lenght += 1

    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)

    snake_list.append(head_list)

    if snake_list.count(head_list) > 1:
        if points > highscore:
            highscore = points

        message = 'Game Over! Press R to restart.'
        message2 = 'Press H to play hard mode.'

        formated_text = font.render(message, True, (0,0,0))
        formated_text2 = font.render(message2, True, (0,0,0))

        ret_text = formated_text.get_rect()
        ret_text2 = formated_text2.get_rect()

        die = True
        while die:
            windows.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()

                    if event.key == K_h:
                        restart_game_hard()

            ret_text.center = (width//2, (height//2)-100)
            ret_text2.center = (width//2, (height//2)+100)

            windows.blit(formated_text, ret_text)
            windows.blit(formated_text2, ret_text2)
            pygame.display.update()
    
    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width
    if y_snake < 0:
        y_snake = height
    if y_snake > height:
        y_snake = 0
        
    if len(snake_list) > lenght:
        del snake_list[0]

    increases_snake(snake_list)

    windows.blit(formated_text, (450, 5))

    windows.blit(formated_text_highscore, (380, 50))

    pygame.display.update()
