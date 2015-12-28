def isTriangle(x, y, z):
    if x+y > z and x+z > y and y+z > x:
        return True
    else:
        return False
