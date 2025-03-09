# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    out = []
    for i in str(n):
        out.append(int(i))
    out.reverse()
    return out