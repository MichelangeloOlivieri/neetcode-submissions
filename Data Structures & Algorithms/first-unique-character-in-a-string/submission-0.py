class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n = len(s)
        freq = {}

        for i in range(n):
            if s[i] not in freq:
                freq[s[i]] = [1, i]
            else:
                freq[s[i]] = [1 + freq[s[i]][0], i]

        for i in range(n):
            if freq[s[i]][0] == 1:
                return freq[s[i]][1]

        return -1

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(1)
        """