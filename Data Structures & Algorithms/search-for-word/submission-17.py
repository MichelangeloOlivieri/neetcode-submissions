class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # double for loop + dfs with visited set/marker

        if not board:
            return False

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True
            if board[r][c] != word[k]:
                return False

            visited.add((r, c))
            for (dr, dc) in directions:
                new_row = r + dr
                new_col = c + dc
                if (0 <= new_row < m and
                    0 <= new_col < n and
                    (new_row, new_col) not in visited):
                        if dfs(new_row, new_col, k + 1):
                            return True
                if k == len(word) - 1:
                    return True

            visited.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
        