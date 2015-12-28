def removeVowels(word):
    for str in word:
        if str.lower() in 'aeiou':
            word = word.replace(str, '')
    return word
