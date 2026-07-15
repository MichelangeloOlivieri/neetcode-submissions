# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, 
        head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        1) head = [10, 5, 15, 10] -> head = [10, 5, 5, 5, 15, 5, 10]
        2) Use two pointers
        """

        if not head:
            return None

        prev = head
        curr = head.next
        while curr:
            GCD = math.gcd(prev.val, curr.val)
            prev.next = ListNode(GCD, curr)
            prev = curr
            curr = curr.next

        return head

        """
        3) Ok
        4) Time complexity O(n), where n = len(head); space complexity O(n)
        """

    def _compute_mcd(self, x: float, y: float) -> float:
        if x is None or y is None:
            raise ValueError("Input error.")
        if x == 0 or y == 0:
            return 0
        if x == 1 or y == 1:
            return 1
        
