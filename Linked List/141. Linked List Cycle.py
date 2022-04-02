# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            #let the node become empty
            if head.val:
                
                head.val = None
            else:
                #if we find an empty node there is a cycle
                return True
            head = head.next
        return False
