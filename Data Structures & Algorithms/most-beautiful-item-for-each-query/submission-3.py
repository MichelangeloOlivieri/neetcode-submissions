class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort(key=lambda x: x[0])
        prices = []
        best = []
        max_beauty = 0
        
        for price, beauty in items:
            prices.append(price)
            max_beauty = max(max_beauty, beauty)
            best.append(max_beauty)
            
        res = []
        for q in queries:
            left = 0
            right = len(prices)
            while left < right:
                mid = (left + right) // 2
                if prices[mid] <= q:
                    left = mid + 1
                else:
                    right = mid
            res.append(best[left - 1] if left > 0 else 0)
            
        return res

        """
        - Time complexity O((m + n) * log(n)), where n = len(items) and m = len(queries)
        - Space complexity O(m + n) (for TimSort and result)
        """