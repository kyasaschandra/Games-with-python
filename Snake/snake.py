"""
A Snake game made with help of Youtbe video by Tech with Tim
https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
"""

import pygame
import random
import tkinter as tk
from tkinter import messagebox

width = 500
rows = 20
def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0),(10,10))
    snack = cube(randomSnack(rows,s), color=(0,0,255)) 
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows,s), color=(0,0,255))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda x:x.pos,s.body[x+1:])):
                print("score: ",len(s.body)-1)
                message_box("You Lost!","Play Again\nYour Score: "+str(len(s.body)-1))
                s.reset((10,10))
                break
        redrawWindow(win)

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width,rows,surface)
    pygame.display.update()

def drawGrid(width,rows,surface):
    size = width//rows
    x = 0
    y = 0
    for _ in range(rows):
        x = x + size
        y = y + size

        pygame.draw.line(surface,(255,255,255),(x,0),(x,width))
        pygame.draw.line(surface,(255,255,255),(0,y),(width,y))

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
    
    def move(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for _ in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0],0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0],c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)
    
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = -1


class cube(object):
    rows = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
 
       
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            center = dis//2
            r = 3
            circle1 = (i*dis+center-r,j*dis+8)
            circle2 = (i*dis + dis -r*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circle1, r)
            pygame.draw.circle(surface, (0,0,0), circle2, r)

def randomSnack(rows, item):  
    postions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda x:x.pos == (x,y), postions))) > 0:
            continue
        else:
            break
    return (x,y)



def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass

main()