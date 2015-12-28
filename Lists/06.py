def countOddNumbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count
