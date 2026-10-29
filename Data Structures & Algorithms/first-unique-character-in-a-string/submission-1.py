class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n = len(s)
        freq = {}

        for i in range(n):
            if s[i] not in freq:
                freq[s[i]] = [1, i]
            else:
                freq[s[i]][0] += 1

        res = float('inf')

        for c in freq:
            if freq[c][0] == 1:
                res = min(res, freq[c][1])

        return res if res != float('inf') else -1

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(1)
        """