import pygame
import math
import random





class Bullet:
    def __init__(self, x, y,angle,move = False):
        self.x = x
        self.y = y
        self.speed = 10
        if move:
            self.angle = angle + random.random()*random.choice([-2,2])
        else:
            self.angle = angle + random.random()*random.choice([-1,1])
        self.image = pygame.image.load('assets/bullet2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 6))
        self.image = pygame.transform.rotate(self.image, angle)

    def move(self):
        # self.y -= self.speed
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))