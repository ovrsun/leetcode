import random

class RandomizedSet:

    def __init__(self):
        self.current = set()
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Returns true if the item was not present, false otherwise.
        """
        res = val not in self.current
        if res:
            self.current.add(val)
        self.array.append(val)
        return res

    def remove(self, val: int) -> bool:
        """
        Returns true if the item was present, false otherwise.
        """
        res = val in self.current
        self.current.discard(val)
        return res

    def getRandom(self) -> int:
        rand = random.choice(self.array)
        while rand not in self.current:
            rand = random.choice(self.array)
        return rand


# I
randomized_set = RandomizedSet()
assert randomized_set.insert(1) is True
assert randomized_set.remove(2) is False
assert randomized_set.insert(2) is True
assert (res := randomized_set.getRandom()) in( 1, 2), res
assert randomized_set.remove(1) is True
assert randomized_set.insert(2) is False
assert randomized_set.getRandom() == 2

# II
randomized_set = RandomizedSet()
assert randomized_set.remove(0) is False
assert randomized_set.remove(0) is False
assert randomized_set.insert(0) is True
assert randomized_set.getRandom() == 0
assert randomized_set.remove(0) is True
assert randomized_set.insert(0) is True
