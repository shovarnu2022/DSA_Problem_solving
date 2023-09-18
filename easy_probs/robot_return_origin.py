"""
Imagine a robot standing at postion(0,0)
in a 2D grid, given a string consisting of its moves,
find the final location of the robot

Example: UD
Current Position: (0,0)
U => (0, 0+1)
D => (0, 1-1)

U: up, Increase in y axis
D: down, Decrease in y axis
R: right, Increase in x axis
L: Left, Decrease in x axis
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for move in moves:
            if move == "U":
                y += 1
            elif move == "R":
                x += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
        return x == 0 and y == 0

s= Solution()
answer = s.judgeCircle("URRDLL")









