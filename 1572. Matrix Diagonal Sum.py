# https://leetcode.com/problems/matrix-diagonal-sum
from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        primary = 0
        secondary = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    primary += mat[i][j]
                if j == n-1-i:
                    secondary += mat[i][n-1-i]
        if n % 2:
            secondary -= mat[n//2][n//2]
        return primary + secondary


sln = Solution()
assert sln.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25
assert sln.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8
assert sln.diagonalSum([[5]]) == 5
assert sln.diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]) == 55
