import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.og_surf = pygame.image.load("Images\Spaceships\Green_ship.png").convert_alpha()
        self.image = self.og_surf
        self.rect = self.image.get_rect(center = (480,270))
        self.movespeed = 5
        self.direction = 0

    def update(self):
        #update for one frame
        self.rotate()
        self.move()
        
    def move(self): 
        #move player depending on input
        key = pygame.key.get_pressed()
        #unnormalized movement vector
        x_new, y_new = [0, 0]

        if key[pygame.K_w]:
            y_new -= 1
        if key[pygame.K_s]:
            y_new += 1
        if key[pygame.K_d]:
            x_new += 1
        if key[pygame.K_a]:
            x_new -= 1
        #normalize vector
        norm = ((y_new**2+x_new**2)**(1/2))
        if norm != 0:
            self.rect.y += y_new/norm*self.movespeed
            self.rect.x += x_new/norm*self.movespeed
            #self.rect = self.image.get_rect(center = (x_new,y_new))

    def rotate(self):
        #get the mouse position
        x_mouse, y_mouse = pygame.mouse.get_pos()
        #calculate angle between player and mouse
        center_x, center_y = self.rect.center
        angle_rad = math.atan2((y_mouse-center_y),(x_mouse-center_x))
        self.direction = math.degrees(angle_rad)
        
        self.image = pygame.transform.rotate(self.og_surf, -self.direction-90) #angle_deg-90, since 0 grad means looking up
        self.rect = self.image.get_rect(center=self.rect.center)
    #rotate player depending on mouse position