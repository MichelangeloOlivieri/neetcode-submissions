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
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]

        curr.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        if not dictionary:
            return len(s)

        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        memo = {}

        def dfs(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]

            leave = 1 + dfs(i + 1)
            take = float('inf')

            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]
                if curr.is_word:
                    take = min(take, dfs(j + 1))
            
            memo[i] = min(leave, take)
            return memo[i]

        return dfs(0)

        """
        - Time complexity O(n^2 + m), where n = len(s) and m is the total number of characters in dictionary
        - Space complexity O(n + m)
        """