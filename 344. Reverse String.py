# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # also we can do it using two pointers:
        # while l < r etc
        # h e l l o s
        # o l l e h
        n = len(s)
        for i in range(n // 2):
            s[i], s[n-i-1] = s[n-i-1], s[i]


# sln = Solution()
#assert (res := sln.reverseString(["h","e","l","l","o"])) == ["o","l","l","e","h"], res
#assert (res := sln.reverseString(["H","a","n","n","a","h"])) == ["h","a","n","n","a","H"], res
#assert (res := sln.reverseString(["H","a","n","n","a","h"])) == ["h","a","n","n","a","H"], res
#assert (res := sln.reverseString(["H"])) == ["H"], res

# assert (res := sln.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"])) == ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"], res
