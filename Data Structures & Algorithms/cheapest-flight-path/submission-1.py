class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            
            tmpPrices = prices.copy()

            for s, d, p in flights:
                
                # Se il nodo sorgente è stato già raggiunto in passato 
                # e il nuovo volo offre un prezzo totale inferiore a quello attualmente noto per la destinazione:
                if prices[s] != float("inf") and prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]

        """
        Time complexity O(n + (m * k)), where m is the number of flights; space 
        complexity O(n)
        """

    