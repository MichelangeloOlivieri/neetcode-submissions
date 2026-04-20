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

        if not l1 and not l2:
            return None

        # Inizializziamo un nodo fittizio per tenere traccia della testa della nuova lista
        dummy = ListNode(0)
        curr = dummy # curr sarà il cursore che costruisce la lista
        
        first = l1
        second = l2
        remainder = 0

        # FASE 1: Entrambe le liste hanno nodi
        while first and second:
            total = first.val + second.val + remainder
            
            # Creiamo il nodo e lo colleghiamo SUBITO
            curr.next = ListNode(total % 10)
            curr = curr.next # Avanziamo il cursore
            
            # Calcolo del riporto compatto
            remainder = 1 if total > 9 else 0
            
            first = first.next
            second = second.next

        # FASE 2: La prima lista era più lunga (es. 100 + 1)
        while first:
            total = first.val + remainder
            curr.next = ListNode(total % 10)
            curr = curr.next
            remainder = 1 if total > 9 else 0
            first = first.next

        # FASE 3: La seconda lista era più lunga
        while second: 
            total = second.val + remainder
            curr.next = ListNode(total % 10)
            curr = curr.next
            remainder = 1 if total > 9 else 0
            second = second.next

        # FASE 4: Edge case critico - Se alla fine avanza un riporto (es. 5 + 5 = 10)
        if remainder > 0:
            curr.next = ListNode(remainder)

        # Restituiamo tutto ciò che c'è dopo il nodo fittizio iniziale
        return dummy.next

        """
        3) Ok
        4) Time complexity O(n), where n is the maximum of nodes of the two linked 
        lists; space complexity O(n)
        """

