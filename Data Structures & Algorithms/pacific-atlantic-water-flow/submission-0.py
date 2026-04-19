class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # dfs solution

        m = len(heights)
        n = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prev_height):
            if (r, c) in visit or r < 0 or c < 0 or r == m or c == n or heights[r][c] < prev_height:
                return

            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions: 
                dfs(r + dr, c + dc, visit, heights[r][c])

        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])
        
        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])

        res = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append((i, j))

        return res