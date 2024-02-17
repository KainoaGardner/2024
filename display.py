from settings import *
from board import *

def display():
    screen.fill("#84817a")
    board.display()
    pygame.display.update()
    clock.tick(FPS)