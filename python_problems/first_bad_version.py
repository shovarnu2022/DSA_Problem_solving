"""
You have N versions of a software, we want to
find the first "bad" version of the software

How to determine a bad version?

We will be given a method called "isBadVersion" by default,
it returns a boolean,true if the version you pass to it is bad,
false otherwise

Important Note:
if a version is bad, all versions after it are bad

Step 1: Can our input be "0", meaning that we have no versions of
our software?

No, our input N, will represent versions starting from
[1...N] and we'll never have N be 0

Step 2: isBadVersion(n) {  Input: 5
return n >= 3
}

if this is how the isBadVersion looks like, the first
bad version would be 3, so we should return 3


Step 3:

We know that we can determine if a version is bad or
not using our given "isBadVersion" method

All version after the first bad version will also be bad

How about we do a linear seach, we go over the versions one by one,
and we return the first version that we see is bad.

isBadVersion(num){
    return num>=3
}

solution(n){
    for i in range[1:n]{ O(n)
        if isBadVersion(i) == true
            return i
    }
}


Space Complexity: O(1)

Step 5 : Optimal solution

What we know:
> We know that we can determine if a version is bad or not
using our given "isBadVersion" method

> All version after the first bad version will also be bad

At this point, we know for a fact that all element after
current position version(5) are bad, so we can just
ignore all version after that

Now we have a search span of versions from 1-5, each of them
have an equal chance of being the first version
we'll go to the middle of the span so that we can keep cutting the
search span in half

Pseaudocode:

isBadVersion(num) {
    return num >= 3
}

solution(n){
    L = 1
    R = n
    while L < R:
        mid = (L+R)/2
        if isBadVersion(mid):
            R = mid
        else:
            L = mid + 1
    return L
}
"""


def isBadVersion(num):
    ...


def firs_bad_version(n):
    left = 1
    right = n + 1
    while left < right:
        mid = (left+right)//2
        if isBadVersion(mid):
            if mid == 1 or (mid-1 > 0 and not isBadVersion(mid-1)):
                return mid
            else:
                right = mid
        else:
            left = mid + 1
    return left









