# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        # res = set()
        res = []
        nums.sort()
        for a in range(n-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n-1):
                if b - 1 != a and nums[b] == nums[b-1]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    current_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if current_sum == target:
                        # res.add((nums[a], nums[b], nums[c], nums[d]))
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                    if current_sum < target:
                        c += 1
                    else:
                        d -= 1
        return res



sln = Solution()
assert (res := sln.fourSum([1,0,-1,0,-2,2], 0)) == {(-2,-1,1,2),(-2,0,0,2),(-1,0,0,1)}, res
assert (res := sln.fourSum([2,2,2,2,2], 8)) == {(2,2,2,2)}, res

print('end')