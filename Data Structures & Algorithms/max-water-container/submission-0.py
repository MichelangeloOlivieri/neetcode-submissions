class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # soluzione mia

        """
        1) Devo calcolare il rettangolo di area massima; il problema è ben posto
        e a parte i casi stupidi tipo input vuoto non mi sembra che valga la pena
        di fare domande chiarificatrici all'intervistatore -> invece c'era bisogno
        di chiedere len(heights) > 1
        2) - Soluzione 1: inizializzare un intero "area", fare i doppi scorrimenti
        e vedere quando è massimo -> tempo O(n^2)
        - Soluzione 2: ho letto gli hint ma non sono sicuro di aver capito, provo
        a implementarla 
        3) Scrivo codice
        """

        max_area = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            current_area = (j - i) * min(heights[i], heights[j])
            if current_area > max_area:
                max_area = current_area
            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1

        return max_area

        """
        4) Test case: ok
        5) Complessità temporale O(n); complessità spaziale O(1)
        """


        