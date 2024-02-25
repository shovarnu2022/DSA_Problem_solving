"""
Given an array of integers, return true if the
following conditions are fulfilled

> Length of the array is bigger than or equal to 3
> There exists some index i such that:

a[0] < a[1] < .... < a[i]
a[i] > a[i+1] > .... > a[a.size-1]

in nutshell: Find if there is an increasing subarray followed
by a decreasing subarray

Example:
array: 3, 5, 5

O/p: False

array: 0, 3, 2, 1

o/p: true


What should we return in case we only have 1 element in the array?

In that case, return false


Since we need a strictly increasing sequence followed by a strictly decreasing
sequence, should we return False if the input size is 2?

Yes, you need atleast 3 elements for a chance of
returning true, if you receive an array of size less than 3,
return false


How would we check for an increasing subsequence?

> We can do it in a loop and at each iteration, we check to
see if the current element is bigger than the previous element

> If the above condition fails, we break from the loop

What do we need to keep track of?

> Where the increasing subsequence ends

> Why do we need to keep track of it?

To know there to start checking for a decreased sequence

> How do we keep track of it?

the pointer used to loop over our array while we're checking
for the increasing subsequence needs to be saved

> When would we return false before even checking for a
decreasing subsequence?

if we didn't move from our location (meaning that there
wasn't ANY increasing subsequence)

if we already reached the end of the array

**Implementation**

Steps

> Loop over array starting from loop index as long as it's
increasing

i=1
while i< len(A) and A[i] > A[i-1]:
    i+=1
if i == 1 or i == len(A):
   return False
while i < len(A) and A[i] < A[i-1]:
   i+=1
return i == len(A)


"""


class Solution:
    def validMountainArray(self, A: list[int]) -> bool:
        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i = i + 1
        if i == 1 or i == len(A):
            return False

        while i < len(A) and A[i] < A[i-1]:
            i += 1

        return i == len(A)




















