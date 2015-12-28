def capitalizeVowels(word):
    for str in word:
        if str in 'aeiou':
            word= word.replace(str,str.upper())
    return word
   