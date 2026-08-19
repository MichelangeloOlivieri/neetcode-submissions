class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        """
        1) word1 = "neet", word2 = "code" -> "nceoedte"
        2) String, Two Pointers
        """

        i = 0
        j = 0
        l = min(len(word1), len(word2))
        res = []

        while i < l and j < l:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        while i < len(word1):
            res.append(word1[i])
            i += 1

        while j < len(word2):
            res.append(word2[j])
            j += 1

        return "".join(res)

        """
        3) word1 = "hello", word2 = "world!!!", l = 5
        - i = 0, j = 0: res = ["h", "w"]
        - i = 1, j = 1: res = ["h", "w", "e", "o"]
        - i = 2, j = 2: res = ["h", "w", "e", "o", "l", "r"]
        - ...
        - i = 4, j = 4: res = ["h", "w", "e", "o", "l", "r", "l", "l", "o", "d"]
        - i = 5, j = 5: res = ["h", "w", "e", "o", "l", "r", "l", "l", "o", "d", "!", "!", "!"]
        4) Time complexity O(m + n), where m = len(word1), n = len(word2); space complexity O(m + n)
        """