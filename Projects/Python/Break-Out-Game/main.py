import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

pygame.init()


WIDTH, HEIGHT = 850, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

paddle = Paddle(WIDTH//2 - 75, HEIGHT - 40)
ball = Ball(WIDTH//2, HEIGHT//2)
gap = 5



bricks = []
for row in range(5):
    for col in range(10):
        bricks.append(Brick(col * (80 + gap), row * (30 + gap)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.move(keys, WIDTH)
    ball.move(WIDTH, HEIGHT)

    if paddle.rect.collidepoint(ball.x, ball.y + ball.radius):
        ball.bounce()

    for brick in bricks:
        if brick.alive and brick.rect.collidepoint(ball.x, ball.y):
            brick.alive = False
            ball.bounce()

    if ball.y - ball.radius > HEIGHT:
        print("Game Over!")
        running = False

    screen.fill("black")
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
