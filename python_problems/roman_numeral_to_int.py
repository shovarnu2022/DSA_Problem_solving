"""
1. Iterate throughout. Take two pointers
Curr which is at i position.
next at i+1 position.
2. Check curr >= next. Keep adding to Output
if not, add(next-curr) to Output

"""


def value(A):
    if A == 'I':
        return 1
    if A == 'V':
        return 5
    if A == 'X':
        return 10
    if A == 'L':
        return 50
    if A == 'C':
        return 100
    if A == 'D':
        return 500
    if A == 'M':
        return 1000


def romantoint(A):
    i, result = 0, 0
    while i < len(A):
        curr = value(A[i])
        if i+1 < len(A):
            next = value(A[i + 1])
            if curr >= next:
                result = result + curr
                i += 1
            else:
                result = result + (next-curr)
                i += 2
        else:
            result = result + curr
            i += 1
    return result


print(romantoint("CLLIVI"))





