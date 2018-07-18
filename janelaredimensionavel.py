import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (640,480)
background_image_filename = 'sushiplate.jpg'

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
background = pygame.image.load(background_image_filename).convert()

while True:

    #for event in pygame.event.get():
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        exit()

    if event.type == KEYDOWN:
        if event.key == K_q:
            pygame.quit()
            exit()

    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption('Window resized to ' +str(event.size))
        screen_width, screen_height = SCREEN_SIZE
        for y in range(0, screen_height, background.get_height()):
            for x in range(0, screen_width, background.get_width()):
                screen.blit(background, (x,y))

        pygame.display.update()
