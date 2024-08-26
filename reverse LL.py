class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1
while head:
    print(head.val)
    head = head.next

head = node1
prev = None

# None  1 -> 2 -> 3 -> 4 -> None
while head:
    temp = head
    head = head.next
    temp.next = prev
    prev = temp

while temp:
    print(temp.val)
    temp = temp.next