class Solution:
    def trap(self, height: List[int]) -> int:
        
        # soluzione ottimizzata in tempo O(n) e spazio O(n)

        res = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        # prendo per ogni elemento il muro di altezza massima a sinistra e 
        # il muro di altezza massima a destra

        for i in range(1, len(height)):         
            max_left[i] = max(height[i - 1], max_left[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        # la quantità di acqua che può stare sopra una cella è data dalla minima 
        # altezza tra il massimo muro sinistro e il massimo muro destro meno la 
        # altezza della cella stessa; se viene <= 0, reimposto a zero

        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            if water <= 0:
                water = 0
            res = res + water

        return res

        
            

