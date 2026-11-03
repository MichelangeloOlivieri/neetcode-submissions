class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        n = len(nums)
        l = 0
        r = n - 1
        res = [0] * n
        i = n - 1

        while l <= r:
            first = nums[l]**2
            second = nums[r]**2
            if first > second:
                res[i] = first
                l += 1
            else:
                res[i] = second
                r -= 1

            i -= 1

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n) (for the array result)
        """