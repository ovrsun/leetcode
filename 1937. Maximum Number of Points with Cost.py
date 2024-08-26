# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        previous_row = points[0]

        if rows == 1:
            return max(previous_row)

        for row in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            current_row = [0] * cols
            left_max[0] = previous_row[0]
            right_max[-1] = previous_row[-1]

            for col in range(0, cols):
                left_max[col] = max(left_max[col-1] - 1, previous_row[col])

            for col in range(cols-2, -1, -1):
                right_max[col] = max(right_max[col+1] - 1, previous_row[col])

            for col in range(cols):
                current_row[col] = points[row][col] + max(left_max[col], right_max[col])

            previous_row = current_row

        return max(current_row)
    

sln = Solution()
print(sln.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
print(sln.maxPoints([[0]]))
