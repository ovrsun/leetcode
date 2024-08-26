# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:
    def __init__(self):
        self.hashset = [0] * 1000

    def add(self, key: int) -> None:
        self.hashset[key % 1000] = 

    def remove(self, key: int) -> None:
        self.hashset[key] = 0

    def contains(self, key: int) -> bool:
        return self.hashset[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)