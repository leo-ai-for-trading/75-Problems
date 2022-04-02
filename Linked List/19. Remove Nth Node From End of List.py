# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - left, right pointer
        - shift each pointer by 1
        - the right null goes on null node and the left pointer is where we want to delete the node
        - initialize left at the dummy node 0
        - update the left pointer on the last node of the linked list and return dummy.next
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right: 
            left = left.next
            right = right.next
        
        #delete the node
        #update left node next pointer
        left.next = left.next.next
        return dummy.next
