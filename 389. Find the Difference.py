# https://leetcode.com/problems/find-the-difference

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 1
        # return (set(t) - set(s)).pop()
        
        # 2
        sum_s = sum(ord(c) for c in s)
        sum_t = sum(ord(c) for c in t)
        return chr(sum_t-sum_s)
    
        # 3
        # we can use hashmap to count chars
        # then iterate over values and return
        # key, which value equals 1


sln = Solution()
assert sln.findTheDifference('abcd', 'abcde') == 'e'
assert sln.findTheDifference('', 'a') == 'a'
