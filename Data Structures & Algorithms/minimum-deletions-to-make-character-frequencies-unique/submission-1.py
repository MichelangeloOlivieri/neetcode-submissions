class Solution:
    def minDeletions(self, s: str) -> int:
        
        """
        1) s = "aaabc"
        buckets = [0, 2, 0, 1]
        """

        if not s:
            return 0
        
        # frequency
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        # buckets
        max_freq = 0
        for c in freq:
            max_freq = max(max_freq, freq[c])

        buckets = [0] * (max_freq + 1)
        for c in freq:
            buckets[freq[c]] += 1

        # save the indexes of zeroes
        zeroes = []
        for i in range(1, max_freq + 1):
            if buckets[i] == 0:
                zeroes.append(i)

        # result
        res = 0

        for i in range(max_freq, 0, -1):
            while zeroes and i <= zeroes[-1]:
                zeroes.pop()
            while buckets[i] > 1:
                if not zeroes:
                    res += i
                else:
                    next_index = zeroes.pop()
                    res += i - next_index
                buckets[i] -= 1


        return res

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(n).
"""