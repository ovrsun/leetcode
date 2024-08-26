# https://leetcode.com/problems/baseball-game
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 1:
            return int(operations[0])
        record = [0] * len(operations)
        i = 0
        for op in operations:
            if op == 'C':
                i -= 1
                # ["1","D","D","D"]
                # 1, 2, 4, 8
            else:
                if op == '+':
                    record[i] = record[i-1] + record[i-2]
                elif op == 'D':
                    record[i] = record[i-1] * 2
                else:
                    record[i] = int(op)
                i += 1
        res = 0
        # print(record)
        while i > 0:
            i -= 1
            res += record[i]
        # print(res)
        return res


sln = Solution()
assert sln.calPoints(["5","2","C","D","+"]) == 30
assert sln.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert sln.calPoints(["1","C"]) == 0
assert sln.calPoints(["1"]) == 1
assert sln.calPoints(["1","D","D","D"]) == 15
