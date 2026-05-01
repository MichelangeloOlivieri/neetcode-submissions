class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        """
        1) Example on paper
        2) Dfs
        """

        if not digits:
            return []

        res = []
        dictionary = {
            "2" : "abc", 
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, cur):
            if i > len(digits) - 1:
                res.append(cur)
                return

            for c in dictionary[digits[i]]:
                cur += c
                dfs(i + 1, cur)
                cur = cur[: -1] # adjusting horizontal control

        dfs(0, "")
        return res

        """
        3) Ok
        4) Time complexity O(n * 4^n), where n = len(digits); space complexity O(n)
        """