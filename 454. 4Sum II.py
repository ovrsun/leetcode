# https://leetcode.com/problems/4sum-ii/

from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hm = defaultdict(int)
        for n3 in nums3:
            for n4 in nums4:
                hm[n3+n4] += 1
        count = 0
        for n1 in nums1:
            for n2 in nums2:
                if -(n1+n2) in hm:
                    count += hm[-(n1+n2)]
        return count


sln = Solution()
assert (res := sln.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])) == 2, res
assert (res := sln.fourSumCount([0], [0], [0], [0])) == 1, res
