"""
Given an array of integers, write a function
to move all 0's to the end while maintaining
the relative order of the other elements
ex: input: 0 1 0 3 12
output: 1 3 12 0 0

are the elements sorted?
0 12 0 1 3

That doesn't have to be the case

ex2: input: 0 0 1 3 12
After we reverse: 12 3 1 0 0
After we reverse non-zero: 1 3 12 0 0
Target: 1 3 12 0 0
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0
        n = len(nums)
        
        for non_zero_index in range(0, n):
            if(nums[non_zero_index]!=0):
                nums[zero_index] = nums[non_zero_index]
                zero_index+=1
        
        for i in range(zero_index, n):
            nums[i] = 0
        
        
        


        





