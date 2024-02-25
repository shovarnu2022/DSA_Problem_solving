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
"""










