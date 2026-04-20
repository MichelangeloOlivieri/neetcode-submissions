# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        1) Empty input
        2) Go through the two linked lists and create a new one summing the digits
        """

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new value
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # updating pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        """
        3) Ok
        4) Time complexity O(n), where n is the maximum of nodes of the two linked 
        lists; space complexity O(n)
        """

