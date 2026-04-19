class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        """
        1) Empty input
        2) 
        """

        if not nums:
            return 0

        pool1 = set([i for i in range(0, len(nums) + 1)])
        pool2 = set(nums)
        for n in pool1:
            if n not in pool2:
                return n