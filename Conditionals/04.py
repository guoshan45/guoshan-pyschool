def Fitness(a, b, c):
    add = a+b+c
    if add >= 13 and a >= 4 and b >= 4 and c >= 4:
        return 'Gold'
    elif add >= 10 and a >= 3 and b >= 3 and c >= 3:
        return 'Silver'
    elif add >= 7 and a >= 2 and b >= 2 and c >= 2:
        return 'Pass'
    else:
        return 'Fail'
