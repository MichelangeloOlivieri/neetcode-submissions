class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not words:
            return []

        root = TrieNode()
        for word in words:
            root.addWord(word)

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        path = set()
        res = set()

        def dfs(r, c, node, word):
            if r not in range(m) or c not in range(n) or (r, c) in path or board[r][c] not in node.children:
                return

            path.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_word:
                res.add(word)
                node.is_word = False

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)
            path.remove((r, c))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(res)

        """
        Time complexity O(m * n * 4^max_len); space complexity O(len(words) * max_len)
        """



