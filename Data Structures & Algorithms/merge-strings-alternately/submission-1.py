class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

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
        - Time complexity O(m + n), where m = len(word1) and n = len(word2)
        - Space complexity O(m + n) for output result
        """