def getCommonLetters(word1, word2):
    return ''.join(sorted(set(word1).intersection(set(word2))))
