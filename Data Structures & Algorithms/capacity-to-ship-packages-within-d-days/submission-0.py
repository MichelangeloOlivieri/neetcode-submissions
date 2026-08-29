class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            ships = 1
            curr_cap = capacity
            
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    curr_cap = capacity
                curr_cap -= w
                
            return ships <= days

        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

        """
        - Time complexity O(m * log(n)), where m = len(weights) and n = sum(weights) - max(weights)
        - Space complexity O(1)
        """