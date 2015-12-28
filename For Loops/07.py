# Insert 'continue' in following code so that it returns a
# string with no vowels.


def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou':
            continue
        novowels += ch
    return novowels
