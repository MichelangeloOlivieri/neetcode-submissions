class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # dfs solution
        
        word_set = set(wordDict)
        memo = set()

        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return False

            for end in range(start + 1, len(s) + 1):
                if s[start : end] in word_set and dfs(end):
                    return True

            memo.add(start)
            return False

        return dfs(0)

        """
        Time complexity O(2^n) where n = len(s); space complexity O(n)
        """