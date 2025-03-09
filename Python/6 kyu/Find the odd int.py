# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for i in seq:
        count = 0
        for x in seq:
            if i == x:
                count += 1
        if count % 2 >> 0:
            return i