class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        """
        1) s = "neetcode", wordDict = ["neet", "code"] -> True
        2) DP, String
        """

        if s == "" or not wordDict:
            return False

        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in words:
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]

        """
        3) 
        4) Time complexity O(n^3), space complexity O(n)
        """