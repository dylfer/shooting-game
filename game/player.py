# 
# Destroyers - A top down shooting game with infinite levels and map genration.
# Copyright (C) 2024 Dylan Ferrow
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

import pygame
import asyncio
import math


class Sprite:
    speed = 2
    directions = ['left', 'right', 'up', 'down']
    opration = "idle"
    secondOpration = ""


    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def move(self,direction):
        if self.opration != "reload":
            self.opration = "move"
        match direction:
            case 'left':
                self.x -= self.speed
            case 'right':
                self.x += self.speed
            case 'up':
                self.y -= self.speed
            case 'down':
                self.y += self.speed
            case 'stop':
                self.directions = []
                if self.opration != "reload":
                    self.opration = "idle"
        if self.checkCollision(self.game.board.walls) == True:
            match direction:
                case 'left':
                    self.x += self.speed
                case 'right':
                    self.x -= self.speed
                case 'up':
                    self.y += self.speed
                case 'down':
                    self.y -= self.speed

        # if direction != self.direction:
            # self.image = pygame.transform.rotate(self.image, 90*(self.directions.index(self.direction) - self.directions.index(direction)))
            # self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.displayRect)   


    def checkCollision(self, walls):# TODO create use mask 
        self.mask = pygame.mask.from_surface(self.image)
        for wall in walls:
            offset_x = wall.rect.x - self.displayRect.x
            offset_y = wall.rect.y - self.displayRect.y
            if self.mask.overlap(wall.mask, (offset_x, offset_y)) is not None:
                return True  # Collision detected
        return False



class Player(Sprite):
    speed = 2.5/3
    images = {}
    images["idle"] = ["assets/player/idle/survivor-idle_rifle_",20]
    images["move"] = ["assets/player/move/survivor-move_rifle_",20]
    images["shoot"] = ["assets/player/shoot/survivor-shoot_rifle_",3]
    images["reload"] = ["assets/player/reload/survivor-reload_rifle_",20]
    stage = 0
    magSize = 40
    size = (80,80)
    displayRect = (0,0)
    angle = 0
    image = pygame.image.load(f"{images['idle'][0]}{stage}.png")
    image = pygame.transform.scale(image, size)
    directions = []
    frame = 0
    reloadTimer = 0



    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def reloadAction(self):
        self.magSize = 40
        self.opration = "idle"

    def reload(self):#image
        self.stage = 0
        self.opration = "reload"
        self.reloadTimer = 120

    def setShoot(self, do=True):
        if do:
            self.stage = 0
            self.secondOpration = "shoot"
        else:
            # print("no shoot")
            self.secondOpration = ""
    
    def shoot(self):#image
        self.magSize -= 1
        self.game.shoot()


    def setMove(self, direction):
        if direction not in self.directions:
            self.directions.append(direction)
        if self.opration != "reload":
            # print("move")
            self.opration = "move"

    def stopMove(self, direction):
        if direction in self.directions:
            self.directions.remove(direction)
        if len(self.directions) == 0:
            self.opration = "idle"

    def draw(self, screen):
        self.frame += 1
        #anmation
        # shooting every framee because a shot hapens every 3 framees and thare are 3 anmations
        if self.opration == "idle" and self.secondOpration == "shoot":# shoot anmation
            # print(self.opration)
            if self.stage >= self.images[self.secondOpration][1]-1:
                self.stage = 0
            self.imageOrg = pygame.image.load(f"{self.images[self.secondOpration][0]}{self.stage}.png")  
            x, y = pygame.mouse.get_pos()
            if y != self.y+self.size[1]/2:
                (dx, dy) = (x-(self.x+self.size[0]/2), y-(self.y+self.size[1]/2))
                self.angle = math.atan(float(dx)/float(dy))
                self.angle *= 180/math.pi
                if dy < 0:
                    self.angle += 180
            elif x < self.x+self.size[0]/2:
                self.angle = 0
            else:
                self.angle = 180
            self.angle -= 90
            self.imageOrg = pygame.transform.scale(self.imageOrg, self.size)
            self.image = pygame.transform.rotate(self.imageOrg, self.angle)
            self.displayRect = self.image.get_rect(center = self.imageOrg.get_rect(topleft = (self.x,self.y)).center)
            self.stage += 1
            
                

        if self.frame % 6 == 0:# other anmations
            
            if not (self.opration == "idle" and self.secondOpration == "shoot"):
                if self.stage >= self.images[self.opration][1]-1:
                    self.stage = 0
                self.imageOrg = pygame.image.load(f"{self.images[self.opration][0]}{self.stage}.png")  
                
                x, y = pygame.mouse.get_pos()
                if y != self.y+self.size[1]/2:
                    (dx, dy) = (x-(self.x+self.size[0]/2), y-(self.y+self.size[1]/2))
                    self.angle = math.atan(float(dx)/float(dy))
                    self.angle *= 180/math.pi
                    if dy < 0:
                        self.angle += 180
                elif x < self.x+self.size[0]/2:
                    self.angle = 0
                else:
                    self.angle = 180
                self.angle -= 90
                self.imageOrg = pygame.transform.scale(self.imageOrg, self.size)
                self.image = pygame.transform.rotate(self.imageOrg, self.angle)
                self.displayRect = self.image.get_rect(center = self.imageOrg.get_rect(topleft = (self.x,self.y)).center)
                # pygame.draw.rect(screen, (255,0,0), self.displayRect,  2)
                self.stage += 1

        #reload
        if self.reloadTimer == 0 and self.opration == "reload":
            self.reloadAction()
        elif self.opration == "reload":
            self.reloadTimer -= 1
        #move or shoot
        if self.opration == "move":
            for direction in self.directions:
                self.move(direction)
        if self.frame % 3 == 0:
            
            if self.secondOpration == "shoot" and self.opration != "reload":
                if self.magSize > 0:
                    self.shoot()
                else:
                    # print("empty mag")
                    #sound - empty mag
                    pass
        
        super().draw(screen)





class Computer(Sprite):
    def __init__(self, x, y,level,boss):
        super().__init__(x, y)
        if boss:
            self.speed = 4*level
            self.image = pygame.image.load('assets/boss.png')
            self.image = pygame.transform.scale(self.image, (80, 80))
        self.speed = 1.5*level
        self.boss = boss
        self.level = level
        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (40, 40))

    










    def shoot(self):
        pass


    def draw():
        pass