# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List

class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        # a = [1, 1, 2]
        i = 0
        while i < len(a) - 1 and a[i] < a[-1]:
            # i=0 j=1
            j = i + 1
            while a[i] >= a[j]:
                j += 1
            a[i+1] = a[j]
            i += 1
        print(i+1, a)
        return i + 1


sln = Solution()
assert sln.removeDuplicates([1,1,2]) == 2
assert sln.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
assert sln.removeDuplicates([1,2,3]) == 3
assert sln.removeDuplicates([1]) == 1
assert sln.removeDuplicates([2, 4, 4]) == 2


# 1 с вложенным циклом =\
# class Solution:
#     def removeDuplicates(self, a: List[int]) -> int:
#         # a = [1, 1, 2]
#         i = 0
#         while i < len(a) - 1 and a[i] < a[-1]:
#             # i=0 j=1
#             j = i + 1
#             while a[i] >= a[j]:
#                 j += 1
#             a[i+1] = a[j]
#             i += 1
#         print(i+1, a)
#         return i + 1

        







