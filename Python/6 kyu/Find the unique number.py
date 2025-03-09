# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i