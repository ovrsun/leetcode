# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hm1 = {}
        for c in nums1:
            hm1[c] = hm1.get(c, 0) + 1
        
        hm2 = {}
        for c in nums2:
            hm2[c] = hm2.get(c, 0) + 1

        res = []

        for k in hm1:
            if k in hm2:
                res.extend([k for _ in range(min(hm1[k], hm2[k]))])

        return res


sln = Solution()
assert (res := sln.intersect([1, 2, 2, 1], [2, 2])) == [2, 2]
