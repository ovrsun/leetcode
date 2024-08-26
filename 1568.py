import copy

grid1 = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]
grid2 = [
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1]
]


class Solution:
    def minDays(self, grid):
        # days = 0
        copied = copy.deepcopy(grid)
        islands_count = self.count_islands(copied)
        if islands_count != 1:
            return 0

        # days += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                copied = copy.deepcopy(grid)
                copied[i][j] = 0
                islands_count = self.count_islands(copied)
                if islands_count != 1:
                    return 1

        return 2

    def count_islands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        if i >= 1:
            self.dfs(grid, i-1, j)
        if i < len(grid) - 1:
            self.dfs(grid, i+1, j)
        if j >= 1:
            self.dfs(grid, i, j-1)
        if j < len(grid[0]) - 1:
            self.dfs(grid, i, j+1)


sln = Solution()
assert (res := sln.minDays(grid1)) == 2, res
assert (res := sln.minDays(grid2)) == 1, res
