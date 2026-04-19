class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        l, r = 0, 0
        profit = 0

        while r < len(prices):

            while r < len(prices) and prices[r] >= prices[l]:
                profit = max(profit, prices[r] - prices[l])
                r += 1

            l = r
            r += 1

        return profit