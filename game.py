import pygame



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



class Board:
    def __init__(self):
        self.width = 800
        self.height = 600

    def draw(self, screen):
        # screen.blit(self.image, (0, 0))
        pass

    def generate(self):
        pass









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