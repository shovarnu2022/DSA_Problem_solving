"""
remove duplicates from sorted array

Algorithm

temp = [0]*n
pivot = 0

for last_o in range(0, n-1):
    if arr[last_o] != arr[last_o + 1]
    temp[pivot] = arr[last_o]
    pivot += 1

arr[]
"""


def remove_duplicates_space(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    temp = [0] * n
    pivot = 0
    for last_o in range(0, n-1):
        if arr[last_o] != arr[last_o+1]:
            temp[pivot] = arr[last_o]
            pivot = pivot+1
    temp[pivot] = arr[n-1]
    return temp[0:pivot+1]


def remove_duplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr
    pivot = 0
    for last_o in range(0, n-1):
        if arr[last_o] != arr[last_o+1]:
            arr[pivot] = arr[last_o]
            pivot = pivot+1
    arr[pivot] = arr[n-1]
    return arr[0:pivot+1]


arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr))


# dict method
dict1 = {
    'car': ["Ford", "Toyota", "Ford", "Toyota"],
    'brand': ["Mustang", "Ranz", "Mustang", "Ranz"]
}

dict2 = {}

for key, value in dict1.items():
    dict2[key] = set(value)
print(dict2)













