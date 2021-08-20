import pygame
import random
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
    for i in range(0, 25):
        birds.append(Bird(random.uniform(0, WIDTH - BirdWidth), random.uniform(0, HEIGHT - BirdHeight), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)))

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
    return delX, delY


init()
loop()