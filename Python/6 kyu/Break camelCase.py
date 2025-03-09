# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    answer = ""
    for letter in s:
        if letter.isupper():
            answer += " "
            answer += letter
        else:
            answer += letter
    return answer