class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = defaultdict(int)
        res = 0
        l, r = 0, 0

        for r in range(len(s)):
            count[s[r]] += 1

            to_be_replaced = r - l + 1 - max(count.values())
            if to_be_replaced > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(1)
        """

        