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
    for b in birds:
        b.x = b.x + b.velX
        b.y = b.y + b.velY

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

init()
loop()