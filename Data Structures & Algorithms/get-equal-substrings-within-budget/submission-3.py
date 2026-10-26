class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        if not s or not t or len(s) != len(t):
            return 0

        n = len(s)
        l = 0
        curr_cost = 0
        res = 0

        for r in range(n):
            curr_cost += abs(ord(s[r]) - ord(t[r]))
            while l < n and curr_cost > maxCost:
                curr_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            res = max(res, r - l + 1)

        return res

        """
        - Time complexity O(n), where n = len(s) = len(t)
        - Space complexity O(1)
        """

        