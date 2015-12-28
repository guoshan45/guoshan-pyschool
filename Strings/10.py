def startEndVowels(word):
    if len(word) != 0:
        if word[0].lower() in 'aeiou' and word[len(word)-1].lower() in 'aeiou':
            return 'True'
        else:
            return 'False'
    else:
        return 'False'
