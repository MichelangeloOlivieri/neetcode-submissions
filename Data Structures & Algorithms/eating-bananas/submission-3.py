class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        1) piles[i] and h must be positive numbers; h must be greater or equal than len(piles);
        what happens if I first eat some bananas from a pile[i] and then in the next hour I eat
        more bananas than how many are still left in the pile? can i go on eating from another 
        pile?
        2) - Solution 1: find the max in the array piles and for each 0 <= k <= max find out
        whether i can finish eating the piles in time by calculating Sum_i((piles[i] + 1) // k)
        """

        # binary search

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = sum((p - 1) // mid + 1 for p in piles)

            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l

        """
        3) Dry run: - piles = [1, 4, 3, 2], h = 9;
        - maximum = 4, res = 4, k = 4;
        - maximum = 3, res = 5, k = 3;
        - maximum = 2, res = 6, k = 2; 
        - maximum = 1, res = 10, k = 2;
        4) Time complexity O(max(piles) * len(piles)); space complexity O(1)
        """

        
        