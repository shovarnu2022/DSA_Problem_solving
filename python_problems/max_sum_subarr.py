"""
Given an array, find max sum of sub array within an array

Algorithm
************

curr_sum = 0
max_so_far = a[0]
for i in range(0, size):
   curr_sum = curr_sum + arr[i]
   if max_so_far < curr_sum:
      max_so_far = curr_sum
   if curr_sum < 0:
      curr_sum = 0
"""


def max_sum_subarray(arr):
    size = len(arr)
    max_so_far = arr[0]
    curr_sum, start, end, temp = 0, 0, 0, 0
    for i in range(0, size):
        curr_sum = curr_sum+arr[i]
        if max_so_far < curr_sum:
            max_so_far = curr_sum
            start = temp
            end = i
        if curr_sum < 0:
            curr_sum = 0
            temp = i+1

    print("Maximum sum Subarray is", max_so_far)
    print("Start index of window is", start)
    print("End index of window is", end)


arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
max_sum_subarray(arr)







