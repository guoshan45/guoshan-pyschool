def quadratic(a, b, c): 
    D = b*b -4*a*c
    if D >0:
        return 'This equation has 2 real roots.'
    elif D==0:
        return 'This equation has 1 real root.'
    else:
        return 'This equation has 2 complex roots.'