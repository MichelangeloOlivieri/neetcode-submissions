class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(i, j, cur):
            if i > n or j > n or i < j:
                return
            if i + j == 2 * n:
                res.append(cur)
                return

            cur += "("
            dfs(i + 1, j, cur)
            cur = cur[: -1]
            cur += ")"
            dfs(i, j + 1, cur)

            return

        dfs(0, 0, "")
        return res

        """
        - Time complexity O(4^n/sqrt(n))
        - Space complexity O(n)
        """
        