def getEvenNumbers(numbers):
    a = []
    for num in numbers:
        if num % 2 == 0:
            a.append(num)
    return a
