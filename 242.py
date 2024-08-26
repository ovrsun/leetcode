class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hm_s = {}
        hm_t = {}

        for pair in zip(s, t):
            hm_s[pair[0]] = hm_s.get(pair[0], 0) + 1
            hm_t[pair[1]] = hm_t.get(pair[1], 0) + 1

        return hm_s == hm_t


