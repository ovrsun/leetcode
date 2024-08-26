# https://leetcode.com/problems/design-hashmap/description/

class MyHashMap:
    self.size = 1000

    def __init__(self):
        self.keys = [[] for _ in range(self.size)]
        self.values = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        contains, id = self._contains_and_id(key)
        k = self._hash(key)

        if not contains:
            self.keys[k].append(key)
            self.values[k].append(value)
            return

        self.values[k][id] = value
        return
        

    def get(self, key: int) -> int:
        contains, id = self._contains_and_id(key)
        if not contains:
            return None
        k = self._hash(key)
        return self.values[k][id]
        

    def remove(self, key: int) -> None:
        contains, id = self._contains_and_id(key)
        if not contains:
            return None
        k = self._hash(key)
        self.keys[k].pop(id)
        self.values[k].pop(id)
        return

    def _hash(self, key: int) -> int:
        return key % 1000
    
    def _contains_and_id(self, key) -> tuple[bool, int]:
        k = self._hash(key)
        if self.keys[k] == []:
            return False, -1
        for i in range(len(self.keys[k])):
            if self.keys[k][i] == key:
                return True, i
        return False, -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)