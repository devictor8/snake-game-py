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