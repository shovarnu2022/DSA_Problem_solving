def sortColors(A):
    size = len(A)
    red = 0
    blue = 0
    for i in range(size):
        if A[i] == 1:
            red += 1
        elif A[i] == 2:
            blue += 1
    return [1]*red + [2]*blue + [3]*(size-red-blue)


A = [1, 2, 3, 1, 3, 2, 1, 2, 3, 1]
print(sortColors(A))
