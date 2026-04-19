class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # edge cases

        if not text1 or not text2:
            return 0

        if len(text1) == 1 and len(text2) == 1:
            return 1 if text1 == text2 else 0

        # dfs solution

        m = len(text1)
        n = len(text2)
        memo = {}

        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if i == m - 1 and j == n - 1:
                if text1[i] == text2[j]:
                    return 1
                else: 
                    return 0

            if i == m - 1:
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1
                    return memo[(i, j)]
                else:
                    memo[(i, j)] = dfs(i, j + 1)
                    return memo[(i, j)]
            if j == n - 1:
                if text1[i] == text2[j]:
                    memo[(i, j)] = 1
                    return memo[(i, j)]
                else: 
                    memo[(i, j)] = dfs(i + 1, j)
                    return memo[(i, j)] 

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
                return memo[(i, j)]

        return dfs(0, 0)

        """
        4) Time complexity O(m * n); space complexity O(m * n)
        """
        
        