class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        1) Il problema è ben definito, niente da aggiungere
        2) - Soluzione 1: scorrere l'array, e per ogni intero riscorrere in avanti
        finché non si trova la soluzione -> tempo O(n^2), dove n = len(numbers)
        - Soluzione 2: non me ne viene in mente un'altra
        3) Scrivo codice
        """

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] < target:
                    continue
                elif numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        """
        4) Test case: - numbers = [1, 2, 3, 4]
        - i = 0; j = 1: 1 + 2 = 3 < 3 -> [0, 1] -> [1, 2]
        5) Complessità temporale O(n^2); complessità spaziale O(1)
        """

        
