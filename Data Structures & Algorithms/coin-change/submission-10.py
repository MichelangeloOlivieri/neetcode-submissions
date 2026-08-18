class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        1) coins = [1, 5, 10], amount = 12 -> 3
        2) Array, DP
        """

        if not coins:
            return 0

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  

        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(1 + dp[i - c], dp[i])

        return dp[amount] if dp[amount] != float('inf') else -1

        """
        3) -> coins = [1, 5, 10], amount = 12
        dp = [0, 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf', 'inf']
        - i = 1: dp[1] = 1
        - i = 2: dp[2] = 2
        - i = 3: dp[3] = 3
        - ...
        - i = amount: dp[amount] = min(1 + dp[11], 1 + dp[7], 1 + dp[2]) = 3
        -> coins = [2], amount = 3
        dp = [0, 'inf', 'inf', 'inf']
        - i = 1: dp[1] = 'inf'
        - i = 2: dp[2] = 1
        - i = 3: dp[3] = 'inf'
        4) Time complexity O(amount * len(coins)); space complexity O(amount)
        """