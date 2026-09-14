class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        """
        1) s = "aneetcoder", dictionary = ["ane", "neet", "code"] -> 2
                 ^    
        2) Trie
        """

        words = set(dictionary)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)

        """
        - Time complexity O(2^n), where n = len(s)
        - Space complexity O(n + m), where m total length dictionary
        """