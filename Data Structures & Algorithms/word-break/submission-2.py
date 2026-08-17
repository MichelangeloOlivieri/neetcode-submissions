class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        """
        1)  s = "neetcode", wordDict = ["neet", "code"] -> True
            s = "neetcode", wordDict = ["neet"] -> False
            s = "aab", wordDict = ["a", "a", "bc", "aa", "b"]
        2) DP, String
        """

        if not wordDict:
            return False

        words = set(wordDict)
        memo = {}

        def dfs(i: int) -> bool:
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for j in range(i, len(s)):
                word = s[i : j + 1]

                if word in words:
                    if dfs(j + 1):
                        return True
            
            memo[i] = False
            return False            

        return dfs(0)

        """
        3) s = "neetcode", wordDict = ["neet", "code"]
        -> i = 0:
        - j = 0, memo[0] = False
        - j = 1, memo[1] = False
        - ...
        - j = 3, word = "neet" 
        -> i = 4:
        - 
        """