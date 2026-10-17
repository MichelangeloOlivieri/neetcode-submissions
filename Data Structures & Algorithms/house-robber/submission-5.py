class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        second_to_last = 0
        last = 0
        curr = 0

        for i in range(len(nums)):
            curr = max(second_to_last + nums[i], last)
            second_to_last = last
            last = curr
            
        return curr        