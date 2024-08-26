# # # new
# # # https://leetcode.com/problems/sqrtx/
# # class Solution:
# #     def mySqrt(self, x: int) -> int:
# #         i = 0
# #         while i * i <= x:
# #             if i * i == x:
# #                 return i
# #             i += 1
# #         return i - 1

# # sln = Solution()
# # assert (res := sln.mySqrt(4)) == 2, res
# # assert (res := sln.mySqrt(8)) == 2, res

# from typing import List


# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         # [1,2,2]


#         res = [nums[0]] * 3

#         i = 1
#         while i < len(nums) - 1:
#             if res[2] < nums[i]:
#                 res[2], res[1], res[0] = nums[i], res[2], res[1]
#             if res[1] < nums[i] < res[2]:
#                 res[1], res[0] = nums[i], res[1]
#             if res[0] < nums[i] < res[1]:
#                 res[0] = nums[i]
#             i += 1    
        
#         if res[0] != res[1] != res[2]:
#             return res[0]
#         else:
#             return res[2]
        

# sln = Solution()
# print(sln.thirdMax([3,2,1]))
