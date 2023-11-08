import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images\Spaceships\Green_ship.png").convert_alpha()
        self.rect = self.image.get_rect(center = (480,270))

    def update(self):
        #update for one frame
        test = 1