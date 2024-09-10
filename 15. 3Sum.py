# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums) - 1
        triplets = []
        nums.sort()

        for i in range(n - 1):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1

        return triplets


sln = Solution()
assert (res := sln.threeSum([-1,0,1,2,-1,-4])) == [[-1,-1,2],[-1,0,1]], res
assert (res := sln.threeSum([0,0,0,0])) == [[0,0,0]], res
