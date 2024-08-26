# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


assert contains_duplicate([1,2,3,1]) is True
assert contains_duplicate([1,2,3]) is False
assert (res := contains_duplicate([0])) is False, res
