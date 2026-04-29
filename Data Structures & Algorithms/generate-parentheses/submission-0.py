class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        1) No empty input; what is a "well-formed parentheses string"
        2) Dfs
        """

        res = []

        def dfs(i, j, cur):
            if i > n or j > n or i < j:
                return
            if i + j == 2*n:
                res.append(cur)
                return

            cur += "("
            dfs(i + 1, j, cur)
            cur = cur[:-1]
            cur += ")"
            dfs(i, j + 1, cur)

        dfs(0, 0, "")
        return res

        """
        3) Ok
        4) Time complexity O(n * 2^n); space complexity O(n)
        """
        