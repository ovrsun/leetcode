# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums): 
            if nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                # nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                continue
            i += 1

        res = []
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                res.append(i+1)
            i += 1
        return res
        
        
sln = Solution()
assert sln.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]