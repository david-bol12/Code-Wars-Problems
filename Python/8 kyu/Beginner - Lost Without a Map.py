# Given an array of integers, return a new array with each value doubled.

def maps(a):
    newList = []
    for i in a:
        i *= 2
        newList.append(i)
    return newList