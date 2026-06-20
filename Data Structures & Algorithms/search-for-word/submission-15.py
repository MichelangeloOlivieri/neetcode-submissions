# board: 2D grid of characters
# word: string  
# move horizontally and vertically, not use same cell more than once when forming word

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        # run a dfs at every entry of the matrix

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        visited = set()

        def dfs(i, j, k):
            if k == len(word):
                return True
            if board[i][j] != word[k]:
                return False

            visited.add((i, j))
            for dr, dc in directions:
                if (0 <= i + dr < m and 
                    0 <= j + dc < n and
                    (i + dr, j + dc) not in visited):
                    if dfs(i + dr, j + dc, k + 1):
                        return True
                elif k == len(word) - 1:
                    return True

            visited.remove((i, j))
            return False        

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False