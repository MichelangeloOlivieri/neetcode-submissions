class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word:
            return True
        if not board:
            return False

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()

        def dfs(i, j, k):
            if k == len(word) - 1 and board[i][j] == word[k]:
                return True
            if board[i][j] != word[k]:
                return False

            if board[i][j] == word[k]:
                visited.add((i, j))
                for dr, dc in directions:
                    if (i + dr in range(m) and 
                        j + dc in range(n) and 
                        (i + dr, j + dc) not in visited and
                        dfs(i + dr, j + dc, k + 1)):
                        return True

            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False        