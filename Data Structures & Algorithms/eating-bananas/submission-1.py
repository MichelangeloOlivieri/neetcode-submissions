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

        if h == len(piles):
            return max(piles)

        maximum = max(piles)
        if maximum == 0:
            return 0  

        l = 1
        r = maximum 

        while l <= r:

            mid = (l + r) // 2

            res = 0
            for i in range(len(piles)):
                if piles[i] == 0:
                    continue
                else:
                    res = res + 1 + (piles[i] - 1) // mid
            
            if res <= h:
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

        
        