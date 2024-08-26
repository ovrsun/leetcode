# https://leetcode.com/problems/repeated-substring-pattern

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool

        """

----
# a = 'лииллиил'


a = 'abac'

print(len(a))
p = [0] * len(a)

j = 0
i = 1

while i < len(a):
    if a[j] == a[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

print(p)
length = len(a) - p[len(a) - 1]
print(length)
print(a[:length], 'vs', a[len(a) - length:])
if a[:length] == a[len(a) - length:] and p[-1] != 0:
    print(True)
else:
    print(False)

----




        n = len(s)
        i = 1
        j = 0
        while i < n:
            # abacababacab
            while s[i] == s[j]:
                print(s[i], s[j])
                i += 1
                j += 1
                if i == n:
                    if i % (i - j) == 0:
                        return True
                    else:
                        return False
            i += 1
            j = 0


        return False
# a b c a b c



# abckdaabck
# abckabck

sln = Solution()
# assert sln.repeatedSubstringPattern('abab') is True
# assert sln.repeatedSubstringPattern('aba') is False
# assert sln.repeatedSubstringPattern('abcabcabc') is True
# assert sln.repeatedSubstringPattern('abcdabcdabck') is False
# assert sln.repeatedSubstringPattern('a') is False
# assert sln.repeatedSubstringPattern('ac') is False
# assert sln.repeatedSubstringPattern('abckdaabck') is False
# assert sln.repeatedSubstringPattern('abckabck') is True
assert sln.repeatedSubstringPattern('abacababacab') is True
