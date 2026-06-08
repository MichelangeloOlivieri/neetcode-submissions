class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s2) + len(s1):
            return False

        memo = {}

        def dfs(i, j):
            if i == len(s1):
                return s3[i + j:] == s2[j:]
            if j == len(s2):
                return s3[i + j:] == s1[i:]
            if (i, j) in memo:
                return memo[(i, j)]

            if s3[i + j] == s1[i] and s3[i + j] == s2[j]:
                memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
                return memo[(i, j)]
            elif s3[i + j] == s1[i]:
                memo[(i, j)] = dfs(i + 1, j) 
                return memo[(i, j)] 
            elif s3[i + j] == s2[j]:
                memo[(i, j)] = dfs(i, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = False
                return memo[(i, j)]

        return dfs(0, 0)
            

        