class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        num = x
        y = 0
        while num > 0:
            y = y * 10 + num % 10
            num //= 10
        return x == y


# can improve it reversing just half of x
# when original and cutted x becomes less
# then reversed x it's time to compare

# sln = Solution()
# assert sln.isPalindrome(121) is True
# assert sln.isPalindrome(-121) is False
# assert sln.isPalindrome(10) is False
# assert sln.isPalindrome(0) is True
