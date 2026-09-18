class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1: 
            return 1

        prev = 0
        curr = 1

        while n > 0:
            prev, curr = curr, prev + curr
            n -= 1

        return curr

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
        