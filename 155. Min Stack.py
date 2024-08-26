# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self) -> None:
        self.stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = val if not len(self.stack) else self.getMin()
        if current_min > val:
            current_min = val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


ms = MinStack()
assert ms.stack == []

ms.push(3)
assert ms.stack == [(3, 3)], ms.stack
assert ms.top() == 3
assert ms.getMin() == 3

ms.push(4)
assert ms.stack == [(3, 3), (4, 3)]
assert ms.top() == 4
assert ms.getMin() == 3

assert ms.stack == [(3, 3), (4, 3)]
ms.pop()
assert ms.stack == [(3, 3)], ms.stack
ms.pop()
assert ms.stack == []

print('====end====')

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
