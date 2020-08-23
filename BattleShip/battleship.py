"""
A Game opted from Space Invaders video from
https://www.youtube.com/watch?v=FfWpgLFMI7w
"""
import pygame 
import os

# Initializing the pygame
pygame.init()

# create a Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("BattleShip by @BlitzBlaster31")
icon = pygame.image.load(os.path.dirname(__file__)+"/ufo.png")
pygame.display.set_icon(icon)
running = True


# Main loop
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
    screen.fill((155,110,50))
    pygame.display.update()