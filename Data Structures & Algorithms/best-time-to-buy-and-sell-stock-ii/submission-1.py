class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        1)  prices = [1, 2, 3, 1, 5] -> 6
            prices = [4, 2, 1] -> 0
            prices = [1] -> 0
        2) Brute Force + Array (Two Pointers pattern)
        """        

        if not prices:
            return 0

        res = 0

        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                res += prices[i] - prices[i - 1]

        return res

        """
        3) l = 0, r = 1; l = 1, r = 2
        4) Time complexity O(n), where n = len(prices); space complexity O(1)
        """

            