class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        """
        1) nums = [1, 2, 3, 2, 1, 1], target = 5 -> [[1, 2, 1, 1]]
        2) Backtracking -> n^4
        Two Pointers -> n^3
        """

        if not nums:
            return []

        n = len(nums)
        nums.sort()
        res = []
        i = 0

        while i < n:
            j = n - 1
            while j > i + 2:
                l = i + 1
                r = j - 1

                while l < r:
                    amount = nums[i] + nums[l] + nums[r] + nums[j]
                    if amount < target:
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                           l += 1
                    elif amount > target:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                           r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r], nums[j]])
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                           l += 1

                j -= 1
                while j >= 0 and nums[j] == nums[j + 1]:
                    j -= 1

            i += 1
            while i < n and nums[i - 1] == nums[i]:
                i += 1

        return res

        """
        - Time complexity O(n^3), where n = n
        - Space complexity O(n) (for TimSort) 
        """
