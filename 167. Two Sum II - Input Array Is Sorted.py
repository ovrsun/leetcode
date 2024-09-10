class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                # break
                return [left+1, right+1]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        # return [left+1, right+1]


sln = Solution()
assert (res := sln.twoSum([2,7,11,15], 9)) == [1, 2], res
assert (res := sln.twoSum([2,3,4], 6)) == [1, 3], res
assert (res := sln.twoSum([-1,0], -1)) == [1, 2], res
assert (res := sln.twoSum([0,0], 0)) == [1, 2], res
