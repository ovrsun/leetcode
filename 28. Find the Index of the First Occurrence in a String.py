# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 1
        # i = 0
        # n = len(needle)
        # while i < len(haystack):
        #     if haystack[i:i+n] == needle:
        #         return i
        #     i += 1
        # return -1

        # 2
        
        n = len(needle)

        # m     i s s i ssippi
        #       i s s i p

        i = 0
        j = 0
        n = len(needle)

        while i < len(haystack):
            while haystack[i] == needle[j]:
                j += 1
                i += 1
                if j == n:
                    return i - j
                if i >= len(haystack):
                    return -1
            i = i - j + 1
            j = 0
        return -1




sln = Solution()
assert sln.strStr('sadbutsad', 'sad') == 0
assert sln.strStr('sadbutsad', 'a') == 1
assert sln.strStr('leetcode', 'leeto') == -1
assert sln.strStr('leet', 'leetcode') == -1
assert sln.strStr('hello', 'll') == 2
assert sln.strStr('a', 'a') == 0
assert (res := sln.strStr('mississippi', 'issip')) == 4, res
assert (res := sln.strStr('issi', 'issip')) == -1, res


