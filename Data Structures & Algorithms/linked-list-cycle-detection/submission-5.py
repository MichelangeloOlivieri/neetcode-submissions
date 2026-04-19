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

        visited = set()
        curr = head

        while curr:
            if not visited:
                visited.add(curr)
                curr = curr.next
            else:
                if curr in visited:
                    return True
                else:
                    visited.add(curr)
                    curr = curr.next

        return False

        """
        3) Dry run: seems ok (tried it on paper)
        4) Time complexity O(n); space complexity O(1)
        """