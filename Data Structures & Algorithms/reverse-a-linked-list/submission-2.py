# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # soluzione iterativa
        
        """
        1) Empty inputs and stuff; no idea about other questions
        2) Solution 1: scan through all the nodes and reverse the order
        """

        curr = head
        prec = None

        while curr:

            temp = curr.next
            curr.next = prec
            prec = curr 
            curr = temp

        return prec

        """
        3) Dry run: seems ok (tried it on paper)
        4) Time complexity O(n); space complexity O(1)
        """