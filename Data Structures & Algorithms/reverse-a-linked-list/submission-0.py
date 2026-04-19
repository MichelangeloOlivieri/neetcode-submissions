# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        1) Empty inputs and stuff; no idea about other questions
        2) Solution 1: scan through all the nodes and reverse the order
        """

        curr = head
        precedente = None

        while curr:

            temp = curr.next
            curr.next = precedente
            precedente = curr
            curr = temp

        return precedente

        """
        3) Dry run: seems ok (tried it on paper)
        4) Time complexity O(n); space complexity O(1)
        """