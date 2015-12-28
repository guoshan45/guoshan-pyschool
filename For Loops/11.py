def sumOfDigit(num):
    s = 0
    while num:
        s += num % 10
        num = num/10
    return s
