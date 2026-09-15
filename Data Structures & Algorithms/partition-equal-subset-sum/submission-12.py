class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            for t in dp.copy():
                if t + nums[i] == target:
                    return True
                dp.add(t + nums[i])

        return False

        """
        - Time complexity O(n * target), where n = len(nums)
        - Space complexity O(target)
        """