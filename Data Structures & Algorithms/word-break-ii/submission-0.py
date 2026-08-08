class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)
        memo = {}

        def backtrack(i):
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            sentences = []

            for j in range(i + 1, len(s) + 1):
                word = s[i : j]

                if word in word_set:
                    suffix_sentences = backtrack(j)

                    for suffix in suffix_sentences:
                        if suffix == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + suffix)

            memo[i] = sentences
            return memo[i]            

        return backtrack(0)

        """
        Time complexity O(N^2 + 2^N + V), where N = len(s) and V is the total number of characters of all valid sentences; space complexity O(N * 2^N)
        """