class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if not coins:
            return -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float('inf') else -1
        