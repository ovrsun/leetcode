# https://leetcode.com/problems/remove-element/description/

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
    
def remove_element(nums, val):
    left = 0
    right = len(nums) - 1
    # 3 2 2 3
    # left=0 right=3

    count = 0
    for num in nums:
        if num != val:
            count += 1

    while left < right:
        if nums[left] == val:
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right -= 1
        else:
            left += 1
    return count

assert remove_element([asdasd]) == 2

assert remove_element([3,2,2,3], 3) == 2
assert remove_element([0,1,2,2,3,0,4,2], 2) == 5
assert remove_element([1], 1) == 0
assert remove_element([1], 0) == 1
assert remove_element([1, 1], 1) == 0
