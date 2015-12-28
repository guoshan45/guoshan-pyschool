def countVowels(word):
    count = 0
    for str in word:
        if str in 'aeiou':
            count += 1
    return count
