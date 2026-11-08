from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from game import Game
from board import Board

pygame.init()
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 720
OFFSET = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Minesweeper')
game = Game(Board, SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

#surfaces
font = pygame.font.Font("cocogoose.ttf", 30)
Grey = (29, 29, 27)
White = (255, 255, 255)
highscore_text_surface = font.render("000", False, White)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            Game.game.reveal(pos[0], pos[1])
        elif event.type == pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            Game.game.flag(pos[0], pos[1])
    Board.bombSprites.update()
    #TODO screen.blit(highscore_text_surface, (50,25,50,50))
    screen.fill(Grey)

    clock.tick(60)