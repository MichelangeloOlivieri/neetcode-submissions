class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return 0

        curr = None
        count = 0

        for n in nums:
            if count == 0:
                curr = n
            count += (1 if curr == n else -1)

        return curr

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """