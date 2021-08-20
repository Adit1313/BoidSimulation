import pygame
import random
import math
from pygame.locals import *

#Constants
RED = 37
GREEN = 150
BLUE = 190
BirdWidth = 10
BirdHeight = 10
WIDTH = 800
HEIGHT = 600
gravFactor = 100

#Begin
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
birds = []

#Bird Class
class Bird:
    def __init__(self, x, y, velX, velY):
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY

#Methods
def init():
    for i in range(0, 2):
        birds.append(Bird(random.uniform(0, WIDTH - BirdWidth), random.uniform(0, HEIGHT - BirdHeight), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)))

def render():
    i = 0
    for b in birds:
        if i == 1:
            pygame.draw.rect(screen, (255, GREEN, BLUE), pygame.Rect(int(b.x), int(b.y), BirdWidth, BirdHeight))
        else:
            pygame.draw.rect(screen, (RED, GREEN, BLUE), pygame.Rect(int(b.x), int(b.y), BirdWidth, BirdHeight))
        i = i + 1

def update():
    i = 0
    for b in birds:
        if b.x > WIDTH or b.x < 0:
            b.velX = -b.velX
        if b.y > HEIGHT or b.y < 0:
            b.velY = -b.velY
        
        v1x, v1y = gravitate(i)
        #v2x, v2y = avoid(i)

        b.x = b.x + b.velX + v1x
        b.y = b.y + b.velY + v1y
        i = i + 1

def loop():
    done = False
    while not done:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
        update()
        render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()

def gravitate(i):
    cx = 0
    cy = 0
    j = 0
    for b in birds:
        if j == i:
            continue
        else:
            cx = cx + b.x
            cy = cy + b.y
        j = j + 1
    cx = cx / (len(birds) - 1)
    cy = cy / (len(birds) - 1)

    delX = (cx - birds[i].x) / gravFactor
    delY = (cy - birds[i].y) / gravFactor

    if i == 1:
        print(delX, " ", delY)
        print(cx, " ", cy, " ", birds[i].x, " ", birds[i].y)
    return delX, delY

def avoid(i):
    j = 0
    delX = 0
    delY = 0

    for b in birds:
        if i == j:
            continue
        if distance(birds[j].x, birds[j].y, birds[i].x, birds[i].y) < 50:
            #do something
            delX = 0
        

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

init()
loop()