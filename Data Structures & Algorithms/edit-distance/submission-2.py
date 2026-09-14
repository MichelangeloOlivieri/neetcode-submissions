class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        1) word1 = "hello", word2 = "ihello" -> 1
                    ^                ^
        word1 = "ihello", word2 = "hello" -> 1
                 ^                 ^
        word1 = "iello", word2 = "hello" -> 1
                 ^                ^
        2) Dynamic Programming
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

            count = 0

            if word1[i] == word2[j]:
                count = dfs(i + 1, j + 1)
            else:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)
                count = min(insert, delete, replace)

            memo[(i, j)] = count
            return memo[(i, j)]

        return dfs(0, 0)

        """
        res = 2 + 
        word1 = "mon(ey)keys"
                        ^   
        word2 = "money"
                      ^
        """

        """
        - Time complexity O(m + n), where m = len(word1) and n = len(word2)
        - Space complexity O(m + n)
        """