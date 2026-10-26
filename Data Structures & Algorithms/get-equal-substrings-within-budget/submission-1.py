class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        if not s or not t or len(s) != len(t):
            return 0

        n = len(s)
        def cost(i):
            return abs(ord(s[i]) - ord(t[i]))

        l = 0
        r = 0
        curr_cost = 0
        res = 0

        while l < n and r < n:
            curr_cost += cost(r)
            while l < n and curr_cost > maxCost:
                curr_cost -= cost(l)
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res

        """
        - Time complexity O(n), where n = len(s) = len(t)
        - Space complexity O(n)
        """

        