import os
import pygame
from random import randint

class Snake:
    IMAGE = pygame.image.load("./assets/snake-body.png")

    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score
    
    def draw(self, screen):
            screen.blit(Snake.IMAGE, (self.x, self.y))
    
    def checkSelfCollision(self, body):
        for c in range(1, len(body)):
            if self.x == body[c].x and self.y == body[c].y:
                print("bateu em si mesmo")
                return False
        return True
    
    def checkBorderCollision(self):
        if self.x <= 0 - Snake.IMAGE.get_width() or self.x >= 1000:
            print('passou da borda do lado')
            return False
        if self.y <= 0 - Snake.IMAGE.get_height() or self.y >= 600:
            print('passou da borda superior/inferior')
            return False
        return True
    
    def scoreUpdate(self, screen):
            font = pygame.font.Font(None, 25)
            score_text = font.render(f"score: {self.score}", True, (255,255,255))
            screen.blit(score_text, (50, 50))
    

class Food: 
    IMAGE = pygame.image.load("./assets/food.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen):
        screen.blit(Food.IMAGE, (self.x, self.y))

    def checkFoodEat(self, snake, score):
        if self.x == snake[0].x and self.y == snake[0].y:
            self.addTail(snake, self.x, self.y)
            self.x = randint(0, 39) * 25
            self.y = randint(0, 23) * 25
            return score + 1
        return score
    
    def addTail(self, body, x, y):
        body.insert(0, Snake(x, y, body[0].score + 1))