class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word: str) -> None:
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
            root.insert(word)

        m = len(board)
        n = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        path = set()
        res = []

        def dfs(r, c, node, word):
            if (r < 0 or r >= m or 
                c < 0 or c >= n or 
                (r, c) in path or
                board[r][c] not in node.children):
                return

            path.add((r, c))
            letter = board[r][c]
            word += letter
            node = node.children[letter]
            if node.is_word:
                res.append(word)
                node.is_word = False

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)
            path.remove((r, c))

        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return res

        """
        - Time complexity O(m * n * 3^max_len)
        - Space complexity O(len(words) * max_len)
        """



