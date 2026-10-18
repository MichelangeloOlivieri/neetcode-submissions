from collections import defaultdict

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])

        if m < 3 or n < 3:
            return 0

        def helper(r, c):
            if r + 2 >= m or c + 2 >= n:
                return False

            values = set()
            row_sum = defaultdict(int)
            column_sum = defaultdict(int)
            diagonal_sum = defaultdict(int)

            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if grid[i][j] <= 0 or grid[i][j] > 9:
                        return False

                    values.add(grid[i][j])
                    row_sum[i] += grid[i][j]
                    column_sum[j] += grid[i][j]
                    if (i - r) == (j - c):
                        diagonal_sum[1] += grid[i][j]
                    if (i - r) + (j - c) == 2:
                        diagonal_sum[-1] += grid[i][j]

            values_condition = (len(values) == 9)
            rows_condition = (
                row_sum[r] == row_sum[r + 1] == row_sum[r + 2]
            )
            columns_condition = (
                column_sum[c] == column_sum[c + 1] == column_sum[c + 2]
            )
            diagonals_condition = (
                diagonal_sum[1] == diagonal_sum[-1]
            )
            common_value = (row_sum[r] == column_sum[c] == diagonal_sum[1])

            return (values_condition and 
                rows_condition and 
                columns_condition and 
                diagonals_condition and
                common_value
            )

        res = 0

        for i in range(m):
            for j in range(n):
                if helper(i, j):
                    res += 1

        return res
