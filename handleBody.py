from elements import Snake
imageHeight = Snake.IMAGE.get_height()
imageWidth = Snake.IMAGE.get_width()

def checkDirection(direction, body):
    if body[1].y <= body[0].y and direction == "down":
        return True
    elif body[1].y >= body[0].y and direction == "up":
        return True
    elif body[1].x <= body[0].x and direction == "right":
        return True
    elif body[1].x >= body[0].x and direction == "left":
        return True
    else:
        return False

def goDown(body):
    y = body[0].y + imageHeight
    
    if checkDirection("down", body):
        body.insert(0, Snake(body[0].x, y, body[0].score))
        body.pop()

def goUp(body):
    y = body[0].y - imageHeight

    if checkDirection("up", body):
        body.insert(0, Snake(body[0].x, y, body[0].score))
        body.pop()

def goRight(body):
    x = body[0].x + imageWidth

    if checkDirection("right", body): 
        body.insert(0, Snake(x, body[0].y, body[0].score))
        body.pop()

def goLeft(body):
    x = body[0].x - imageWidth
    
    if checkDirection("left", body):
        body.insert(0, Snake(x, body[0].y, body[0].score))
        body.pop()
