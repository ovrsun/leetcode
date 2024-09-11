# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freq = defaultdict(int)
        
        for num in nums:
            num_freq[num] += 1

        freq_nums = defaultdict(list)
        for num, freq in num_freq.items():
            freq_nums[freq].append(num)
            
        max_freq = 0
        for freq in freq_nums.keys():
            max_freq = max(freq, max_freq)
        
        res = []
        fr = max_freq
        while len(res) < k and fr > 0:
            res.extend(freq_nums[fr])
            fr -= 1

        return res


# sln = Solution()
# assert (res := set(sln.topKFrequent([1, 1, 1, 2, 2, 3], 2))) == set([1, 2]), res
# assert (res := set(sln.topKFrequent([1, 2], 2))) == set([1, 2]), res
# assert (res := set(sln.topKFrequent([1], 1))) == set([1]), res
