class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if matrix is None:
            return []

        m = len(matrix)
        n = len(matrix[0])
        res = []

        l = 0
        r = min(m, n) - 1
        while l <= r:
            for j in range(l, n - l):
                res.append(matrix[l][j])
            for i in range(l + 1, m - l):
                res.append(matrix[i][n - 1 - l])
            # Stampiamo la riga in basso SOLO SE è fisicamente diversa da quella in alto
            if l < m - 1 - l:
                for j in range(n - 2 - l, - 1 + l, -1):
                    res.append(matrix[m - 1 - l][j])
            
            # Stampiamo la colonna di sinistra SOLO SE è fisicamente diversa da quella di destra
            if l < n - 1 - l:
                for i in range(m - 2 - l, l, -1):
                    res.append(matrix[i][l])
            l += 1
            r -= 1
    
        return res

        """
        Time complexity O(m * n); space complexity O(1)
        """

        