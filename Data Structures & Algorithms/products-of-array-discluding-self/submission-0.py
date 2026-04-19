class Solution:
    from typing import List
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        1) Gestire il caso nums = []? Al di là di questo non ho domande
        2) Soluzione 1: inizializzare un array res = [], scorrere nums, per
        ogni n in nums fare un ulteriore scorrimento, moltiplicare, e infine
        dividere per n -> tempo O(n^2), spazio O(n)
        Soluzione 2: scorrere su tutti gli elementi dell'array e fare il prodotto; 
        poi fare un array res[i] dove a ogni entrata prendo quel prodotto e 
        divido per nums[i] -> tempo O(n), spazio O(n)
        3) Scrivo codice
        """

        
        res = [] 
        index = 0
        product = 1

        zero_counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_counter += 1
                index = i

        if zero_counter >= 2:
            return [0] * len(nums)

        elif zero_counter == 0:
            for n in nums: 
                product = product * n
            for i in range(len(nums)):
                res.append(product // nums[i])

        elif zero_counter == 1:
            for i in range(0, index):
                product = product * nums[i]
            for i in range(index + 1, len(nums)):
                product = product * nums[i]
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(product)
                else: 
                    res.append(0)

        return res

        """
        4) Test case: - nums = [1, 2, 4, 6]
        - product = 1 * 1 * 2 * 4 * 6 = 48
        - res = [48/1 = 48, 48/2 = 24, 12, 8]
        5) Complessità temporale O(m) dove m = len(nums); complessità spaziale
        O(m)
        """