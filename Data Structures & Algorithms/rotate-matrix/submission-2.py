class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        if not matrix:
            return None
        
        m = len(matrix)

        for i in range(m // 2):
            for j in range(i, m - i - 1):
                temp_right = matrix[j][m - i - 1]
                matrix[j][m - i - 1] = matrix[i][j] # top row -> right column

                temp_bottom = matrix[m - i - 1][m - 1 - j]
                matrix[m - i - 1][m - 1 - j] = temp_right # right column -> bottom row

                temp_left = matrix[m - 1 - j][i]
                matrix[m - 1 - j][i] = temp_bottom # bottom row -> left column

                matrix[i][j] = temp_left # left column -> top row

        """
        3) Syntax and dry run: ok
        4) Time complexity O(n^2); space complexity O(1)
        """