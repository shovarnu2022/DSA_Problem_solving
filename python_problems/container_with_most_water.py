"""
Given n non-negative integers where each integer represent the
height of a vertical line on a chart

Find two lines, which together with x-axis
forms a container, that holds the biggest amount of water.
return the area of that water.

height: 1, 8, 6, 2, 5, 4, 8, 3, 7

step 1: constraint question 1
Do we need to consider the thickness of the lines
in our calculations? No, the lines only in terms of height

Do lines inside.of. our container affect the area?

No, when calculating the area, ignore all the lines between
the walls of our container


Step 2: Test cases

Heights: 5, 3, 2, 1, 4

Why would 5 and 4 would be considered
These 2 are the greatest values in our array, and they
are the furthest apart

area = length * width
area = min(5,4) * (4-0) = 4*4 = 16

heights: []
area = 0

heights = [4]
area = 0

heights = [5, 9, 2, 1, 4]

possibilities are 5, 4 and 9, 4

area = length * width
area = min(5, 4) * (4-0)
area = 4 * 4 = 16

area = min(9, 4) * (4 - 1)
area = 4 * 3 = 12

Step 3: Brute force intuition

heights: 5, 9, 2, 1, 4
We want to find 2 positions that would maximize our area
How about we search every possible area
"""


def maxArea(height: list[int]) -> int:
    maxarea = 0
    l = 0
    r = len(height) - 1
    while l < r:
        calculate_area = min(height[l], height[r])*(r-l)
        maxarea = max(maxarea, calculate_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxarea


height_arr = [5, 9, 2, 1, 4]
print(maxArea(height_arr))
