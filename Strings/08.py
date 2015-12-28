def getVowels(word):
    vowels = []
    for str in word:
        vo = str.lower()
        if vo in 'aeiou':
            vowels.extend(str)
    return vowels
