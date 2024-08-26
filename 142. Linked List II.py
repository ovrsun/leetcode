# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next

        while fast != slow:
            if fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
        
        slow = head
        fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
        

# [3,2,0,-4]
node3 = ListNode(-4)
node2 = ListNode(0)
node1 = ListNode(2)
node0 = ListNode(3)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node1

head = node0
sln = Solution()
print(sln.detectCycle(head))
