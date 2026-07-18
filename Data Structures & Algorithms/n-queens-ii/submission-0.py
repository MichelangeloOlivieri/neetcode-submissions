class Solution:
    def totalNQueens(self, n: int) -> int:

        if n == 0:
            return 0

        res = 0
        columns = set()
        diagonals = set()
        antidiagonals = set()

        def backtrack(i):
            if i == n:
                nonlocal res
                res += 1
                return res

            for j in range(n):
                if j in columns or i - j in diagonals or i + j in antidiagonals:
                    continue
                columns.add(j)
                diagonals.add(i - j)
                antidiagonals.add(i + j)
                backtrack(i + 1)
                columns.remove(j)
                diagonals.remove(i - j)
                antidiagonals.remove(i + j)                

        backtrack(0)
        return res    