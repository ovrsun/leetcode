# https://leetcode.com/problems/spiral-matrix-iii/description/

class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        res = [[rStart, cStart]]
        if cols == rows == 1:
            return res

        def inside(r, c):
            return 0 <= r < rows and 0 <= c < cols

        k = max([rows - rStart, rStart - 0, cols - cStart, cStart - 0]) * 2
        print(k)
        r = rStart
        c = cStart
        for i in range(0, k+1, 2):
            border = c
            while c < border + i + 1:
                c += 1
                if inside(r, c):
                    res.append([r, c])
            border = r
            while r < border + i + 1:
                r += 1
                if inside(r, c):
                    res.append([r, c])
            border = c
            while c > border - i - 2:
                c -= 1
                if inside(r, c):
                    res.append([r, c])
            border = r
            while r > border - i - 2:
                r -= 1
                if inside(r, c):
                    res.append([r, c])
            
        return res


sln = Solution()

print(sln.spiralMatrixIII(5, 6, 1, 4))
