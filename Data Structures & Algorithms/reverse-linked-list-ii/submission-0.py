class ListNode:
    def __init__(self, value=0, following=None):
        self.val = value
        self.next = following

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        """
        1) Assuming input makes sense (0 <= left <= right <= len(list))
        2) Use standard algorithm to reverse a singly linked list, use a count to get
        to the left node, and start reversing until you arrive at the right node
        """

        if not head:
            return None

        count = 1
        prev = None
        curr = head
        while count < left:
            prev = curr
            curr = curr.next
            count += 1

        # starting point at (left - 1)
        start = prev
        # ending point at (left)
        end = curr

        # prev is at (left) and curr at (left + 1)
        prev = curr
        curr = curr.next
        while count < right:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
            count += 1

        # prev is at (right) and curr at (right + 1)
        if start:
            start.next = prev
            end.next = curr
            return head
        else:
            end.next = curr
            return prev

        """
        3) 0 -> 1 -> 2 -> 3 -> 4 -> 5, left = 2, right = 4
        4) Time complexity O(right); space complexity O(1)
        """