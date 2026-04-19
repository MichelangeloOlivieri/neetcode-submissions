class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # soluzione mia

        """
        1) Il problema assicura che esiste un'unica coppia che soddisfa i criteri;
        pertanto non mi pare ci sia alcun problema sull'input; forse mi posso chiedere
        se l'input sia già ordinato perché vedo che quelli suggeriti son già ordinati
        2) Brute force: ciclo prima sulle entrate dell'array, e poi per ogni entrata
        ciclo di nuovo sulle successive -> tempo O(len(nums)^2), spazio O(1)
        Soluzione ottimizzata: nulla di che al momento
        3) Scrivo codice
        """

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        """
        4) Test case: 
        - nums = [3, 4, 5, 6], target = 7
        - i = 0: j = 1; 3 + 4 = 7; [0, 1]
        5) complessità temporale O(len(nums)^2), spaziale O(1)
        """
