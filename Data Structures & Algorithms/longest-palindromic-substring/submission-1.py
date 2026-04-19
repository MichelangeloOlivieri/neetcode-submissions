class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # mio tentativo

        """
        1) Which characters are allowed? Are upper-case letters allowed? empty inputs
        2) - Solution 1: define a helper function and check all the substrings to find longest 
        palindromic one
        - Solution 2: dynamic programming
        """

        if not s:
            return None

        max_length = -float('inf')
        res_id = [-1, -1]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindromic(s[i: j + 1]) and len(s[i: j + 1]) > max_length:
                    max_length = len(s[i: j + 1])
                    res_id = [i, j]

        i = res_id[0]
        j = res_id[1]

        return s[i: j + 1] if max_length > -float('inf') else None
        
    def isPalindromic(self, string):

        if not string:
            return None

        for i in range(len(string)):
            if string[i] != string[len(string) - 1 - i]:
                return False
        return True

        """
        3) Dry run: ok
        4) Time complexity O(n^3); space complexity O(n) (slicing)
        """


