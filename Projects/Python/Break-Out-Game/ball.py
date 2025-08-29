import pygame

class Ball:
    def __init__(self, x, y, radius=10, color="red", speed_x=5, speed_y=-5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, screen_width, screen_height):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce on walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0:
            self.speed_y = -self.speed_y

    def bounce(self):
        self.speed_y = -self.speed_y
