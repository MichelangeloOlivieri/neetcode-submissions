class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_first_row = False

        # set the markers
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zero_first_row = True

        # put the zeroes inside the matrix
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # put the zeroes on the first column
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        # put the zeroes on the first row
        if zero_first_row:
            for c in range(n):
                matrix[0][c] = 0

"""
- Time complexity: O(m * n).
- Space complexity: O(1).
"""