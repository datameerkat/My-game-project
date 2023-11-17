import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.og_surf = pygame.image.load("Images\Spaceships\Green_ship.png").convert_alpha()
        self.image = self.og_surf
        self.rect = self.image.get_rect(center = (480,270))
        self.movespeed = 5
        #self.direction = (0,0)

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
        #define direction
        direction = self.get_direction_vector()
        angle_rad = math.atan2((direction[1]),(direction[0]))
        direction = math.degrees(angle_rad)
        
        self.image = pygame.transform.rotate(self.og_surf, -direction-90) #angle_deg-90, since 0 grad means looking up
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot_bullet(self):
        if pygame.mouse.get_pressed()[0]:
            #define direction of bullet
            #create normalized direction vector from the angle of the ship
            bullet_direction = self.get_direction_vector()

            #define starting position of bullet
            #depending on rotation and radius of ship
            ship_radius = 16
            bullet_x = self.rect.center[0] + ship_radius * bullet_direction[0]
            bullet_y = self.rect.center[1] + ship_radius * bullet_direction[1]
            bullet_position = (bullet_x,bullet_y)

            #create Laser object
            return Laser(bullet_position, bullet_direction)
        
    def get_direction_vector(self):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        center_x, center_y = self.rect.center
        delta_x = x_mouse-center_x
        delta_y = y_mouse-center_y
        norm = ((delta_x**2+delta_y**2)**(1/2))
        direction_vector = (delta_x/norm, delta_y/norm)
        return direction_vector

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, direction):
        super().__init__()
        self.direction = direction
        self.og_surf = pygame.image.load("Images\Objects\Green_laser.png").convert_alpha()
        self.image = self.og_surf
        self.rect = self.image.get_rect(center = position)
        self.movespeed = 10
        #rotate image depending on position:

    def update_position(self):
        #step = self.direction*self.movespeed
        #self.rect.x += step[0]    
        #self.rect.y += step[1]
        self.rect.x += self.direction[0]*self.movespeed
        self.rect.y += self.direction[1]*self.movespeed

    def update(self):
        self.update_position()