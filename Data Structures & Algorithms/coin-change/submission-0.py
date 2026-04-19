class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # soluzione dp standard

        if not coins:
            return -1 

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(amount + 1):
            for c in coins:
                if c <= a:
# se a - c non è presente nell'array, ossia non è possibile sommare alcun valore nell'array per 
# ottenere la quantità desiderata, si rimane con amount + 1
                    dp[a] = min(dp[a], 1 + dp[a - c]) 

        return dp[amount] if dp[amount] != amount + 1 else - 1

        """
        4) Time complexity O(amount * len(coins)); space complexity O(amount)
        """