# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        mask = 0
        for num in nums:
            mask ^= num
        return mask

sln = Solution()
print(sln.singleNumber([4, 1, 2, 1 ,2]))