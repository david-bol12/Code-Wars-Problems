# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    # your code here
    l = 200000000000000
    for item in s.split(' '):
        if len(item) < l:
            l = len(item)
    return l # l: shortest word length