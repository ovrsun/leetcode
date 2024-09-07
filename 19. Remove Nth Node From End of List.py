https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # []->1->2->3->4->None, 2
        fake = ListNode(next=head)
        fast = slow = fake
        for i in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return fake.next
        
#         # []->1-None, 1
#         slow(fake).next = slow.next.next, e.i. none
#         return fake.next
    
#         # []->1->2->None, 1
#         return fake.next
        
#         # []->1->2->None, 2
#         return fake.next