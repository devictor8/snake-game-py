import os
import pygame
from random import randint

class Snake:
    IMAGE = pygame.image.load("./assets/snake-body.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
            screen.blit(Snake.IMAGE, (self.x, self.y))
    
    def checkSelfCollision(self, body):
        for c in range(1, len(body)):
            if self.x == body[c].x and self.y == body[c].y:
                print("bateu")

class Food: 
    IMAGE = pygame.image.load("./assets/food.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        screen.blit(Food.IMAGE, (self.x, self.y))

    def checkCollision(self, snake):
        if self.x == snake[0].x and self.y == snake[0].y:
            self.addTail(snake, self.x, self.y)
            self.x = randint(0, 31) * 25
            self.y = randint(0, 15) * 25
        
    def addTail(self, body, x, y):
        body.insert(0, Snake(x, y))