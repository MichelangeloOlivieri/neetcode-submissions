class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        res = []
        to_string = {
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
            if i == len(digits):
                res.append(cur)
                return 

            digit = digits[i]
            for c in to_string[digit]:
                cur += c
                dfs(i + 1, cur)
                cur = cur[: -1]

        dfs(0, "")
        return res

"""
- Time complexity: O(n * 4**n), where n = len(digits).
- Space complexity: O(n).
"""