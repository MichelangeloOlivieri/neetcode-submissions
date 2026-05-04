class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        """
        1) Empty input
        2) Dfs
        """

        if not grid:
            return 0

        res = 0
        area = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j):

            nonlocal area
            area += 1
            
            visited.add((i, j))
            q = collections.deque()
            q.append((i, j))

            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row in range(m) and new_col in range(n) 
                        and grid[new_row][new_col] == 1 
                        and (new_row, new_col) not in visited):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        dfs(new_row, new_col)            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    res = max(res, area)
                    area = 0                    

        return res
        
        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """