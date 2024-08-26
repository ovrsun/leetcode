# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        numbers_count = high - low + 1
        odd_count = (numbers_count - high % 2 - low % 2) // 2 + high % 2 + low % 2
        return odd_count


sln = Solution()
assert sln.countOdds(3, 7) == 3     # 3, 5, 7
assert sln.countOdds(8, 10) == 1    # 9
assert sln.countOdds(0, 1) == 1     # 1
assert sln.countOdds(11, 11) == 1   # 11
assert sln.countOdds(4, 4) == 0     # nothing
assert sln.countOdds(4, 8) == 2     # 5, 7

# numbers_count = high - low + 1
# 8 - 4 + 1 = 5 | 5 7  5 // 2 = 2, 8 % 2 | 4 % 2
# # 7 - 3 + 1 = 5 |      5 // 2 
# 3 4 5 6 7
# 3 4 5 6 7 8 | 6 