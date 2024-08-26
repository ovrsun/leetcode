# https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sortedSquares(nums):
    n = len(nums)
    arr = [0] * n
    left, right = 0, n - 1

    i = n - 1
    while i >= 0:
        if abs(nums[left]) > abs(nums[right]):
            arr[i] = nums[left] ** 2
            left += 1
        else:
            arr[i] = nums[right] ** 2
            right -= 1
        i -= 1

    return arr


assert sortedSquares([]) == []
assert sortedSquares([-1]) == [1]
assert sortedSquares([-3, -2, -1]) == [1, 4, 9]
assert sortedSquares([1, 2, 3]) == [1, 4, 9]
assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
