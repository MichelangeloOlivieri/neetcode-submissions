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
        4) The number of well-formed parentheses strings that you can generate with
        n pairs is given by Catalan's number, that grows like 4^n/(n * sqrt(n));
        since "res.append(cur)" costs O(n), we have a time complexity equal to
        O(4^n/sqrt(n)); the space complexity is O(n) given by the recursion stack
        """
        