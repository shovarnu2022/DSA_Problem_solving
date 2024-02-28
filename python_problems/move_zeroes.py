"""
Given an array of integers, write a function
to move all 0's to the end while
maintaining the relative order of the other elements

Example: 0 1 0 3 12
o/p: 1 3 12 0 0

Are the elements sorted? No, it doesn't have to be the case
say if the array is 0 12 0 1 3 -> 12 1 3 0 0

Input: 0 0 1 3 12
After we reverse:  12 3 1 0 0
After we reverse non-zero: 1 3 12 0 0
Target: 1 3 12 0 0

Cam the entire array only consist of zeroes:

Input: 0 0 0 0 0
Just return the input as is


Brute force approach:

Exmaple: 0 1 0 3 12
Expected O/P: 1 3 12 0 0

steps:

Create new array with the same size as the input
Loop over input array and push non-zero elements to new array
Push zeroes for rest of new array size

moveZeroes(input):
 output = []
 n = input. Length
 Loop as i in range(0,n)
 {
   if(input[i] is non-zero)
      output.add(input[i])
 }
 m=output.length
 Loop in range(m,n)

Time complexity:
O(n+n-m) = O(2n - m)
n:length of input
m: Number of non-zero elements in input

Space Complexity: O(n)

Optimal solution intuition:

0 1 0 3 12 -> 1 3 12 0 0

We want to move the non-zero elements to the beginning
o the array in order

moveZeroes(input){
    output = []
    n = input.Length
    Loop as i in range(0, n){
     if input[i] is non-zero:
        output.add(input[i])
    }
    m = output.Length
    Loop in range(m,n)
        output.add(0)
}



"""


def moveZeroes(nums: list[int]) -> None:
    zero_index = 0
    n = len(nums)

    for non_zero_index in range(0, n):
        if nums[non_zero_index] != 0:
            nums[zero_index] = nums[non_zero_index]
            zero_index += 1

    for i in range(zero_index, n):
        nums[i] = 0

    return nums


arr = [1, 0, 3, 5, 0, 7]
print(moveZeroes(arr))

















