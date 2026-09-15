class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid or not grid[0]:
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
            r, c = q.popleft()
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if (new_r >= 0 and new_r < m and
                    new_c >= 0 and new_c < n and
                    grid[new_r][new_c] == 2147483647):
                    grid[new_r][new_c] = grid[r][c] + 1
                    q.append((new_r, new_c))

        """
        - Time complexity O(m * n)
        - Space complexity O(m * n)
        """     