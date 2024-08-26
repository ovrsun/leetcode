# https://leetcode.com/problems/plus-one/description
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry:
            if carry and digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
            i -= 1
        if digits[0] == 0:
            new_digits = [1] * (len(digits) + 1)
            for i in range(len(digits)):
                new_digits[i+1] = digits[i]
            return new_digits
        return digits
            


sln = Solution()
assert sln.plusOne([1, 2, 4]) == [1, 2, 5]
assert sln.plusOne([0]) == [1]
assert sln.plusOne([9]) == [1, 0]
assert sln.plusOne([8]) == [9]
assert sln.plusOne([1, 0]) == [1, 1]
