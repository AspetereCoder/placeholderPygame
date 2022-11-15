import pygame

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()
font_size = 15
font = pygame.font.Font(pygame.font.get_default_font(), font_size)