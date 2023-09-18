"""
Given an array of integers and a target
value, return the indices of 2 numbers
that add up to the input target value

0: 3, 1: 6, 2:12, 3:14   Target = 15
return [0, 2]

Can an input have multiple solutions? No

Can you use the same element twice? No

Are we guaranteed atleast 2 integers in the array? Yes

Are we guaranteed to always have a solution? Yes

numbers = [2,11,7,15], target=26
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(0, n):
            goal = target - nums[i]
            if(goal in m):
                return [m[goal], i]
            m[nums[i]] = i


s = Solution()
answer = s.twoSum([3, 2, 1, 5], 8)

     
        








