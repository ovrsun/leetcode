class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hms = {}
        hmt = {}

        for i in range(len(s)):
            hms[s[i]] = t[i]
            hmt[t[i]] = s[i]

        if len(hms) != len(hmt):
            return False

        for si, ti in zip(hms, hmt):
            if hms[si] != ti or hmt[ti] != si:
                return False

        return True

# a:a     a:a
# b:b     b:b
# c:a     

sln = Solution()
assert sln.isIsomorphic('badc', 'baba') is False
assert sln.isIsomorphic('abca', 'abaa') is False
