import pygame

class Brick:
    def __init__(self, x, y, width=80, height=30, color="green"):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)
