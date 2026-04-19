class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Brute force solution

        if not nums:
            return 0

        max_prod = -float('inf')

        for i in range(len(nums)):
            aux = 1
            for j in range(i, len(nums)):
                aux = nums[j] * aux
                max_prod = max(aux, max_prod)

        return max_prod

        """
        4) Time complexity O(n^2); space complexity O(1)
        """



        
        