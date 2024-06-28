import pygame
import math
# import random
from game.board import Board
from game.player import Player, Computer
from game.objects import Bullet


#TODO colition, map genration, sounds, enemy




class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.clock = pygame.time.Clock()


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        # self.computer.draw(self.screen)
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(self.screen)
        self.board.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        pass


    def menu(self):
        pass



    def start(self):
        self.screen = pygame.display.set_mode((1400, 1000))
        self.player = Player(self,400, 500)
        # self.computer = Computer(400, 100)
        self.bullets = []
        self.board = Board()
        self.board.generate(0)
        self.mainLoop()

    # def custom(self):
    #     self.mainLoop()



    def mainLoop(self):
        down = []
        while self.running:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.setMove("left")
                        down.append("left")
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.setMove("right")
                        down.append("right")
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.setMove("up")
                        down.append("up")
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.setMove("down")
                        down.append("down")
                    if event.key == pygame.K_r:
                        self.player.reload()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.stopMove("left")
                        down.remove("left")
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.stopMove("right")
                        down.remove("right")
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.stopMove("up")
                        down.remove("up")
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.stopMove("down")
                        down.remove("down")
                # if len(down) == 0:
                #     self.player.move("stop")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player.magSize != 0:
                        self.player.setShoot()
                    else:
                        # sound - empty mag
                        pass
                if event.type == pygame.MOUSEBUTTONUP:
                    self.player.setShoot(False)

                
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

    
    def shoot(self):
        self.bullets.append(Bullet(self.player.x+self.player.size[0]/2, self.player.y+self.player.size[1]/2,self.player.angle))






