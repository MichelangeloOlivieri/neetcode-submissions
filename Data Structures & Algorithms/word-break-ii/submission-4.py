class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]

            sentences = []

            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in word_set:
                    suffix_sentences = dfs(j + 1)
                    for suffix in suffix_sentences:
                        if suffix == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + suffix)

            memo[i] = sentences
            return memo[i]            

        return dfs(0)

        """
        - Time complexity O(n * 2^n), where n = len(s)
        - Space complexity O(n * 2^n)
        """