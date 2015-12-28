def pairwiseScore(seqA, seqB): 
    signed = ''
    score = 0
    for i in range(len(seqA)):
      if seqA[i] == seqB[i]:
          signed += '|'
          if signed[-2:] == '||':
              score += 3
          else:
              score += 1
      else:
          signed += ' '
          score -= 1
    return '%s\n%s\n%s\nScore: %d' % (seqA, signed, seqB, score)