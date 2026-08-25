class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)  
        n = len(grid[0])
        directions = [(1, 0), (0, 1)]
        memo = {}
        res = 0

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            paths = 0
            for di, dj in directions:
                new_i, new_j = i + di, j + dj

                if (new_i >= 0 and new_i < m and 
                new_j >= 0 and new_j < n and
                grid[new_i][new_j] != 1):
                    paths += dfs(new_i, new_j)

            memo[(i, j)] = paths
            return paths

        if grid[0][0] != 1:
            res = dfs(0, 0)

        return res

        """
        grid = [[0, 0, 0], 
                [0, 0, 0],
                [0, 1, 0]]
        - (0, 0): visited = {(1, 0)} -> (1, 0): visited = {(1, 0), (1, 1)} -> (2, 0): return
                                                                           -> (1, 1): visited = {(1, 0), (1, 1), (2, 1)}
        """