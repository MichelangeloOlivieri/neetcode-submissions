class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [["."] * n for _ in range(n)]

        columns = set()
        positive_diagonal = set()
        negative_diagonal = set()

        def dfs(r):
            if r > n - 1:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in columns or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                    continue

                board[r][c] = "Q"
                columns.add(c)
                positive_diagonal.add(r + c)
                negative_diagonal.add(r - c)

                dfs(r + 1)

                columns.remove(c)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res

        """
        Time complexity O(n!); space complexity O(n^2)
        """
