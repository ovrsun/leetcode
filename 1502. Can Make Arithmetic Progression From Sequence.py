# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        counts = {}
        mini = min(arr)
        maxi = max(arr)
        d = (maxi - mini) // (len(arr) - 1)
        for num in arr:
            if num in counts and d:
                return False
            counts[num] = 1
        num = mini
        while num != maxi:
            if num not in counts:
                return False
            num += d
        return True



sln = Solution()
# assert sln.canMakeArithmeticProgression([3,5,1]) is True
# assert sln.canMakeArithmeticProgression([1,2,4]) is False
# assert sln.canMakeArithmeticProgression([2,10,7,8,3]) is False
# assert sln.canMakeArithmeticProgression([1,2]) is True
assert sln.canMakeArithmeticProgression([0,0,0,0]) is True  # WTF?

# можно не множества, а словарь использовать. и там на первом проходе dict[key] +1 делать, а потом -1
