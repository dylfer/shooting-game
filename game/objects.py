import pygame
import math
import random





class Bullet:
    def __init__(self, x, y,angle,move = False):
        self.x = x
        self.y = y
        self.origin = (x, y)
        self.frame = 0
        self.speed = 10
        if move:
            self.angle = angle + random.random()*random.choice([-2,2])
        else:
            self.angle = angle + random.random()*random.choice([-1,1])
        self.image = pygame.image.load('assets/bullet2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 6))
        self.image = pygame.transform.rotate(self.image, angle)
        self.flashImage = pygame.image.load('assets/flash.png').convert_alpha()
        self.flashImage = pygame.transform.scale(self.flashImage, (20, 10))
        self.flashImage = pygame.transform.rotate(self.flashImage, angle)

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

    def draw(self, screen):
        
        if self.frame < 20:
            self.frame += 1
            # centerOffset = 20
            # angle_in_radians = math.radians(180+self.angle)
            # gun_offset_x = centerOffset * math.cos(angle_in_radians)
            # gun_offset_y = centerOffset * math.sin(angle_in_radians)

            # self.StartX = self.origin[0] + gun_offset_x
            # self.StartY = self.origin[1] + gun_offset_y
            screen.blit(self.flashImage, self.origin)#(self.StartX,self.StartY)) 
        screen.blit(self.image, (self.x, self.y))