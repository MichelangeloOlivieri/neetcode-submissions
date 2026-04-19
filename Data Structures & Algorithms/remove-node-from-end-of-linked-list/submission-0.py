# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        """
        1) All good apart from edge cases
        2) Go through the list until the end to count its length, then remove the (length - n)-th
        node
        """

        # measuring list length
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        # removing (n-th)-to-last node 
        if length == n:
            return head.next

        index = 1
        prev = None
        curr = head
        while index < length - n + 1:
            prev = curr
            curr = curr.next
            index += 1
        
        prev.next = curr.next  

        return head

        """
        3) Dry run: seems ok
        4) Time complexity O(n); space complexity O(1)
        """