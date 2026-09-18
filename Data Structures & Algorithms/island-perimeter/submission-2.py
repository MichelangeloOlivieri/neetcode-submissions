class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        res = 0

        def bfs(i, j):
            nonlocal res
            q = deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                res += 4
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r >= 0 and new_r < m and
                        new_c >= 0 and new_c < n and
                        grid[new_r][new_c] == 1):
                            res -= 1
                            if (new_r, new_c) not in visited:
                                q.append((new_r, new_c))
                                visited.add((new_r, new_c))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    return res

        """
        - Time complexity O(m * n), where m = len(grid) and n = len(grid[0])
        - Space complexity O(m * n)
        """            