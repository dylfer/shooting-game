import pygame
import math
# import random
from game.board import Board
from game.player import Player, Computer
from game.objects import Bullet
import time


#TODO colition, map genration, sounds, enemy, inprove bullet origin, player - smooth anmate




class Game:
    debuging = False


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
        if self.debuging:
            self.debug()
    
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
            # start = time.time()
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
                    if event.key == pygame.K_p:
                        self.debuging = not self.debuging
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.player.magSize != 0:
                            self.player.setShoot()
                        else:
                            # sound - empty mag
                            pass
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.player.setShoot(False)

                
            self.draw()
            # stop = time.time()
            self.clock.tick(60)
            # end = time.time()
            # print(stop-start, end-stop)
            

    
    def shoot(self):
        centerOffset = 30
        angle_in_radians = math.radians(30 - self.player.angle)
        gun_offset_x = centerOffset * math.cos(angle_in_radians)
        gun_offset_y = centerOffset * math.sin(angle_in_radians)

        bulletStartX = self.player.x + self.player.size[0]/2 + gun_offset_x
        bulletStartY = self.player.y + self.player.size[1]/2 + gun_offset_y


        # pygame.draw.circle(self.screen, (255, 0, 0), (int(bulletStartX), int(bulletStartY)), 5)

        if self.player.opration == "move":
            self.bullets.append(Bullet(bulletStartX, bulletStartY, self.player.angle, True))
        else:
            self.bullets.append(Bullet(bulletStartX, bulletStartY, self.player.angle))
    




    def debug(self):
        print(self.player.opration,self.player.secondOpration)



