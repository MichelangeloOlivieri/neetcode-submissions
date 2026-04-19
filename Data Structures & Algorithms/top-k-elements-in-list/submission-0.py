class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # soluzione mia

        """
        1) L'input è un array di interi, e per i constraints il problema è sempre 
        ben posto; l'ordine è ininfluente -> nessuna domanda
        2) Soluzione 1: fare una hash map dict = {[intero: frequenza]}, poi fare k 
        volte max sulle frequenze al variare degli elementi in dict: spazio e tempo
        O(n)
        Soluzione 2: fare una hash map dict = {[intero: frequenza]}, poi fare una
        lista delle frequenze, ordinarla e... aspetta, così perdo traccia dello
        elemento associato -> casino -> vado di soluzione 1
        3) Scrivo codice
        """

        frequency_dict = defaultdict(int)

        for integer in nums:
            frequency_dict[integer] = frequency_dict.get(integer, 0) + 1
        
        most_frequent = []
        for _ in range(k):
            m = max(frequency_dict[integer] for integer in frequency_dict)
            for integer in frequency_dict:
                if frequency_dict[integer] == m:
                    most_frequent.append(integer)
                    del frequency_dict[integer]
                    break
        
        return most_frequent

        """
        4) Test case: - nums [1, 2, 2, 3, 3, 3], k = 2
        - frequency_dict = {1:1, 2:2, 3:3}
        - counter = 0
            m = 3
            integer = 1 -> no
            integer = 2 -> no
            integer = 3 -> ok -> most_frequent = [3]

        5) Complessità temporale O(len(nums)^2); complessità spaziale O(len(nums))
        """
        