class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        1) Empty input; example seen
        2) Dfs
        """

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        memo = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert = dfs(i, j + 1)
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                memo[(i, j)] = 1 + min(insert, delete, replace)

            return memo[(i, j)]

        return dfs(0, 0)

        """
        3) Ok
        4) Time complexity O(m * n), where m = len(word1) and n = len(word2); space 
        complexity O(m * n)
        """        