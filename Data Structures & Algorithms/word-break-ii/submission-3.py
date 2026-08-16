class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if not wordDict:
            return []

        words = set(wordDict)
        memo = {}

        def backtrack(i: int) -> List[str]:
            if i in memo:
                return memo[i]

            if i == len(s):
                return [""]

            res = []
            for j in range(i, len(s)):
                word = s[i : j + 1]

                if word in words:
                    subsequent_words = backtrack(j + 1)

                    for tail in subsequent_words:
                        if tail:
                            res.append(word + " " + tail)
                        else:
                            res.append(word)

            memo[i] = res
            return memo[i]

        return backtrack(0)       