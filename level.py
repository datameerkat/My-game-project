import pygame
import player_class

class Level:
    def __init__(self):
        self.background_surf = pygame.image.load("Images\Backgrounds\Black.png").convert_alpha()
        
        #create a GroupSingle instance with our Player class
        self.player = pygame.sprite.GroupSingle()
        self.player.add(player_class.Player())

        #list of all laser bullets
        self.lasers = pygame.sprite.Group()

    def update(self):
        self.check_shooting()
        self.player.update()

        for laser in self.lasers:
            laser.update()

    def draw(self, screen):
        screen.blit(self.background_surf, (0,0))

        self.player.draw(screen)
        self.lasers.draw(screen)

    def check_shooting(self):
        new_laser = self.player.sprite.shoot_bullet()
        if new_laser is not None:
            self.lasers.add(new_laser)
