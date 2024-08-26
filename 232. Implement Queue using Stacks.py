# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:
    def __init__(self):
        self.write = []
        self.read = []

    def push(self, x: int) -> None:
        self.write.append(x)

    def pop(self) -> int:
        if not len(self.read):
            self._move_elements()
        return self.read.pop()

    def peek(self) -> int:
        if not len(self.read):
            self._move_elements()
        return self.read[-1]

    def empty(self) -> bool:
        return not bool(len(self.write) + len(self.read))

    def _move_elements(self) -> None:
        self.read = self.write[::-1]
        self.write = []


# Your MyQueue object will be instantiated and called as such:
mq = MyQueue()
mq.push(1)
foo = mq.pop()
assert (res := foo) == 1, res
assert (res := mq.empty()) is True, res
