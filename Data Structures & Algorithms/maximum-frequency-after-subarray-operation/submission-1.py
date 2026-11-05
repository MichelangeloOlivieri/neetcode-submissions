class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        freq = defaultdict(int)
        max_gain = 0

        for n in nums:
            if freq[n] >= freq[k]:
                freq[n] += 1
            else:
                freq[n] = freq[k] + 1

            max_gain = max(max_gain, freq[n] - freq[k])

        return freq[k] + max_gain

        """
        nums = [10, 2, 10, 2, 2, 3], k = 10
                                 ^
        {10 : 2, 2 : 4, 3 : 3}
        max_gain = 2
        """

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """