class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if not cost:
            return 0
        
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [float('inf')] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = min(0, cost[0])
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]) 

        return dp[-1]

        """
        cost = [-1, 0, 4, 1]
        dp = [float('inf')] * 5
        dp[0] = 0, dp[1] = -1, dp[2] = -1, dp[3] = -1, dp[4] = 0
        """      