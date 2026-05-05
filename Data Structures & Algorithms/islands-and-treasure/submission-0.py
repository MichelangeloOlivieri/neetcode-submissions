class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        """
        1) Empty grid; example on paper; what if cell equidistant from two 0's? How
        is distance defined? Assuming Manhattan distance
        2) Bfs solution
        """

        if not grid:
            return

        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited:
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                if (row + dr in range(m) 
                and col + dc in range(n)
                and (row + dr, col + dc) not in visited
                and grid[row + dr][ col + dc] != -1):
                    grid[row + dr][ col + dc] = grid[row][col] + 1
                    visited.add((row + dr, col + dc))  
                    q.append((row + dr, col + dc)) 

        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """     