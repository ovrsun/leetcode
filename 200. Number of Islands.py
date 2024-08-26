# https://leetcode.com/submissions/detail/1328367281/
# read this and try to understand:
# https://leetcode.com/problems/number-of-islands/solutions/56349/7-lines-python-14-lines-java
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen:
                    seen.add((i, j))
                    if grid[i][j] == '1':
                        queue = [(i, j)]
                        while len(queue):
                            x, y = queue.pop(0)
                            if x - 1 >= 0 and (x-1, y) not in seen:
                                seen.add((x-1, y))
                                if grid[x-1][y] == '1':
                                    queue.append((x-1, y))
                            if y + 1 < n and (x, y+1) not in seen:
                                seen.add((x, y+1))
                                if grid[x][y+1] == '1':
                                    queue.append((x, y+1))
                            if x + 1 < m and (x+1, y) not in seen:
                                seen.add((x+1, y))
                                if grid[x+1][y] == '1':
                                    queue.append((x+1, y))
                            if y - 1 >= 0 and (x, y-1) not in seen:
                                seen.add((x, y-1))
                                if grid[x][y-1] == '1':
                                    queue.append((x, y-1))
                        islands += 1
        return islands
