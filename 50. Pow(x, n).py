class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x == 1:
            # return x
        # if x == -1:
            # return -1 if n % 2 else 1
        if n == 0:
            return 1
        if n < 0 and x != 0:
            n = abs(n)
            x = 1 / x

        if n % 2 == 1:
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)

        # arr = []
        # i = 0
        # while n != 1:
        #     x *= x
        #     n //= 2 + i
        #     i += 1
        # else 
        # return x
        # if 0 < x <= 0.5 and n > 1000:
            # return 0
        # if n == 1:
            # return x
        # i = 0
        # res = 1
        # while i < n:
        #     res *= x
        #     i += 1
        # k = n//2 + n%2

        # return self.myPow(x, k) * self.myPow(x, n-k)


        return res


sln = Solution()
assert (res := sln.myPow(2, 10)) == 1024, res
# assert (res := sln.myPow(2, -2)) == 0.25, res
# assert (res := sln.myPow(0.00001, 2147483647)) == 0.25, res
assert (res := sln.myPow(1.0000000000001, -2147483648)) == 0.25, res
