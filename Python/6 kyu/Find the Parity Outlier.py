# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    x = 0
    for item in integers[0:3]:
        if item % 2 == 0:
            x = x + 1
    if x >= 2:
        even = True
    else:
        even = False
    if even == True:
        for number in integers:
            if number % 2 != 0:
                n = number
    else:
        for number in integers:
            if number % 2 == 0:
                n = number
    return n