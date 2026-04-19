class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        """
        1) Empty inputs: what if one is empty, or even both are? Example: input text1 = "abacd", 
        text2 = "a#cs" -> output = 2; correct?
        2) - Solution 1: check all subsequences of both strings, put them in sets and if there is
        a match return longest match -> time complexity at least O(2^n) to find all subsequences
        - Solution 2: bidimensional dp solution?
        """

        # edge cases

        if not text1 or not text2:
            return 0

        if len(text1) == 1 and len(text2) == 1:
            return 1 if text1 == text2 else 0

        # dp implementation
        
        seen1 = set()
        seen2 = set()
        m = len(text1)
        n = len(text2)
        dp = [[0] * n for _ in range(m)]

        if text1[m - 1] == text2[n - 1]:
            dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            if text2[n - 1] == text1[i] or text2[n - 1] in seen1:
                seen1.add(text1[i])
                dp[i][n - 1] = 1
        for j in range(n - 1, -1, -1):
            if text1[m - 1] == text2[j] or text1[m - 1] in seen2:
                seen2.add(text2[j])
                dp[m - 1][j] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

        """
        3) Syntax and dry run: seems ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """
                



