import pygame, random
from game.board import Board
from game.player import Player, Computer




class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.image = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))






class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        self.computer.draw(self.screen)
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(self.screen)
        self.board.draw(self.screen)
        pygame.display.flip()


    def start(self):
        self.player = Player(400, 500)
        self.computer = Computer(400, 100)
        self.bullets = []
        self.board = Board()
        self.board.generate()
        self.mainLoop()

    def custom(self):
        self.mainLoop()


    

    def mainLoop(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()
                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()
                    if event.key == pygame.K_SPACE:
                        self.bullets.append(Bullet(self.player.x, self.player.y))
            self.draw()
            pygame.display.flip()






