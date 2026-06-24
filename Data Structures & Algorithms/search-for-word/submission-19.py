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
            if (r not in range(m) or
                c not in range(n) or
                (r, c) in visited or
                board[r][c] != word[k]):
                return False

            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, k + 1):
                    return True
            visited.remove((r, c))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
        