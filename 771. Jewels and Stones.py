# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_set = set(jewels)
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count


sln = Solution()
assert (res := sln.numJewelsInStones('aA', 'aAAbbbb')) == 3, res
assert (res := sln.numJewelsInStones('z', 'ZZ')) == 0, res
