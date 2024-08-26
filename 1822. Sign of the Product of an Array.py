# https://leetcode.com/problems/sign-of-the-product-of-an-array
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for num in nums:
            if num < 0:
                negatives += 1
            if num == 0:
                return 0
        return -1 if negatives % 2 else 1


sln = Solution()
assert sln.arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
assert sln.arraySign([-1, 1]) == -1
assert sln.arraySign([-1, 0, 1]) == 0
assert sln.arraySign([-1, 0, 1]) == 0
