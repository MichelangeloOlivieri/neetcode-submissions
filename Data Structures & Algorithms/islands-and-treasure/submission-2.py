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
                if(row + dr in range(m) and
                    col + dc in range(n) and
                    grid[row + dr][col + dc] == 2147483647):
                    grid[row + dr][col + dc] = grid[row][col] + 1
                    q.append((row + dr, col + dc))