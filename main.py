import pygame





class Shooter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.image.load('shooter.png')
        self.image = pygame.transform.scale(self.image, (40, 40))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



class Player(Shooter):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 5
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (40, 40))




class Computer(Shooter):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 3
        self.image = pygame.image.load('computer.png')
        self.image = pygame.transform.scale(self.image, (40, 40))




