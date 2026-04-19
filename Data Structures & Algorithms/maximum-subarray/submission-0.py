class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        1) Empty input; example: nums = [2, -3, 1, 3] -> 4
        2) - Solution 1: a brute force approch would be to check each possible subarray
        to find the max sum (can be done with two indexes)
        - Solution 2: two pointers keeping track of what intervals give positive sums
        and returning the max
        """

        if not nums:
            return 0

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub          

        """
        3) Syntax and dry run: ok
        4) Time complexity O(n); space complexity O(1)
        """

        