import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'

pygame.init()

SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()

BLACK = (0,0,0)

x, y = 0, 0
move_x, move_y = 0, 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                exit()

            elif event.key == K_LEFT:
                move_x = -1

            elif event.key == K_RIGHT:
                move_x = +1

            elif event.key == K_UP:
                move_y = -1

            elif event.key == K_DOWN:
                move_y = +1

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0

            elif event.key == K_RIGHT:
                move_x = 0

            elif event.key == K_UP:
                move_y = 0

            elif event.key == K_DOWN:
                move_y = 0

        x += move_x
        y += move_y

        screen.fill(BLACK)
        screen.blit(background, (x,y))

        pygame.display.update()
            
