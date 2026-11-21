class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        
        prev = 1
        curr = 2

        for i in range(3, n + 1):
            temp = prev
            prev = curr
            curr = curr + temp

        return curr

"""
- Time complexity: O(n).
- Space complexity: O(1).
"""