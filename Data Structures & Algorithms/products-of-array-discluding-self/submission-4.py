class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        Use left- and right-products trick
        """

        res = [1] * len(nums)

        left_products = [1] * len(nums)
        left_products[1] = nums[0]
        for i in range(2, len(nums)):
            left_products[i] = nums[i - 1] * left_products[i - 1]

        right_products = [1] * len(nums)
        right_products[-2] = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            right_products[i] = nums[i + 1] * right_products[i + 1]

        for i in range(len(nums)):
            res[i] = left_products[i] * right_products[i]

        return res        