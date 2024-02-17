import pygame

pygame.init()

TILESIZE = 150
MARGINSIZE = TILESIZE // 2
WIDTH = TILESIZE * 4 + MARGINSIZE * 2
HEIGHT = TILESIZE * 4 + MARGINSIZE * 2
FPS = 60
font1 = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE)
font2 = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE * 4//5)
font3 = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE * 3//5)
font4 = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE // 2)
fontSmall = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE//2)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()