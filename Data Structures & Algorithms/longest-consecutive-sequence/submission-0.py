class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # soluzione mia + soluzione ottimizzata

        """
        1) Il problema è ben posto e la soluzione, se non unica, suppongo possa
        essere scelta tra le possibili; quindi nulla da dire
        2) - Soluzione 1: scorrere l'array e a partire da ogni intero scrivere la
        sequenza corrispondente, salvarle tutte in una matrice dove gli indici
        delle righe identificano gli indici degli interi, e le righe sono le 
        sequenze effettive -> tempo O(n^2), dove n = len(nums) e spazio O(n^2)  
        - Soluzione 2: ordinare l'array con nums.sort(), convertirlo in stringa, 
        scorrere sui caratteri: se trovo un carattere che non sia il successore
        del precedente, inserisco un carattere speciale e so dove tagliare la
        stringa poi dopo; tempo O(nlogn) per ordinare, spazio O(n) per l'array
        finale di stringhe
        - Soluzione 3: non so come fare in tempo O(n)
        """

        number_set = set(nums)
        longest_length = 0

        for n in nums:
            if n - 1 not in number_set:
                length = 0
                while (n + length) in number_set:
                    length += 1
                longest_length = max(longest_length, length)

        return longest_length

        """
        Test case: - nums = [2, 20, 4, 10, 3, 4, 5]
        - length(2) = 0; 2 in number_set -> length = 1
        """

                



        
