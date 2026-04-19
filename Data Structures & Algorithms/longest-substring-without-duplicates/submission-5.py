class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        l, r = 0, 0
        count = {}
        res = -float('inf')

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            while max(count.values()) >= 2:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res

        