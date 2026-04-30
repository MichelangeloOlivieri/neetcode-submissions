class Solution:
    def partition(self, s: str) -> List[List[str]]:

        """
        1) No empty input; example (seen)
        2) Dfs
        """

        res = []
        part = []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return res    

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    """
    3) Ok
    4) Time complexity O(n * 2^n); space complexity O(n)
    """