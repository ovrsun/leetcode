# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        num = (low + high) // 2
        attempt = guess(num)

        while attempt != 0:
            if attempt == -1:
                high = num
            else:
                low = num + 1
            num = (low + high) // 2
            attempt = guess(num)

        return num
