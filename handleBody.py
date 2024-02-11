from elements import Snake
imageHeight = Snake.IMAGE.get_height()
imageWidth = Snake.IMAGE.get_width()

def checkDirection(direction, body):
    if body[1].y <= body[0].y or body[0].y == 0:
        return "down"
    if body[1].y >= body[0].y or body[0].y == 400:
        return "up"
    if body[1].x <= body[0].x or body[0].x == 0:
        return "right"
    if body[1].x >= body[0].x or body[0].x == 800:
        return "left"
    return direction

def goDown(body):
    y = body[0].y + imageHeight if body[0].y + imageHeight <= 400 else 0
    
    if body[1].y <= body[0].y or body[0].y == 0:
        body.insert(0, Snake(body[0].x, y))
        body.pop()

def goUp(body):
    y = body[0].y - imageHeight if body[0].y - imageHeight >= 0 else 400

    if body[1].y >= body[0].y or body[0].y == 400:
        body.insert(0, Snake(body[0].x, y))
        body.pop()

def goRight(body):
    x = body[0].x + imageWidth if body[0].x + imageWidth <= 800 else 0

    if body[1].x <= body[0].x or body[0].x == 0: 
        body.insert(0, Snake(x, body[0].y))
        body.pop()

def goLeft(body):
    x = body[0].x - imageWidth if body[0].x - imageWidth >= 0 else 800
    
    if body[1].x >= body[0].x or body[0].x == 800:
        body.insert(0, Snake(x, body[0].y))
        body.pop()
