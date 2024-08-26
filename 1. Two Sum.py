# https://leetcode.com/problems/two-sum/description/

def two_sum(nums, target):
    diffs = {}
    for i in range(len(nums)):
        if nums[i] in diffs:
            return [diffs[nums[i]], i]
        
        diffs[target - nums[i]] = i


assert (res := two_sum([1, 2], 3)) == [0, 1], res
assert (res := two_sum([2, 15, 11, 7], 9)) == [0, 3], res
