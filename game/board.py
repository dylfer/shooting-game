import pygame, random




class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('wall.png')
        self.image = pygame.transform.scale(self.image, (40, 40))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))




class Board:
    borders = [pygame.Rect(0, 0, 800, 10), pygame.Rect(0, 0, 10, 600), pygame.Rect(0, 590, 800, 10), pygame.Rect(790, 0, 10, 600)]# maby rebove this because rect for inner is used ?
    walls = []
    def __init__(self):
        self.width = 1400
        self.height = 1000

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (50, 50, self.width-100, self.height-100),2)
        for wall in self.walls:
            # screen.blit(wall.image, (wall.x, wall.y))
            pygame.draw.rect(screen, (255,255,255), wall)
            # screen.blit(wall)
        # for border in self.border:
        #     pygame.draw.rect(screen, (255, 255, 255), border)
    
    def generate(self):# convert theis to class objects and add them to the walls list
        width = 25
        margin = 50
        for i in range(3):
            overlap = True
            while overlap:
                length = random.randint(300, 700)
                new_wall = pygame.Rect(random.randint(50,1325-length),random.randint(50,900-width) , length, width)
                new_wall_margin = pygame.Rect(new_wall.left-margin, new_wall.top-margin, new_wall.width+2*margin, new_wall.height+2*margin)
                if i%2 == 0 or not any(new_wall_margin.colliderect(wall) for wall in self.walls):
                    self.walls.append(new_wall)
                    overlap = False

        for i in range(3):
            while True:
                length = random.randint(300, 700)
                new_wall = pygame.Rect(random.randint(50,1325-width) , random.randint(50,900-length) , width, length)
                new_wall_margin = pygame.Rect(new_wall.left-margin, new_wall.top-margin, new_wall.width+2*margin, new_wall.height+2*margin)
                if i%2 == 0 or not any(new_wall_margin.colliderect(wall) for wall in self.walls):
                    self.walls.append(new_wall)
                    break


# testing pourposes
# board = Board()
# screen = pygame.display.set_mode((1400, 1000))
# board.generate()
# board.draw(screen)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     pygame.display.flip()
#     pygame.time.Clock().tick(30)





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