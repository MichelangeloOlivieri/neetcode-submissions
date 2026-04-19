class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if not nums or len(nums) == 1:
            return False

        total = 0
        for n in nums:
            total += n
        if total % 2 != 0:
            return False

        for i in range(len(nums) - 1):
            sum1 = nums[i]
            if sum1 == total/2:
                return True
            for j in range(i + 1, len(nums)):
                sum1 += nums[j]
                if sum1 == total/2:
                    return True
                if sum1 > total/2:
                    sum1 -= nums[j]
                    continue

        return False     