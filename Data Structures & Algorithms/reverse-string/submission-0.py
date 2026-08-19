class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        """
        1) s = ["n", "e", "a", "t"] -> s = ["t", "e", "e", "n"]
        2) Array, Two Pointers
        """

        if not s:
            return

        l = 0
        r = len(s) - 1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1

        """
        3)  s = ["n", "e", "c", "a", "t"]
        - l = 0, r = 3: s = ["t", "a", "c", "e", "n"]
        4) Time complexity O(n), where n = len(s); space complexity O(1)
        """