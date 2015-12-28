def addOddNumbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += num
    return count
