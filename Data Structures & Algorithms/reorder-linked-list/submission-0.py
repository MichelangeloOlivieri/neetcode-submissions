# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        1) Questions about edge cases or empty list
        2) Create a deque where numbers can be removed from the front and back istantaneously
        and a list to keep track of the numbers associated to a position
        """

        array = []
        curr = head
        while curr:
            array.append(curr)
            curr = curr.next

        queue = deque(array)
        curr = head
        queue.popleft()
        index = 1

        while queue:
            if index == 1:
                curr.next = queue[-1]
                queue.pop()
                curr = curr.next
                index = 0
            elif index == 0:
                curr.next = queue[0]
                queue.popleft()
                curr = curr.next
                index = 1

        curr.next = None


        """
        3) Dry run: seems ok (tried on paper) 
        4) Time complexity O(n); space complexity O(n)
        """
        



        