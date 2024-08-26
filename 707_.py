class Node:
    def __init__(self, val=0, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        new_head = Node(val=val, next=self.head)
        if self.size:
            self.head.prev = new_head
        self.head = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val=val)
            return
        node = self.head
        # 1 2 3 4
        for _ in range(self.size - 1):
            node = node.next
        node.next = Node(prev=node, val=val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # print(node, asd)
        if index > self.size or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        # 1 2 3 4 
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        next = prev.next
        new = Node(val=val, prev=prev, next=next)
        next.prev = new
        prev.next = new
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        if index == 0 and self.size == 1:
            self.head = None
            self.size -= 1
            return None
        if index == 0:
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None
            self.size -= 1
            return
        
        node = self.head
        # 1 2 3 4
        # 1 2 3
        for _ in range(index):
            node = node.next
        prev = node.prev
        next = node.next
        prev.next = next
        if index != self.size - 1:
            next.prev = prev
        self.size -= 1
        return
        
    def get_node_by_index(self, index: int) -> Node | None:
        if index >= self.size or index < 0:
            return None
        node = self.head
        # 1 2 3 4
        for _ in range(index):
            node = node.next
        return node

    def print_list(self) -> None:
        node = self.head
        while node:
            print(node.val, end=' -> ')
            node = node.next
        print('None')


ll = MyLinkedList()
ll.print_list()

ll.addAtTail(1)
ll.addAtTail(3)
print(ll.get(1))

# ["MyLinkedList","addAtTail","addAtTail","get"]
# [[],[1],[3],[1]]



# print(ll.size)


# ll.addAtHead(1)
# ll.print_list()
# print(ll.size)



# ll.addAtTail(3)
# ll.print_list()
# print(ll.size)


# ll.addAtIndex(1,2)
# ll.print_list()
# print(ll.size)



# print(ll.get(1))


# ll.deleteAtIndex(1)
# ll.print_list()
# print(ll.size)



# print(ll.get(1), '----')
# print(ll.get(3), '-----')
# ll.deleteAtIndex(3)


# ll.deleteAtIndex(0)
# ll.print_list()
# print(ll.size)


# print(ll.get(0))

# ll.deleteAtIndex(0)
# ll.print_list()
# print(ll.size)



# # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get",
# # "get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
# # [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]




# # node1 = Node(val=1)
# # node2 = Node(val=2, prev=node1)
# # node3 = Node(val=3, prev=node2)
# # node4 = Node(val=4, prev=node3)
# # node1.next = node2
# # node2.next = node3
# # node3.next = node4

# # ll = MyLinkedList()

# # assert (res := ll.get(0)) == -1, res
# # assert (res := ll.get(4)) == -1, res

# # ll.head = node1
# # ll.size = 4
# # assert (res := ll.get(0)) == node1.val, res
# # assert (res := ll.get(1)) == node2.val, res
# # assert (res := ll.get(2)) == node3.val, res
# # assert (res := ll.get(3)) == node4.val, res

# # old_head = ll.head
# # ll.addAtHead(5)
# # assert (res := ll.size) == 5, res
# # assert (res := ll.get(0)) == 5, res
# # assert (res := ll.get(1)) == 1, res
# # assert (res := ll.head.next) == old_head
# # assert (res := ll.head.val) == ll.get(0), res
# # assert (res := old_head.prev) == ll.head, res

# # ll.addAtTail(6)
# # assert (res := ll.size) == 6, res
# # tail = ll.get_node_by_index(ll.size)
# # assert tail is None, tail
# # tail = ll.get_node_by_index(ll.size-1)
# # assert tail is not None, tail
# # assert tail.next is None, tail.next
# # assert tail.prev == ll.get_node_by_index(ll.size-2)
# # assert (res := ll.get(6)) == -1, res



# # current_size = ll.size
# # index = current_size + 1
# # assert (res := ll.size) == current_size, res
# # index = current_size
# # ll.addAtIndex(index, 10)
# # assert (res := ll.size) == current_size + 1, res

# # ll.print_list()
# # ll.deleteAtIndex(1000)
# # current_size = ll.size
# # ll.deleteAtIndex(current_size-1)
# # ll.print_list()

# # ll.deleteAtIndex(0)

# # ll.print_list()

# # ll.deleteAtIndex(2)
# # ll.print_list()
# # assert (res := ll.get_node_by_index(1).val) == 2, res
# # assert (res := ll.get_node_by_index(2).val) == 4, res
# # assert (res := ll.get_node_by_index(1).next) == ll.get_node_by_index(2), res
# # assert (res := ll.get_node_by_index(2).prev) == ll.get_node_by_index(1), res

# # # Your MyLinkedList object will be instantiated and called as such:
# # # obj = MyLinkedList()
# # # param_1 = obj.get(index)
# # # obj.addAtHead(val)
# # # obj.addAtTail(val)
# # # obj.addAtIndex(index,val)
# # # obj.deleteAtIndex(index)