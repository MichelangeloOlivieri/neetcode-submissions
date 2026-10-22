class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        skip_first = self.house_robber_solver(nums[1:])
        rob_first = self.house_robber_solver(nums[:-1])

        return max(rob_first, skip_first)

    def house_robber_solver(self, arr):
        rob1, rob2 = 0, 0
        
        for n in arr:
            new_rob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = new_rob
    
        return rob2
        
        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """


        