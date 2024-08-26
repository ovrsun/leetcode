# https://leetcode.com/problems/merge-strings-alternately

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        res = [0] * (n + m)

        i, j = 0, 0
        while i < n and i < m:
            res[j] = word1[i]
            res[j+1] = word2[i]
            j += 2
            i += 1
        
        if n < m:
            while i < m:
                res[j] = word2[i]
                j += 1
                i += 1
        else:
            while i < n:
                res[j] = word1[i]
                j += 1
                i += 1
        return ''.join(res)



        

sln = Solution()
assert sln.mergeAlternately('abc', 'pqr') == 'apbqcr'
assert sln.mergeAlternately('ab', 'pqr') == 'apbqr'
assert sln.mergeAlternately('a', 'pqr') == 'apqr'
assert sln.mergeAlternately('abc', 'p') == 'apbc'
assert sln.mergeAlternately('a', '') == 'a'
assert sln.mergeAlternately('', 'p') == 'p'
assert sln.mergeAlternately('', '') == ''

