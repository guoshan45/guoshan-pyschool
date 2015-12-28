def isIsosceles(x, y, z):
    a = x > 0 and y > 0 and z > 0
    return a and (x == y or y == z or z == x)
