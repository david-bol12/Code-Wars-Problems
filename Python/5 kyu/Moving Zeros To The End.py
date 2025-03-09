# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    zeroCount = array.count(0)
    while zeroCount > 0:
        array.remove(0)
        array.append(0)
        zeroCount -= 1
    return array