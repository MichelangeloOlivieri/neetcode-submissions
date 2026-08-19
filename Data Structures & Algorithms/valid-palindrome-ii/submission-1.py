class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        """
        1) s = "abaacaaa" -> True
        2) String, Two Pointers
        """

        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                skip_left = s[l + 1 : r + 1]
                skip_right = s[l : r]
                return (skip_left == skip_left[::-1] or skip_right == skip_right[::-1])
            else:
                l += 1
                r -= 1

        return True

        """
        3) s = "lcupu upucul"
        - l = 0, r = 7
        - l = 1, r = 6
        - l = 2, r = 6
        s = "aabaca"
        - l = 0, r = 5
        - l = 1, r = 2
        4) Time complexity O(n), where n = len(s); space complexity O(1)
        """