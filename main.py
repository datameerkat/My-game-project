import pygame
import player_class
import level
from sys import exit

pygame.init()
screen_width, screen_height = [960, 540]
screen = pygame.display.set_mode((screen_width,screen_height)) #can be scaled up to 1920*1080
pygame.display.set_caption("Space Geckos")
clock = pygame.time.Clock()

#create level object
level = level.Level()

while True:
    for event in pygame.event.get():
        #closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #update and draw level with the player and all objects
    level.update()
    level.draw(screen)

    pygame.display.update()
    clock.tick(60)