# insert 'break' in following code so that the comment
# after '#' (including '#') are stripped.


def stripComment(sentence):
    codeonly = ""
    for ch in sentence:
        if ch == '#':
            break
        codeonly += ch
    return codeonly
