class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        """
        1) s = "neetcode"; wordDict = ["neet", "code", "ne"] -> ["neet code"]
        2) Backtracking, Linear 
        """

        if not wordDict:
            return [""]

        words = set(wordDict)
        res = []

        def backtrack(i: int, cur: str) -> None:
            if i == len(s):
                res.append(cur)

            for j in range(i, len(s)):
                word = s[i : j + 1]
                
                if word in words:
                    if j + 1 in range(len(s)):
                        backtrack(j + 1, cur + word + " ") 
                    else:
                        backtrack(j + 1, cur + word)        

        backtrack(0, "")
        return res

        """
        3) s = "aaaa", wordDict = ["a", "aa, "]
        4) 
        """