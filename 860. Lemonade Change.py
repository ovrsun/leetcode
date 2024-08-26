# https://leetcode.com/problems/lemonade-change/
from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {
            5: 0,
            10: 0,
            20: 0,
        }

        for bill in bills:
            if bill == 5:
                cash[5] += 1
            elif bill == 10:
                if not cash[5]:
                    return False
                cash[10] += 1
                cash[5] -= 1
            else:
                if cash[5]:
                    if cash[10]:
                        cash[5] -= 1
                        cash[10] -= 1
                    elif cash[5] >= 3:
                        cash[5] -= 3
                    else:
                        return False
                else:
                    return False
        return True



sln = Solution()
# assert sln.lemonadeChange([5,5,10,10,20]) is False
assert sln.lemonadeChange([5,5,5,10,5,5,10,20,20,20]) is False
