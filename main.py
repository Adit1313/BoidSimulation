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
gravFactor = 300
spacing = 50
followFactor = 100

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
    for i in range(0, 3):
        birds.append(Bird(random.uniform(0, WIDTH - BirdWidth), random.uniform(0, HEIGHT - BirdHeight), 0, 0))

def render():
    for b in birds:
        pygame.draw.rect(screen, (RED, GREEN, BLUE), pygame.Rect(int(b.x), int(b.y), BirdWidth, BirdHeight))

def update():
    i = 0
    for b in birds:
        if b.x > WIDTH or b.x < 0:
            b.velX = -b.velX
        if b.y > HEIGHT or b.y < 0:
            b.velY = -b.velY
        
        v1x, v1y = gravitate(i)
        v2x, v2y = avoid(i)
        v3x, v3y = follow(i)

        finalVelX = b.velX + v1x + v2x + v3x
        finalVelY = b.velY + v1y + v2y + v3y

        if math.sqrt(finalVelX**2 + finalVelY**2) > 1:
            finalVelX = (finalVelX / math.sqrt(finalVelX**2 + finalVelY**2))
            finalVelY = (finalVelY / math.sqrt(finalVelX**2 + finalVelY**2))

        b.x = b.x + finalVelX
        b.y = b.y + finalVelY
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
            j = j + 1
            continue
        else:
            cx = cx + b.x
            cy = cy + b.y
            j = j + 1
    cx = cx / (len(birds) - 1)
    cy = cy / (len(birds) - 1)

    delX = (cx - birds[i].x) / gravFactor
    delY = (cy - birds[i].y) / gravFactor
    return delX, delY

def avoid(i):
    j = -1
    delX = 0
    delY = 0

    for b in birds:
        j = j + 1
        if i == j:
            continue
        if distance(b.x, b.y, birds[i].x, birds[i].y) < spacing:
            delX = delX - (b.x - birds[i].x)
            delY = delY - (b.y - birds[i].y)
    
    return delX/100, delY/100

def follow(i):
    j = -1
    delX = 0
    delY = 0

    for b in birds:
        j = j + 1
        if i == j:
            delX = delX + b.x
            delY = delY + b.y
    
    delX = delX / (len(birds) - 1)
    delY = delY / (len(birds) - 1)
    delX = (delX - birds[i].x) / followFactor
    delX = (delY - birds[i].y) / followFactor
    return delX, delY

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

init()
loop()