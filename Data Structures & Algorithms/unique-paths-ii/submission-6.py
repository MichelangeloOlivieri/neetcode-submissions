class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
                if i == m - 1 and j == n - 1:
                    dp[i][j] = 1
                if grid[i][j] == 1:
                    dp[i][j] = 0

        return dp[0][0]

        """
grid =  [[0, 0, 0]
         [0, 1, 0]
         [1, 0, 0]]

  dp  = [[1, 1, 1]
         [0, 0, 1]
         [0, 1, 1]]
        """

        """
        - Time complexity O(m * n)
        - Space complexity O(m * n)
        """