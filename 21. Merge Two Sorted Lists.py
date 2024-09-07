# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # l1: None
        # l2: None
        
        # l1: 1 -> 2 -> ... -> None
        # l2: None or vice versa
        
        node = ListNode()
        new_head = node
        
        
        # l1: 1 2 3 5 None
        # l2: 1 4 None
        # n : [] -> 1 -> 1 -> 2 -> 3 -> 4
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 if list1 else list2
        
        return new_head.next
        
        
        # l1: 1 -> 2 -> ... -> None
        # l2: 2 -> 3 -> 6 -> ... -> None
        
        # l1: 2 -> 3 -> 6 -> ... -> None
        # l2: 1 -> 2 -> ... -> None