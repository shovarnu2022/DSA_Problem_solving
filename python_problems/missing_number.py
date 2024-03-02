"""
Given an array containing n distinct
numbers taken from 0, 1, 2, 3, ..., n
find the number that is missing from the array.

Input: [3, 0, 1]
Output: 2

Why?
Given an array containing n distinct numbers taken from 0,1,2,3,...,n.
find the number that is missing from the array.

n = 3 -> What's missing from 0,1,3 in input array is 2

Step 1 Constraint questions:

Are all the numbers in the array unique?
# Yes, you will be given n distinct numbers

Are we guaranteed to have only one missing number?
# Yes

What should we return if we receive an empty array?

input: []

This is not allowed, the input will have atleast a single element
in it (size will never be less than 1)


Step 2: Test
Input: [2, 3, 1, 0]
Output: 4

Why?
n = 4 -> What's missing from 0,1,2,3,4 in input array is 4.

Input: [1]
Output: 0

Why?
n = 1 -> What's missing from 0, 1 in input array is 0

Approach 1:

Input: [5, 3, 2, 4, 0]
Number that is missing: 1
We know that we should have all numbers in
range: 0, 1, 2, 3, 4, 5

We can sort the input, this way we will have 0, 2, 3, 4, 5

Difference between every consecutive element is 1, except difference
between 0,2,... here is the difference is 2

Now we know that the missing element is between 0 and 2,
which is 1

Steps:
> sort the array
> If current element is bigger than the previous element by
more than one, the missing number is the current element-1

How to implement this:

missingNumber(input){
    sortedInput = sort(input)
    for i in range[1, sortedInput.Length]{
        expectedNumber = sortedInput[i] - 1
        if(sortedInput[i - 1] != expectedNumber)
            return expectedNumber
    }
}

Approach 2:
Input: [3, 0, 1]
Output: 2

Given an array containing n distinct numbers taken from
0,1,2,3,...,n
find the number that is missing from the array.

We know for a fact that we should have all the number
from 0,...,n, but one number will be missing

Is there a way for us to loop from 0,...,n and for each number,
we can verify whether it exists or not in the array?

First thought:
> Loop from 0,...,n
> For each number,do another loop over our input to see
if that number exist or not, if we reached end of input
& we haven't found it, it doesn't exist, so we return it

findMissing(input){
    for i in range[0...n]{
        found = false
        for number in input{
            if i == number{
                found = true
            }
        }
        if found is false
            return i
    }
}
"""


# def missingNumber(nums: list[int]) -> int:
#     n = len(nums)
#     currentSum = 0
#     for i in range(n):
#         currentSum += nums[i]
#     intendedSum = 0
#     for i in range(n+1):
#         intendedSum += i
#     return intendedSum - currentSum


"""
Optimal solution: 
input: [4,1,2,0]
n = 4

intendedSum = n*(n+1)/2 = 4*5/2 = 10
actualSum = 4+1+2+0 = 7
missingNum = intendedSum - actualSum = 10 - 7 = 3

Implementation: 

missingNumber(input){
    n = input.length
    intendedSum = n*(n+1)/2
    actualSum = 0
    for num in input {
        actualSum += number
    }
    return (intendedSum - actualSum)
}
"""


def missingNumber(nums: list[int]) -> int:
    currentSum = sum(nums)
    n = len(nums)
    intendedSum = n*(n+1)/2

    return int(intendedSum - currentSum)


arr = [4, 1, 2, 0]
print(missingNumber(arr))









