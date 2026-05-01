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
            "2" : {"a", "b", "c"}, 
            "3" : {"d", "e", "f"},
            "4" : {"g", "h", "i"},
            "5" : {"j", "k", "l"},
            "6" : {"m", "n", "o"},
            "7" : {"p", "q", "r", "s"},
            "8" : {"t", "u", "v"},
            "9" : {"w", "x", "y", "z"}
        }

        def dfs(i, cur):
            if i > len(digits) - 1:
                res.append(cur)
                return

            for c in dictionary[digits[i]]:
                cur += c
                dfs(i + 1, cur)
                cur = cur[: -1]

        dfs(0, "")
        return res

        """
        3) Ok
        4) Time complexity O(n * 4^n), where n = len(digits); space complexity O(n)
        """