class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # dfs solution

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
                row, col = q.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions: 
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row in range(m) and new_col in range(n) 
                        and grid[new_row][new_col] == "1" 
                        and (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    res += 1

        return res
        