class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum_mat = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += matrix[i][j]
                above = self.sum_mat[i][j + 1]
                self.sum_mat[i + 1][j + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1

        top_left = self.sum_mat[r1 - 1][c1 - 1]
        above = self.sum_mat[r1 - 1][c2]
        bottom_right = self.sum_mat[r2][c2]
        left = self.sum_mat[r2][c1 - 1]

        return bottom_right - above - left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)