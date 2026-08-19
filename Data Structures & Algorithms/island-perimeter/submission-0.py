class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        """
        1) grid = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 1, 1]] -> 18
        2) Graph, BFS
        """

        if not grid:
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
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r not in range(m):
                        res += 1
                    elif new_c not in range(n):
                        res += 1
                    elif grid[new_r][new_c] == 0:
                        res += 1
                    elif (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    return res

        """
        3) m = 4, n = 4, visited = {}
        -> i = 0, j = 0:
        - q = {(0, 0)}; res = 2
        - q = {(1, 0), (0, 1)}; res = 7
        - q = {(2, 0)}; res = 9
        - q = {(2, 1)}; res = 11
        - q = {(2, 2)}; res = 13
        - q = {(3, 2)}; res = 15
        - q = {(3, 3)}; res = 18
        4) Time complexity O(m * n); space complexity O(m * n)
        """            