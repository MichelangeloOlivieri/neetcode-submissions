class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # dp solution

        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            for t in dp.copy():
                if t + nums[i] == target:
                    return True
                dp.add(t + nums[i])

        return False



        