class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid:
            return

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
        