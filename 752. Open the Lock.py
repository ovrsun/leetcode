# https://leetcode.com/problems/open-the-lock/description/

class Solution:
    def add_all_moves(self, current: list, step: int):
        res = [
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
            [current.copy(), step],
        ]
        for i in range(4):
            res[i*2][0][i] = (res[i*2][0][i] + 1) % 10
            res[i*2+1][0][i] = (res[i*2+1][0][i] - 1) % 10
        return res

    def openLock(self, deadends: list[str], target: str) -> int:
        t = [int(i) for i in target]
        source = [0, 0, 0, 0]
        queue = [[source, 0]]
        seen = set()
        while queue:
            current, step = queue.pop(0)
            if tuple(current) not in seen and ''.join((str(i) for i in current)) not in deadends:
                seen.add(tuple(current))
                if current == t:
                    return step
                new = self.add_all_moves(current, step+1)
                queue.extend(new)
        return -1

deadends = ["0201","0101","0102","1212","2002"]
sln = Solution()
assert sln.openLock(deadends, '0202') == 6


# def add_all_moves(current: list, step: int):
#     res = [
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#         [current.copy(), step],
#     ]
#     for i in range(4):
#         res[i*2][0][i] = (res[i*2][0][i] + 1) % 10
#         res[i*2+1][0][i] = (res[i*2+1][0][i] - 1) % 10
#     return res


# def search(t):
    # target = [int(i) for i in t]
    # print(target)
    # deadends = ["0201", "0101", "0102", "1212", "2002"]
    # source = [0, 0, 0, 0]
    # queue = [[source, 0]]
    # seen = set()
    # while queue:
    #     current, step = queue.pop(0)
    #     if tuple(current) not in seen and ''.join((str(i) for i in current)) not in deadends:
    #         seen.add(tuple(current))
    #         # print(current, step)
    #         if current == target:
    #             return step
    #         new = add_all_moves(current, step+1)
    #         queue.extend(new)
    # return -1


# target = '0202'
# print(search(target))
# print('end')

# 00
# 90
# 80
# 70
# 60
# 50
# 40
# 30

# 00
# 01
# 11
# 21
# 31
# 30