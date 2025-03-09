# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.

def valid_parentheses(string):
    openCount = 0
    closeCount = 0
    for char in string:
        if char == "(":
            openCount += 1
        if char == ")":
            closeCount += 1
        if closeCount > openCount:
            return False
    if closeCount == openCount:
        return True
    else:
        return False