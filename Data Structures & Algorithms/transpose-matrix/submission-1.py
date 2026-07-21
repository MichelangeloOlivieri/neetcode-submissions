class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix:
            return [[]]

        m = len(matrix)
        n = len(matrix[0])
        res = [[] for j in range(n)]

        for i in range(m):
            for j in range(n):
                res[j].append(matrix[i][j])

        return res
        
        """
        Time complexity O(m * n); space complexity O(m * n)
        """