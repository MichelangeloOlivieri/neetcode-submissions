class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)
        res = 0

        for n in nums:
            freq[n] = max(freq[n], freq[k]) + 1
            res = max(res, freq[n] - freq[k])

        return freq[k] + res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """