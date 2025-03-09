# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    out = 0
    for n in arr:
     if n > 0:
        out += n
    return out