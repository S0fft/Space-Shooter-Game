import pygame
import sys
from random import randint

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption('Space Shooter')


while True:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    pygame.display.update()

    clock.tick(5)