class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1

        for c in s_count:
            if s_count[c] != t_count[c]:
                return False

        return True

        """
        - Time complexity O(n), where n = len(s) = len(t)
        - Space complexity O(1)
        """        