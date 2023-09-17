"""
Given an array containing n distinct
numbers taken from 0,1,2,3,...,n.
find the number that is missing from
the array.

Input: [3,0,1]
Output: [2]

n = 2 -> What's missing from 0,1,3 in input
array is 2

it is also guaranteed to have only one 
missing number

Input: [2,3,1,0]
Output: 4

What's missing from 0,1,2,3,4 in input
array is 4

Input: [5,3,2,4,0]

Number that is missing: 1
We Know that we should have all
numbers in range: 0,1,2,3,4,5

Approach: Difference between every 2 consecutive
elements is 1, except difference between 
0,2,.... here is the difference is 2

And therefore, we know that the missing 
element is between 0 and 2, which is 1
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currentSum = sum(nums)
        n = len(nums)
        intendedSum = n*(n+1)/2 # gaussian theorem

        return int(intendedSum - currentSum)
    
















