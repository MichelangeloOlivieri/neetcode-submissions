class Solution:
    def numSquares(self, n: int) -> int:

        """
        1) n = 6 -> 2
        - squares = {1, 4}
        - dp = [0, 1, 2, 3, 1, 2, 3]
        2) Dynamic Programming
        """

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                square = j * j
                if square > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]

        """
        -- Time complexity O(n * n^(1/2))
        -- Space complexity O(n)
        """