class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0

        freq = defaultdict(int)
        res = 0
        l = 0
        
        for r in range(len(nums)):
            freq[nums[r]] += 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            length = r - l + 1
            res = max(res, length)

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """