import pygame, random
import board
White = (255, 255, 255)
block1 = pygame.image.load("1.png")
block2 = pygame.image.load("2.png")
block3 = pygame.image.load("3.png")
block4 = pygame.image.load("4.png")
block5 = pygame.image.load("5.png")
block6 = pygame.image.load("6.png")
block7 = pygame.image.load("7.png")
block8 = pygame.image.load("8.png")
flag = pygame.image.load("flag.png")
bomb = pygame.image.load("bomb.png")
redbomb = pygame.image.load("red-bomb.png")
wrong = pygame.image.load("wrong-flag.png")

class Game:
    def __init__(self, board, screen_width, screen_height, offset):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.run = True
        self.flags = 0
        self.highscore = 0
        self.score = 0
        self.difficulty = "easy"
        self.gridWidth = 9
        self.gridHeight = 9
        self.bombs = 10
        self.flags = 10
        self.bombPositions = []
        self.board = board.Board()

    def run(self):
        pass

    def reset(self):
        self.score = 0
        self.flags = 0
        self.difficulty = "easy"

    def difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "medium":
            self.gridWidth = 16
            self.gridHeight = 16
            self.bombs = 40
            self.flags = 40
        elif difficulty == "hard":
            self.gridWidth = 16
            self.gridHeight = 30
            self.bombs = 99
            self.flags = 99

    def drawBoard(self, screen):
        board.Board.grid(screen, self.gridWidth)

    def bomb(self):
        board.Board.bomb()

    def reveal(self, x, y):
        if [x,y] in bombPositions:
            self.run = False

    def flag(self):
        self.flags -= 1
        pass