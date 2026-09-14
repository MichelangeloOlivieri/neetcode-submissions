# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        """
        1) [[1, 2], [3, 5], [5, 8]] -> [1, 2, 3, 5, 5, 8]
        2) Min-Heap
        """

        if not lists:
            return None

        min_heap = []
        index = 0

        for head in lists:
            if head:
                index += 1
                value = head.val
                following = head.next
                heapq.heappush(min_heap, (value, index, following))

        dummy = ListNode(-float('inf'), None)
        curr = dummy

        while min_heap:
            value, index, following = heapq.heappop(min_heap)

            if following:
                heapq.heappush(min_heap, (following.val, index, following.next))

            curr.next = ListNode(value, None)
            curr = curr.next

        return dummy.next

        """
        - Time complexity O(sum(length[i]) * log(k)), where length[i] = len(lists[i])
        - Space complexity O(k)
        """