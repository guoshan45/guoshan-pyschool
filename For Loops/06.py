def addEvenNumbers(start, end):
    count = 0
    for i in range(start, end+1):
        if i % 2 == 0:
            count += i
    return count
