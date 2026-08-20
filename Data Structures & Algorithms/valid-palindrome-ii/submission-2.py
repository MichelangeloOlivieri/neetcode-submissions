class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                remove_left = s[l + 1 : r + 1]
                remove_right = s[l : r]
                return (remove_left == remove_left[:: -1] or 
                    remove_right == remove_right[:: -1])
            else:
                l += 1
                r -= 1

        return True