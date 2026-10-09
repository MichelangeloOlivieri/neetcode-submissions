class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        res = 0

        def backtrack(i, xor):
            nonlocal res
            if i == len(nums):
                res += xor
                return

            backtrack(i + 1, xor ^ nums[i])
            backtrack(i + 1, xor)

        backtrack(0, 0)
        return res

        """
        - Time complexity O(2**n), where n = len(nums)
        - Space complexity O(n)
        """