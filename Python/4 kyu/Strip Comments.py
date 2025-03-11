# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.

def strip_comments(strng, markers):
    result = ''
    for line in strng.split('\n'):
        line_split = line
        for marker in markers:
            line_split = line_split.split(marker)[0]
        result += f'{line_split.rstrip()}\n'
    return result.removesuffix('\n')