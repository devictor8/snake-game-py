import pygame
from elements import *
from handleBody import *

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
running = True
snake = [Snake(250, 50), Snake(275, 50)]
food = Food(225, 50)
direction = "stop"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = checkDirection(direction, snake)
            if event.key == pygame.K_RIGHT:
                direction = "right"
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"
    
    screen.fill("black")
    match direction:
        case "up":
            goUp(snake)
        case "down":
            goDown(snake)
        case "right":
            goRight(snake)
        case "left":
            goLeft(snake)
    
    for s in snake:
        s.draw(screen)
    food.draw(screen)
    snake[0].checkSelfCollision(snake)
    food.checkCollision(snake)
    
    pygame.display.flip()
    clock.tick(15)
pygame.quit()
