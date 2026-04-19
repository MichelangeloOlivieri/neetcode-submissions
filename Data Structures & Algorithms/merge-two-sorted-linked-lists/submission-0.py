# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # tentativo mio

        """
        1) Which criterion should one use to merge the lists?
        2) Scan through the lists and add the nodes in increasing order
        """

        if not list1:
            return list2
        if not list2: 
            return list1

        if list1.val < list2.val:
            res = list1
            aux = list2
        else:
            res = list2
            aux = list1

        head = res

        while res and aux:

            if res.next:
                if aux.val < res.next.val:
                    temp = res.next
                    res.next = aux
                    aux = temp
                    res = res.next
                else:
                    res = res.next
            else:
                res.next = aux
                break
            
        return head

        """
        3) Dry run: ok on paper
        4) Time complexity O(m + n); space complexity O(1)
        """
        
