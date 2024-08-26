# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) == 1:
            return False
        horizontal = 0
        vertical = 0
        for move in moves:
            if move == 'L':
                horizontal += 1
            elif move == 'R':
                horizontal -= 1
            elif move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
        return horizontal == 0 and vertical == 0


sln = Solution()
assert sln.judgeCircle("UD") is True
assert sln.judgeCircle("LL") is False
assert sln.judgeCircle("LLDDUURR") is True
assert sln.judgeCircle('U') is False
