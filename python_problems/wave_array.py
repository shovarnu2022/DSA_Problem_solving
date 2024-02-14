"""
Given an array, find out the elements in the array
when plotted in a graph does form a wave or not

Algorithm

For Every Even Position i,
    if current element is smaller than
    previous element, Swap them
    a[i-1] > a[i]   ----> Swap

    if current element is smaller than
    next element, Swap them.
    a[i] < a[i+1] ----> Swap
"""


def wave(arr):
    size = len(arr)
    for index in range(0, size, 2):
        if index > 0 and arr[index-1] > arr[index]:
            arr[index-1], arr[index] = arr[index], arr[index-1]
        if index < size - 1 and arr[index] < arr[index+1]:
            arr[index], arr[index+1] = arr[index + 1], arr[index]
    return arr


A = [3, 5, 12, 2, 6, 10, 7, 9, 8]
print(wave(A))


