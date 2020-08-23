"""
A Game opted from Space Invaders video from
https://www.youtube.com/watch?v=FfWpgLFMI7w
"""
import pygame 
import os
import random

# Initializing the pygame
pygame.init()

# create a Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("BattleShip by @BlitzBlaster31")
icon = pygame.image.load(os.path.dirname(__file__)+"/ufo.png")
pygame.display.set_icon(icon)

# Enemy
enemyImg = pygame.image.load(os.path.dirname(__file__)+"/ufoenemy.png")
eX = random.randint(5,730)
eY = random.randint(10,230)
edx = -1
lvl = 0.1

def enemy(X,Y):
    global eX
    global eY
    global edx
    eX = X
    eY = Y
    if eX > 730:
        edx *= -1
        eX = 730
        eY = eY + 5
    elif eX < 5:
        edx*=-1
        eX = 5
        eY = eY + 5
    screen.blit(enemyImg,(eX, eY))


# Player
playerImg = pygame.image.load(os.path.dirname(__file__)+"/space-invaders.png")
pX = 370
pY = 500
pdx = 0
pdy = 0

def player(X,Y):
    global pX
    global pY
    pX = X
    pY = Y
    if pX > 730:
        pX = 730
    if pX < 5:
        pX = 5
    if pY > 530:
        pY = 530
    if pY < 10:
        pY=10
    screen.blit(playerImg,(pX,pY))

# Main loop
running = True
while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                pdx = -1
            if e.key == pygame.K_UP:
                pdy = -1
            if e.key == pygame.K_DOWN:
                pdy = 1
            if e.key == pygame.K_RIGHT:
                pdx = 1
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_UP or e.key == pygame.K_RIGHT or e.key == pygame.K_DOWN:
                pdx = 0
                pdy = 0
        
    screen.fill((155,110,50))
    enemy(eX+lvl*edx,eY)
    player(pX+1*pdx,pY+1*pdy)
    
    pygame.display.update()