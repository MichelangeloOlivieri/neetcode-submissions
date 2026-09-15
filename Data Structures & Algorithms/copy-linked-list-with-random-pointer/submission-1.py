"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:

        old_to_copy = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val, None, None)
            old_to_copy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]

        """
        - Time complexity O(n), where n is the number of nodes
        - Space complexity O(n)
        """