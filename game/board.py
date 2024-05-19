import pygame, random




class Wall:
    def __init__(self, rect, marginRect, length, rotation):
        self.rect = rect
        self.marginRect = marginRect
        self.length = length
        self.rotation = rotation
        self.image = pygame.image.load('assets/wall.png')
        self.image = pygame.transform.scale(self.image,  (25, 200))
        if self.rotation == 1:
            self.image = pygame.transform.rotate(self.image, 90)

    def draw(self, screen):
        for i in range(self.length):
            if self.rotation == 0:
                screen.blit(self.image, (self.rect.x, self.rect.y+i*200))
            else:
                screen.blit(self.image, (self.rect.x+i*200, self.rect.y))




class Board:
    borders = [pygame.Rect(0, 0, 800, 10), pygame.Rect(0, 0, 10, 600), pygame.Rect(0, 590, 800, 10), pygame.Rect(790, 0, 10, 600)]# maby rebove this because rect for inner is used ?
    walls = []
    def __init__(self):
        self.width = 1400
        self.height = 1000

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (50, 50, self.width-100, self.height-100),2)
        for wall in self.walls:
            wall.draw(screen)
            # screen.blit(wall.image, (wall.x, wall.y))
            # pygame.draw.rect(screen, (255,255,255), wall)
            # screen.blit(wall)
        # for border in self.border:
        #     pygame.draw.rect(screen, (255, 255, 255), border)
    
    def generate(self):# convert theis to class objects and add them to the walls list
        self.walls = []
        width = 25
        margin = 50
        for i in range(3):
            while True:#vertical
                length = random.randint(2, 4)
                newWall = pygame.Rect(random.randint(50,1325-length*200),random.randint(50+margin,900-width-margin) , length*200, width)
                NewWallMargin = pygame.Rect(newWall.left, newWall.top-margin, newWall.width, newWall.height+2*margin)
                if  not any(NewWallMargin.colliderect(wall) for wall in self.walls):#i%2 == 1 or
                    # pygame.draw.rect(screen, (255,255,255), NewWallMargin, 2)#uncomment to see wall margin collision
                    self.walls.append(Wall(newWall, NewWallMargin,length, 1))
                    break
            while True:#horizontal
                length = random.randint(2, 4)
                newWall = pygame.Rect(random.randint(50+margin,1325-width-margin) , random.randint(50,900-length*200) , width, length*200)
                NewWallMargin = pygame.Rect(newWall.left-margin, newWall.top, newWall.width+2*margin, newWall.height)
                if  not any(NewWallMargin.colliderect(wall) for wall in self.walls):#i%2 == 1 or
                    # pygame.draw.rect(screen, (255,255,255), NewWallMargin, 2)#uncomment to see wall margin collision
                    self.walls.append(Wall(newWall, NewWallMargin,length, 0))
                    break



# testing pourposes
board = Board()
screen = pygame.display.set_mode((1400, 1000))
board.generate()
board.draw(screen)
i = 0
# screen.fill((0,0,0))
# board.generate()
# board.draw(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if i % 90 == 0:
        screen.fill((0,0,0))
        board.generate()
        board.draw(screen)
    i += 1
    pygame.display.flip()
    pygame.time.Clock().tick(30)





# ai grnerated test
# import unittest
# import pygame
# from board import Board

# class TestBoard(unittest.TestCase):
#     def setUp(self):
#         self.board = Board()

#     def test_initial_state(self):
#         self.assertEqual(self.board.width, 1400)
#         self.assertEqual(self.board.height, 1000)
#         self.assertEqual(self.board.walls, [])

#     def test_generate(self):
#         self.board.generate()
#         self.assertTrue(len(self.board.walls) > 0)

#     def test_draw(self):
#         pygame.init()
#         screen = pygame.display.set_mode((1400, 1000))
#         self.board.generate()
#         self.board.draw(screen)
#         pygame.quit()

# if __name__ == '__main__':
#     unittest.main()