from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board or not board[0]:
            return False

        m = len(board)
        n = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if (r < 0 or r >= m or 
                c < 0 or c >= n or 
                board[r][c] != word[i] or
                board[r][c] == "#"):
                return False

            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
                   
            board[r][c] = word[i]
            return res

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
                        
        return False

        """
        Time complexity O(m * n * 3^p); space complexity O(p)
        """