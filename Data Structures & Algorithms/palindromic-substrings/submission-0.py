class Solution:
    def countSubstrings(self, s: str) -> int:

        # mio tentativo

        """
        1) Which characters are allowed? Are upper-case letters allowed? empty inputs?
        2) Same solution as before with two pointers
        """

        if not s:
            return None

        res = 0
        for i in range(len(s)):

            # odd case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even case
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

        """
        3) Syntax and dry run: - s = "abba", res = 0;
        - res = etc seems good
        4) Time complexity O(n^2); space complexity O(1)
        """