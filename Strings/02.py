def countLetter(word, letter):
    count = 0
    for str in word:
        if str == letter:
            count += 1
    return count
