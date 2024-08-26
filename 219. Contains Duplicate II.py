class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_at = {}
        for i in range(len(nums)):
            if seen_at.get(nums[i]) is not None and abs(seen_at[nums[i]] - i) <= k:
                return True
            seen_at[nums[i]] = i

        return False


# [1,2,3,1], k = 3
sln = Solution()
assert sln.containsNearbyDuplicate([1,2,3,1], 3) is True
assert sln.containsNearbyDuplicate([1,0,1,1], 1) is True
assert sln.containsNearbyDuplicate([1,2,3,1,2,3], 2) is False
assert sln.containsNearbyDuplicate([1], 3) is False
assert sln.containsNearbyDuplicate([1,0,1,1], 0) is False
