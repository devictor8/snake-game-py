import pygame
from elements import *
from handleBody import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
font = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
running = True
snake = [Snake(250, 50, 0), Snake(275, 50, 0)]
food = Food(225, 50)
direction = "stop"
player_score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left" if checkDirection("left", snake) else direction
            if event.key == pygame.K_RIGHT:
                direction = "right" if checkDirection("right", snake) else direction
            if event.key == pygame.K_UP:
                direction = "up" if checkDirection("up", snake) else direction
            if event.key == pygame.K_DOWN:
                direction = "down" if checkDirection("down", snake) else direction
    
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
    if not snake[0].checkBorderCollision() or not snake[0].checkSelfCollision(snake):
        running = False
    else:
        running = True
    score = food.checkFoodEat(snake, player_score)
    snake[0].scoreUpdate(screen)

    pygame.display.flip()
    clock.tick(15)
pygame.quit()
