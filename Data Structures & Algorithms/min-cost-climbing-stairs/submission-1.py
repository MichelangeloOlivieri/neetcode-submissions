class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """
        1) Empty input; example seen
        2) Dp solution
        """        

        if not cost: 
            return 0
            
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]

        """
        3) Ok
        4) Time complexity O(n); space complexity O(n)
        """