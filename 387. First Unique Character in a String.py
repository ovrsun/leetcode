# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# I. Using hash table
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hm = {}
#         for i in range(len(s)):
#             hm[s[i]] = hm.get(s[i], 0) + 1

#         for i in range(len(s)):
#             if hm[s[i]] == 1:
#                 return i
#         return -1

# II. Using fixed array instead of hash table
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1

        for i in range(len(s)):
            if counts[ord(s[i]) - ord('a')] == 1:
                return i
        return -1


sln = Solution()
assert (res := sln.firstUniqChar('leetcode')) == 0, res
assert (res := sln.firstUniqChar('loveleetcode')) == 2, res
assert (res := sln.firstUniqChar('aabb')) == -1, res
assert (res := sln.firstUniqChar('a')) == 0, res
assert (res := sln.firstUniqChar('aaaa')) == -1, res
