class Solution:
    from typing import List
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # soluzione mia (follow-up question)

        res = []
        left_products = [1] * len(nums)
        right_products = [1] * len(nums) 

        left_products[0] = 1
        for i in range(1, len(nums)):
            left_products[i] = left_products[i - 1] * nums[i - 1] 

        right_products[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1] 
        
        for i in range(len(nums)):
            res.append(left_products[i] * right_products[i])

        return res

        """
        Dry run: - nums = [1, 2, 4, 6]; len(nums) = 4
        - i = 1: left_products[1] = 1; i = 2: left_products[2] = 2; 
        
        = [1, 1, 2, 8]; right_products = [48, 48, 24, 6]
        - res = [ok]
        """