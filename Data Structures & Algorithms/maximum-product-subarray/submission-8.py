class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = -float('inf')
        curr_max = 1
        curr_min = 1

        for n in nums:
            if n != 0:
                temp = curr_max
                curr_max = max(curr_max * n, curr_min * n, n)
                curr_min = min(temp * n, curr_min * n, n)
                res = max(res, curr_max)
            else:
                res = max(res, 0)
                curr_max = 1 
                curr_min = 1

        return res