# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        factors = []
        num = n
        i = 2
        while num > 1:
            if num % i == 0:
                num //= i
                factors.append(i)
            else:
                i += 1

        return sum(factors)


sln = Solution()
assert (res := sln.minSteps(1)) == 0
assert (res := sln.minSteps(2)) == 2
assert (res := sln.minSteps(3)) == 3
assert (res := sln.minSteps(4)) == 4
assert (res := sln.minSteps(5)) == 5
assert (res := sln.minSteps(6)) == 5
assert (res := sln.minSteps(8)) == 6, res
assert (res := sln.minSteps(9)) == 6
assert (res := sln.minSteps(11)) == 11
assert (res := sln.minSteps(13)) == 13

# # A A A A A A A A A A A A A A A A 

# A A A A A A A A 