class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res_index = 0
        res_length = -float('inf')

        for i in range(len(s)):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_length:
                    res_index = l
                    res_length = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_length:
                    res_index = l
                    res_length = r - l + 1
                l -= 1
                r += 1

        return s[res_index : res_index + res_length]

        """
        - Time complexity O(n^2), where n = len(s)
        - Space complexity O(n)
        """