# https://leetcode.com/problems/implement-stack-using-queues/description/

# [10
# [1 2 3 4 5 6 7 8 9


class MyStack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1.append(x)

    def pop(self) -> int:
        res = self.q1.pop()
        while self.q2:
            self.q1.append(self.q2.pop(0))
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        return self.q1[0]

    def empty(self) -> bool:
        return not (len(self.q1) + len(self.q2))

# ["MyStack","push","push","push","top","pop","top","pop","top","empty","pop","empty"]


ms = MyStack()
ms.push(1)
ms.push(2)
ms.push(3)
assert ms.top() == 3
assert ms.pop() == 3
assert ms.top() == 2
assert ms.pop() == 2
assert ms.top() == 1
assert ms.empty() is False
assert ms.pop() == 1
assert ms.empty() is True
