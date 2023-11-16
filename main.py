import pygame
import player_class
from sys import exit

pygame.init()
screen_width, screen_height = [960, 540]
screen = pygame.display.set_mode((screen_width,screen_height)) #can be scaled up to 1920*1080
pygame.display.set_caption("Space Geckos")
clock = pygame.time.Clock()

background_surf = pygame.image.load("Images\Backgrounds\Black.png").convert_alpha()

#create a GroupSingle instance with our Player class
player = pygame.sprite.GroupSingle()
player.add(player_class.Player())

#player_surf = pygame.image.load("Images\Spaceships\Green_ship.png").convert_alpha()
#player_rect = player_surf.get_rect(center = (screen_width*0.5,screen_height*0.5))

while True:
    for event in pygame.event.get():
        #closing window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #show background
    screen.blit(background_surf, (0,0))
    #move player
    #player_rect.y += -1
    #draw images on screen
    player.draw(screen)
    #update all objects
    player.update()

    pygame.display.update()
    clock.tick(60)