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

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def render(b):
    pygame.draw.rect(screen, (RED, GREEN, BLUE), pygame.Rect(b.x, b.y, BirdWidth, BirdHeight))

def init():
    for i in range(0, 25):
        birds.append(Bird(random.randint(0, WIDTH - BirdWidth), random.randint(0, HEIGHT - BirdHeight)))

def loop():
    done = False
    while not done:
        for b in birds:
            render(b)
            #update(b)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()

init()
loop()