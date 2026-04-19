class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = set()
        res = 0

        def bfs(i, j):
            visited.add((i, j))
            q = collections.deque()
            q.append((i, j))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if r + dr in range(m) and c + dc in range(n) and (r + dr, c + dc) not in visited and grid[r + dr][c + dc] == '1':
                        visited.add((r + dr, c + dc))
                        q.append((r + dr, c + dc))                        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    res += 1

        return res        