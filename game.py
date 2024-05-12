import pygame, random



class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('wall.png')
        self.image = pygame.transform.scale(self.image, (40, 40))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))




class Board:
    borders = [pygame.Rect(0, 0, 800, 10), pygame.Rect(0, 0, 10, 600), pygame.Rect(0, 590, 800, 10), pygame.Rect(790, 0, 10, 600)]
    walls = []
    def __init__(self):
        self.width = 1400
        self.height = 1000

    def draw(self, screen):
        for wall in self.walls:
            screen.blit(wall.image, (wall.x, wall.y))
        for border in self.border:
            pygame.draw.rect(screen, (255, 255, 255), border)
    
    def generate(self):
        for i in range(2):
            for j in range(2):
                self.walls.append(pygame.Rect(200 * i, 200 * j, 200, 200))









class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            pygame.display.flip()