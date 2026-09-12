class Solution:
    def integerBreak(self, n: int) -> int:

        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            res = 0
            for j in range(2, (i // 2) + 1):
                res = max(dp[j] * dp[i - j], res)
            dp[i] = res

        return dp[n]

        """
        - Time complexity O(n^2)
        - Space complexity O(n)
        """