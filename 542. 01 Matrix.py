# https://leetcode.com/problems/01-matrix/description/

class Solution:
    def updateMatrix(self, arr: list[list[int]]) -> list[list[int]]:
        n = len(arr)
        m = len(arr[0])
        queue = []
        for r in range(n):
            for c in range(m):
                if arr[r][c] == 0:
                    queue.append([r, c])
                else:
                    arr[r][c] = -1

        while queue:
            directions = [
                [0, 1],
                [1, 0],
                [0, -1],
                [-1, 0],
            ]
            r, c = queue.pop(0)
            for direction in directions:
                nr, nc = r + direction[0], c + direction[1]
                if not 0 <= nr < n or not 0 <= nc < m or arr[nr][nc] != -1:
                    continue
                arr[nr][nc] = arr[r][c] + 1
                queue.append([nr, nc])

        return arr


arr = [
    [0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
]
sln = Solution()
# sln.updateMatrix(arr)
# assert sln.updateMatrix(arr) == [[0,0,0],[0,1,0],[0,0,0]]
# assert (res := sln.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) == [[0,0,0],[0,1,0],[1,2,1]], res
# assert (res := sln.updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]])) == [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]], res
# assert (res := sln.updateMatrix([[0],[0],[0],[0],[0]])) == [[0,0,0],[0,1,0],[1,2,1]], res
assert (res := sln.updateMatrix(arr)) == [[0, 1, 1, 1, 0], [1, 1, 0, 1, 1], [2, 2, 1, 1, 0]], res

# print('end')
