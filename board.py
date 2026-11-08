import pygame, random
bomb = pygame.image.load("bomb.png")
unopened = pygame.image.load("plain.png")

class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.blocksize = None
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.bombs = []
        self.bombSprites = pygame.sprite.Group()

    def draw(self):

    def grid(self, screen, gridWidth):
        self.blocksize = int(720/gridWidth)
        for row in range(0,800,blocksize):
            row = []
            for col in range(0,800,blocksize):
                row.append()
                rect = pygame.Rect(col, row, blocksize, blocksize)
                pygame.draw.rect(screen, White, rect, 1) #TODO fix grid drawing

    def bomb(self):
        for i in range(self.bombs):
            x = random.randint(720/self.blocksize)
            y = random.randint(720/self.blocksize)
            self.bombs.append([x,y])