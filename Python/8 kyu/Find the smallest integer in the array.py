# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):
    arr.sort()
    return arr[0]