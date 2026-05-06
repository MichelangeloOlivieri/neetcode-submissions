class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        """
        1) Empty input; example on paper
        2) Map the two's, run multiple bfs's from the two's and updating adjacent one's
        """

        import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0

        while q and fresh_count > 0:
            
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    
                    if (new_row in range(m) and new_col in range(n) 
                        and grid[new_row][new_col] == 1):
                        
                        grid[new_row][new_col] = 2  
                        fresh_count -= 1            
                        q.append((new_row, new_col))
                    
            time += 1

        return time if fresh_count == 0 else -1

        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """

        
        