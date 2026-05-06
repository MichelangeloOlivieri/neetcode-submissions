class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        1) Empty input; example on paper
        2) Map the two's, run multiple bfs's from the two's and updating adjacent one's
        """

        m = len(grid)
        n = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = collections.deque()
        visited = set()
        time = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                    grid[i][j] = 0

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                if (row + dr in range(m)
                and col + dc in range(n)
                and (row + dr, col + dc) not in visited
                and grid[row + dr][col + dc] != 0):
                    q.append((row + dr, col + dc))
                    visited.add((row + dr, col + dc))
                    grid[row + dr][col + dc] = grid[row][col] + 1
                    time = max(time, grid[row + dr][ col + dc])

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visited:
                    return -1

        return time

        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """

        
        