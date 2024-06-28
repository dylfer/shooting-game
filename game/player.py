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
        # if direction != self.direction:
            # self.image = pygame.transform.rotate(self.image, 90*(self.directions.index(self.direction) - self.directions.index(direction)))
            # self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    def checkCollision(self, sprite):# ToDo create use mask 
        return self.rect.colliderect(sprite.rect)



class Player(Sprite):
    speed = 2.5
    images = {}
    images["idle"] = ["assets/player/idle/survivor-idle_rifle_",20]
    images["move"] = ["assets/player/move/survivor-move_rifle_",20]
    images["shoot"] = ["assets/player/shoot/survivor-shoot_rifle_",3]
    images["reload"] = ["assets/player/reload/survivor-reload_rifle_",20]
    stage = 0
    magSize = 40
    size = (80,80)
    angle = 0
    image = pygame.image.load(f"{images["idle"][0]}{stage}.png")
    image = pygame.transform.scale(image, size)
    directions = []
    fram = 0
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
            print("no shoot")
            self.secondOpration = ""
    
    def shoot(self):#image
        self.magSize -= 1
        self.game.shoot()


    def setMove(self, direction):
        self.directions.append(direction)
        if self.opration != "reload":
            print("move")
            self.opration = "move"

    def draw(self, screen):
        self.fram += 1
        #reload
        if self.reloadTimer == 0 and self.opration == "reload":
            self.reloadAction()
        elif self.opration == "reload":
            self.reloadTimer -= 1
        #move or shoot
        if self.fram % 3 == 0:
            if self.opration == "move":
                for direction in self.directions:
                    self.move(direction)
            if self.secondOpration == "shoot" and self.opration != "reload":
                if self.magSize > 0:
                    self.shoot()
                else:
                    print("empty mag")
                    #sound - empty mag
                    pass
        #images
        if self.opration == "idle" and self.secondOpration == "shoot":# shoot anmation
                if self.stage >= self.images[self.secondOpration][1]:
                    self.stage = 0
                self.image = pygame.image.load(f"{self.images[self.secondOpration][0]}{self.stage}.png")  
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
                self.image = pygame.transform.scale(self.image, self.size)
                self.image = pygame.transform.rotate(self.image, self.angle)

        if self.fram % 6 == 0:# other anmations
            # print(self.opration)
            self.stage += 1
            if not (self.opration == "idle" and self.secondOpration == "shoot"):
                print("anmation")
                if self.stage >= self.images[self.opration][1]:
                    self.stage = 0
                self.image = pygame.image.load(f"{self.images[self.opration][0]}{self.stage}.png")  
                
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
                self.image = pygame.transform.scale(self.image, self.size)
                self.image = pygame.transform.rotate(self.image, self.angle)
        super().draw(screen)





class Computer(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 3
        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image, (40, 40))

    def shoot(self):
        pass
