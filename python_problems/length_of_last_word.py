"""

"""


def length_last_word(A):
    arr = A.split(' ')
    size = len(arr)
    if size == 1:
        return len(A)

    last_word = arr[-1]

    return len(last_word)


A = "Hello NetSetOs"
print(length_last_word(A))