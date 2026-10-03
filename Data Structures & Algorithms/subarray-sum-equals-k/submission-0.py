class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
        1) [1, 1, 2, 1], k = 4 -> 2
            ^
        2) Prefix Sum
        """

        if not nums:
            return 0

        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0

        for n in nums:
            curr += n
            if curr - k in prefix:
                res += prefix[curr - k]
            prefix[curr] += 1

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """