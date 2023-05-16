import pygame
import sys

pygame.init()

pygame.display.set_caption('Space Shooter')

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
fill_color = (32, 52, 71)

rect_width = 100
rect_hegiht = 200
rect_x = (screen_width / 2) - (rect_width / 2)
rect_y = (screen_height / 2) - (rect_hegiht / 2)
rect_color = pygame.Color('lightyellow')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((fill_color))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_hegiht))
    pygame.display.update()
