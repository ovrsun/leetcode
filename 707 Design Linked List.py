class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
        # ["MyLinkedList","addAtHead","addAtIndex","get"]
        # [[],[2],[0,1],[1]]
        # 1 -> 2

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size <= index:
            return -1
        obj = self.head
        for i in range(index):
            obj = obj.next
        return obj.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index:
            return None
        if index == 0:
            curr = Node(val, self.head)
            self.head = curr
            self.size += 1
            return
            
            
        obj = self.head
        for i in range(index-1):
            obj = obj.next
        next = obj.next
        obj.next = Node(val, next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.size <= index:
            return
        if index == 0:
            self.head = self.head.next
            return
#         if index == self.size - 1:
#             ...
        obj = self.head
        for i in range(index-1):
            obj = obj.next
        obj.next = obj.next.next
        self.size -= 1
        

llist = MyLinkedList()
llist.addAtHead(2)
llist.addAtIndex(0, 1)
print(llist.get(1))

# ["MyLinkedList","addAtHead","addAtIndex","get"]
# [[],[2],[0,1],[1]]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)