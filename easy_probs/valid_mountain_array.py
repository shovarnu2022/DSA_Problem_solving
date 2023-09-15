# find increasing subarray followed by decreasing subarray
# example: 355 is not increasing subarray, 0321 is an increasing subarray
# min length fill always be 1

"""
you need atleast 3 elements for a chance of returning true, 
if you receive an array of size less than 3, then return false
"""


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 1
        while(i < len(A) and A[i] > A[i-1]):
            i+=1
        if(i == 1 or i == len(A)):
            return False
        while(i < len(A) and A[i] < A[i-1]):
            i += 1
        
        return i==len(A)


