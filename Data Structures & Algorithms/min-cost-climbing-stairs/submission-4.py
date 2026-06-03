class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if not cost:
            return 0
        
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        prev2 = 0
        prev1 = min(0, cost[0])
        curr = float('inf')
        i = 2

        while i <= len(cost):
            curr = min(prev2 + cost[i - 2], prev1 + cost[i - 1])
            prev2 = prev1
            prev1 = curr
            i += 1

        return curr


        """
        cost = [-1, 0, 4, 1]
        dp = [float('inf')] * 5
        dp[0] = 0, dp[1] = -1, dp[2] = -1, dp[3] = -1, dp[4] = 0
        """      