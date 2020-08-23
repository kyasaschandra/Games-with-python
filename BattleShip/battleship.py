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

# Setting an icon
icon = pygame.image.load(os.path.dirname(__file__)+"/ufo.png")
pygame.display.set_icon(icon)

#  Loading background
bgimg = pygame.image.load(os.path.dirname(__file__)+"/bg.png")

# Enemy
enemyImg = pygame.image.load(os.path.dirname(__file__)+"/ufoenemy.png")
eX = []
eY = []
edx = []
state=[]

def createEnimies(lvl,speed):
    global eX
    global eY
    global edx
    global state
    
    eX = []
    eY = []
    edx = []
    state = []
    for i in range(lvl):
        eX.append(random.randint(5,730))
        eY.append(random.randint(10,180))
        edx.append(random.choice([1*speed,-1*speed]))
        state.append(True)

lvlLimit = 5
lvl = 1
speed = 1
showlvl = 1

def enemy(X,Y,i):
    global eX
    global eY
    global edx
    eX[i] = X
    eY[i] = Y
    if eX[i] > 730:
        edx[i] *= -1
        eX[i] = 730
        eY[i] = eY[i] + 35
    elif eX[i] < 5:
        edx[i] *= -1
        eX[i] = 5
        eY[i] = eY[i] + 35
    if state[i]:
        screen.blit(enemyImg,(eX[i], eY[i]))
    
createEnimies(lvl,speed)

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

# Missile
missileImg = pygame.image.load(os.path.dirname(__file__)+"/bullet.png")
blastImg = pygame.image.load(os.path.dirname(__file__)+"/explosion.png")
bX = pX
bY = pY
bdy = 8
bState = False

def fire(X,Y):
    global bState
    bState = True
    screen.blit(missileImg,(X+16, Y+10))

def collide(eX, eY, bX, bY, x):
    if x:
        dis = (((eX-bX)**2)+((eY-bY)**2))**(0.5)
        #print(dis)
        if dis < 35:
            return True
        else:
            return False

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf",32)
sX=10
sY=10

def showScore(X,Y):
    s = font.render("Score : "+str(score)+" Level : "+str(showlvl), True, (255,255,255))
    screen.blit(s,(X,Y))
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
            if e.key == pygame.K_SPACE:
                if not bState:
                    bY = pY
                    bX = pX
                    fire(bX,bY)
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_UP or e.key == pygame.K_RIGHT or e.key == pygame.K_DOWN:
                pdx = 0
                pdy = 0
        
    screen.fill((155,110,50))
    screen.blit(bgimg,(0,0))
    player(pX+2*pdx,pY+2*pdy)
    showScore(sX,sY)
    if bState and bY > 5:
        bY -= bdy
        fire(bX, bY)
    else:
        bState = False
    for i in range(lvl):
        enemy(eX[i]+1*edx[i],eY[i],i)
        if collide(eX[i],eY[i],bX,bY,state[i]):
            bY = pY
            bX = pX
            bState = False
            score+=1
            print(score)
            screen.blit(blastImg,(eX[i],eY[i]))
            state[i] = False
    pygame.display.update()
    if True in state:
        continue
    else:
        lvl+=1
        if lvl > lvlLimit:
            lvl = 0
            speed+=0.3
            showlvl += 1
            if showlvl%5 == 0:
                lvlLimit+=5
                speed = 1
                lvl = 1
        createEnimies(lvl,speed)

    