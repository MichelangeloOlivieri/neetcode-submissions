class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        l = 0
        r = len(nums) - 1
        res = []

        while l <= r:
            first = nums[l]**2
            second = nums[r]**2
            if first > second:
                res.append(first)
                l += 1
            else:
                res.append(second)
                r -= 1

        res.reverse()
        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n) (for the array result)
        """