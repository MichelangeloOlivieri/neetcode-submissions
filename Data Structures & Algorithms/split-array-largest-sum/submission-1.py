class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def can_split(largest):
            subarrays_count = 1
            current_sum = 0

            for n in nums:
                current_sum += n
                if current_sum > largest:
                    subarrays_count += 1
                    if subarrays_count > k:
                        return False
                    current_sum = n

            return True

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2

            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

        """
        - Time complexity O(N * log(S)), where N = len(nums) and S = sum(nums) - max(nums)
        - Space complexity O(1)
        """       