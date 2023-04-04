import pygame
import numpy as np
import random

class BrownianMotion:
    def __init__(self, color, x, y, size, speed, direction,screen = None):
        if screen != None:
            self.screen = screen
        else:
            self.screen = pygame.display.set_mode((640, 640))
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = direction

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
        

    def move(self):
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)
        pygame.display.flip()

    def change_direction(self):
        if self.x > pygame.display.Info().current_w :
            self.x = pygame.display.Info().current_w
            self.direction = random.uniform(0, 2 * np.pi)
        elif self.x < 0:
            self.x = 0
            self.direction = random.uniform(0, 2 * np.pi)
        elif self.y > pygame.display.Info().current_h:
            self.y = pygame.display.Info().current_h
            self.direction = random.uniform(0, 2 * np.pi)
        elif self.y < 0:
            self.y = 0
            self.direction = random.uniform(0, 2 * np.pi)



