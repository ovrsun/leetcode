# https://leetcode.com/problems/set-matrix-zeroes
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        vertical = set()
        horizontal = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    vertical.add(i)
                    horizontal.add(j)
        print(horizontal)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in vertical or j in horizontal:
                    matrix[i][j] = '0'

        print(vertical, horizontal)
        print(matrix)

sln = Solution()
sln.setZeroes([[1,1,1],[1,0,1],[1,1,1]])