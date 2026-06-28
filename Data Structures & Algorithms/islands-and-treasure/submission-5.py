class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        """
        1) Can u modify grid in place?
        2) Multiple BFS's
        """

        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if (new_row in range(m) and 
                    new_col in range(n) and 
                    grid[new_row][new_col] == 2147483647):
                    grid[new_row][new_col] = grid[row][col] + 1
                    q.append((new_row, new_col))

        """
        3) - grid = [[INF, -1, INF], [-1, 1, 0], [INF, 0, -1]]
            - row, col = 1, 2 -> grid[0][2] = 1
        4) Time complexity O(m * n); space complexity O(m * n)
        """        
