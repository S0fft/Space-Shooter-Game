import pygame
import sys

pygame.init()
pygame.display.set_caption('Awesome Shooter Game')

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_fill_color = (32, 52, 71)

FIGTHER_STEP = 0.5
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = (screen_width / 2) - (fighter_width / 2), screen_height - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False

rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_hegiht = rocket_image.get_size()
rocket_x, rocket_y = (fighter_x + fighter_width / 2) - (rocket_width / 2), fighter_y - rocket_hegiht
rocket_was_fired = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 sys.exit()

            if event.key == pygame.K_LEFT and fighter_x >= FIGTHER_STEP:
                    fighter_is_moving_left = True
                    fighter_x -= FIGTHER_STEP
            if event.key == pygame.K_RIGHT and fighter_x <= screen_width - fighter_width - FIGTHER_STEP:
                 fighter_is_moving_right = True
                 fighter_x += FIGTHER_STEP
            if event.key == pygame.K_SPACE:
                 rocket_was_fired = True

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT:
                  fighter_is_moving_left = False
             if event.key == pygame.K_RIGHT:
                  fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGTHER_STEP:
        fighter_x -= FIGTHER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGTHER_STEP:
        fighter_x += FIGTHER_STEP

    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    if rocket_was_fired:
         screen.blit(rocket_image, (rocket_x, rocket_y))

    pygame.display.update()