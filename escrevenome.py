import pygame

my_name = 'Marcelo Reis'

pygame.init()

my_font = pygame.font.SysFont('arial', 64)

name_surface = my_font.render(my_name, True, (0,0,0), (255,255,255).aplha)

pygame.image.save(name_surface, 'name.png')
