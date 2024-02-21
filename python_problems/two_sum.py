"""
Find out pairs with given sum value of an array
arr = [5,7,4,3,9,8,19.21]
sum = 17
"""


def two_sum(arr, sum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left]+arr[right] > sum:
            right = right - 1
        elif arr[left]+arr[right] < sum:
            left = left + 1
        elif arr[left]+arr[right] == sum:
            print("Values of pair are", arr[left], "&", arr[right])
            right = right - 1
            left = left + 1


sample_arr = [5, 7, 4, 3, 9, 8, 19.21]
sum_target = 17
two_sum(sample_arr, sum_target)

