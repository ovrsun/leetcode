# https://leetcode.com/problems/maximum-distance-in-arrays/


# II
class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        l_min = arrays[0][0]
        l_max = arrays[0][-1]
        max_diff = max(abs(l_max - arrays[1][0]), abs(arrays[1][-1] - l_min))
        for i in range(1, len(arrays)):
            max_diff = max(abs(l_max - arrays[i][0]), abs(arrays[i][-1] - l_min), max_diff)
            l_min = min(l_min, arrays[i][0])
            l_max = max(l_max, arrays[i][-1])

        return max_diff


sln = Solution()
assert (res := sln.maxDistance([[1,2,3],[4,5],[1,2,3]])) == 4, res
assert (res := sln.maxDistance([[1],[1]])) == 0, res
assert (res := sln.maxDistance([[-31,2,600], [4,5],[1,2,3]])) == 599, res
assert (res := sln.maxDistance([[4,5],[1,2,3], [-31,2,600]])) == 599, res
assert (res := sln.maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]])) == 14, res

print('end')


# I
# class Solution:
#     def maxDistance(self, arrays: list[list[int]]) -> int:
#         mins = [arr[0] for arr in arrays]
#         maxs = [arr[-1] for arr in arrays]
#         minimum = self._get_min_with_index(mins)
#         maximum = self._get_max_with_index(maxs)
#         if minimum[1] != maximum[1]:
#             return abs(maximum[0] - minimum[0])

#         second_min = self._get_min_with_index(mins, minimum[1])
#         second_max = self._get_max_with_index(maxs, maximum[1])
#         # print(minimum, maximum)
#         # print(second_min, second_max)

#         return max(abs(maximum[0] - second_min[0]), abs(second_max[0] - minimum[0]))

#     def _get_min_with_index(self, array: list[int], exclude=-1) -> tuple[int, int]:
#         return min([(array[i], i) for i in range(len(array)) if i != exclude], key=lambda x: x[0])

#     def _get_max_with_index(self, array: list[int], exclude=-1) -> tuple[int, int]:
#         return max([(array[i], i) for i in range(len(array)) if i != exclude], key=lambda x: x[0])


# sln = Solution()
# assert (res := sln.maxDistance([[1,2,3],[4,5],[1,2,3]])) == 4, res
# assert (res := sln.maxDistance([[1],[1]])) == 0, res
# assert (res := sln.maxDistance([[-31,2,600],[4,5],[1,2,3]])) == 599, res

# # [-31, | 1, 4]
# # [600, | 5, 3]

  
