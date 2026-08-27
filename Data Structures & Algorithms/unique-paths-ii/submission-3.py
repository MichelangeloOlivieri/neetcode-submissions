class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        dp = [0] * n
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    dp[j] = 0
                elif j + 1 < n:
                    dp[j] += dp[j + 1]

        return dp[0]

        """
        -- Time complexity O(m * n)
        -- Space comeplexity O(n)
        """