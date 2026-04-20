class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # linked list and Floyd's algorithm

        """
        Idea: pensare alle posizioni degli interi degli array come nodi e al
        contenuto di quelle posizioni (cioè gli interi stessi) come puntatori alla
        prossima posizione della linked list; siccome è garantito che un numero è 
        ripetuto, ci sarà un loop; per individuare il numero ripetuto si usa lo
        algoritmo di Floyd: si prende il punto dove il puntatore veloce e quello 
        lento si incontrano, e poi facendo partire un nuovo puntatore lento si vede
        che i due puntatori lenti si incontrano esattamente nel punto corrispondente
        all'intero ripetuto
        """

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        new_slow = 0
        while True:
            slow = nums[slow]
            new_slow = nums[new_slow]
            if slow == new_slow:
                return slow

        """
        Time complexity O(n), where n = len(nums); space complexity O(1)
        """        
        