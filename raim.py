import pygame
import sys
import random

width = 800
height = 600

class Rain:
    def __init__(self):
        self.x = random.randrange(1, width)
        self.y = random.randrange(-height,height)
        self.y_speed = random.uniform(1.75, 2.50)

    def fall(self):
        self.y += self.y_speed
        if self.y >= (height):
            self.y = random.randrange(-height,height)

    def show(self):
        pygame.draw.line(window, (255,0,0), (self.x, self.y), (self.x, self.y+10))

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("purple_rain")

my_drops = []
for i in range(500):
    my_drops.append(Rain())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))  

    for i in range(500):
        my_drops[i].fall()
        my_drops[i].show()

    pygame.display.update()
