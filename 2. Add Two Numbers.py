# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = ListNode()
        fake = node

        while l1 or l2 or carry:
            val = carry
            if l1: val += l1.val
            if l2: val += l2.val

            carry = 1 if val > 9 else 0
            val = (val - 10) if val > 9 else val
            node.next = ListNode(val=val)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            node = node.next

        return fake.next
