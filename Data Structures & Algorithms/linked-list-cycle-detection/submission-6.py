# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # tentativo mio

        """
        1) All good apart from edge cases like empty linked list
        2) Seen the hints
        """

        if not head:
            return False

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

        """
        3) Dry run: seems ok (tried it on paper)
        4) Time complexity O(n); space complexity O(1)
        """