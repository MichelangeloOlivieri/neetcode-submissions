class Solution:
    def reverse(self, x: int) -> int:

        MAX_INT_DIV_10 = 214748364  # max_int is 2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        while x != 0:
            pop = x % 10
            x = x // 10

            if res > MAX_INT_DIV_10 or (res == MAX_INT_DIV_10 and pop > 7):
                return 0
            res = (res * 10) + pop
            
        return res * sign

        """
        - Time complexity O(1)
        - Space complexity O(1)
        """