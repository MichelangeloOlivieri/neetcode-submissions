class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        if not s:
            return 0

        memo = {}

        def dp(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) in memo:
                return memo[(l, r)]
            if s[l] == s[r]:
                memo[(l, r)] = 2 + dp(l + 1, r - 1)
                return memo[(l, r)]
            
            memo[(l, r)] = max(dp(l + 1, r), dp(l, r - 1))
            return memo[(l, r)]

        return dp(0, len(s) - 1) 

        """
        Time complexity O(n^2), where n = len(s); space complexity O(n^2)
        """       