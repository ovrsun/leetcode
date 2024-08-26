# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):
    def topKFrequent(self, nums, k):
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        counts = {}
        for key, value in hm.items():
            counts.setdefault(value, []).append(key)

        frq_arr = [0] * len(counts)
        i = len(nums) - 1
        j = 0
        while i > 0:
            if i in counts:
                t = len(counts[i]) + j
                while j < t:
                    frq_arr[j] = counts[i][t-j-1]
                    j += 1
            i -= 1
        return frq_arr[:k]


sln = Solution()
assert (res := set(sln.topKFrequent([1, 1, 1, 2, 2, 3], 2))) == set([1, 2]), res
# assert (res := set(sln.topKFrequent([1, 2], 2))) == set([1, 2]), res
assert (res := set(sln.topKFrequent([1], 1))) == set([1]), res
