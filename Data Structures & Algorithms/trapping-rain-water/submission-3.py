class Solution:
    def trap(self, height: List[int]) -> int:
        
        # soluzione ottimizzata in tempo O(n) e spazio O(1)

        res = 0
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]

        # come prima, la quantità di acqua che può stare sopra una cella è data
        # dalla differenza tra l'altezza della cella e il più piccolo muro di
        # altezza massima a sinistra o a destra della cella; se la differenza
        # è <= 0, l'acqua scivola via e sommo zero

        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(height[l], max_left)
                water = max(min(max_left, max_right) - height[l], 0)
                res = res + water
            else:
                r -= 1
                max_right = max(height[r], max_right)
                water = max(min(max_left, max_right) - height[r], 0)
                res = res + water
            
        return res

        """
        Test case: - height = [0,2,0,3,1,0,1,3,2,1]
        - l = 1; max_left = 2; water = 0
        - r = 8; max_right = 2; water = 0
        - l = 2; max_left = 2; water = 2
        - etc
        """




