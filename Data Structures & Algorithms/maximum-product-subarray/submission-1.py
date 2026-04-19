class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """
        1) Empty input
        2) - Solution 1: double index to calculate each single product and return the max
        - Solution 2:
        """

        if not nums:
            return 0

        max_prod = -float('inf')

        for i in range(len(nums)):
            aux = 1
            for j in range(i, len(nums)):
                aux = nums[j] * aux
                max_prod = max(aux, max_prod)

        return max_prod



        
        