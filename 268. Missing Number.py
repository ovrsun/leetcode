# https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (1 + n) * n / 2 - sum(nums)


sln = Solution()
assert (res := sln.missingNumber([3, 0, 1])) == 2
print(res)
assert sln.missingNumber([0, 1]) == 2
assert sln.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
