class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        # expand the grid
        n = len(grid)
        m = 3 * n
        blocked = [[False] * m for _ in range(m)]

        # fill the diagonals
        for r, row in enumerate(grid):
            for c, char in enumerate(row):
                if char != " ":
                    for k in range(3):
                        blocked[3 * r + k][3 * c + (2 - k if char == "/" else k)] = True

        # explore new grid
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        answer = 0
        for r in range(m):
            for c in range(m):
                if blocked[r][c]: # diagonal found
                    continue
                answer += 1
                blocked[r][c] = True
                # iterative dfs
                stack = [(r, c)]
                while stack:
                    row, col = stack.pop()
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc
                        if (0 <= new_row < m and 
                            0 <= new_col < m and 
                            not blocked[new_row][new_col]):
                                blocked[new_row][new_col] = True
                                stack.append((new_row, new_col))
        return answer

        """
        - Time complexity O(n**2), where n = len(grid)
        - Space complexity O(n**2)
        """