# https://leetcode.com/problems/design-circular-queue/description/

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue: list = [None] * k
        self.head: int = -1
        self.tail: int = -1
        self.size: int = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % len(self.queue)
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
            self.size = 0
            return True
        self.head = (self.head + 1) % len(self.queue)
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.queue)


obj = MyCircularQueue(3)
assert obj.enQueue(1) is True
assert obj.enQueue(2) is True
assert obj.enQueue(3) is True
assert obj.enQueue(4) is False
assert obj.Rear() == 3
assert obj.isFull() is True
assert obj.deQueue() is True
assert obj.enQueue(4) is True
assert obj.Rear() == 4
