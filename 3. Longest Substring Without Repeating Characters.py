# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        current_string_chars = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in current_string_chars:
                max_len = max(max_len, len(current_string_chars))
                current_string_chars.remove(s[l])
                l += 1
            
            elif s[r] not in current_string_chars:
                current_string_chars.add(s[r])
                r += 1

        max_len = max(max_len, len(current_string_chars))
        return max_len


sln = Solution()
assert (res := sln.lengthOfLongestSubstring('abcabcbb')) == 3, res
assert (res := sln.lengthOfLongestSubstring('bbbbb')) == 1, res
assert (res := sln.lengthOfLongestSubstring('pwwkew')) == 3, res
assert (res := sln.lengthOfLongestSubstring('')) == 0, res
assert (res := sln.lengthOfLongestSubstring("dvdf")) == 3, res
