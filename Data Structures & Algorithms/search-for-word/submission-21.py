class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c, k):
            if k == len(word):
                return True
            if (r not in range(m) or
                c not in range(n) or
                board[r][c] == None or
                board[r][c] != word[k]):
                return False

            temp = board[r][c]
            board[r][c] = None
            for dr, dc in directions:
                if dfs(r + dr, c + dc, k + 1):
                    return True

            board[r][c] = temp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
        