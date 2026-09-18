class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        res = 0

        def bfs(i, j):
            area = 0         
            visited.add((i, j))
            q = collections.deque()
            q.append((i, j))

            while q:
                row, col = q.pop()
                area += 1
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row >= 0 and new_row < m and 
                        new_col >= 0 and new_col < n and 
                        grid[new_row][new_col] == 1 and 
                        (new_row, new_col) not in visited):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col)) 

            return area           

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    res = max(res, bfs(i, j))          

        return res
        
        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """