# Write a function, given a string of characters, return the string
# together with '_'s of the same length.


def underline(title):
    return title + '\n' + len(title)*'_'
