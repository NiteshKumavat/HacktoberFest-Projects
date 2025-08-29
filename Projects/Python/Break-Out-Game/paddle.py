import pygame

class Paddle:
    def __init__(self, x, y, width=150, height=20, color="blue", speed=7):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x + self.rect.width < screen_width:
            self.rect.x += self.speed
