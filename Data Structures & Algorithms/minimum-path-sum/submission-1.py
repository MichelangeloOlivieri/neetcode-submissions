class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * (n + 1)
        dp[n - 1] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0]
        
        """
        - Time complexity O(m * n)
        - Space complexity O(n)
        """