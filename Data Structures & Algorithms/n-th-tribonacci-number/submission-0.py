class Solution:
    def tribonacci(self, n: int) -> int:

        """
        1) n = 4 -> T_4 = T_3 + T_2 + T_1 = 4
        2) DP iterative solution
        """

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        a = 0
        b = 1
        c = 1
        i = 2

        while i < n:
            a, b, c = b, c, a + b + c
            i += 1

        return c

        """
        3) n = 4: a = 0, b = 1, c = 1, i = 2
        - a = 1, b = 1, c = 2, i = 3
        - a = 1, b = 2, c = 4, i = 4
        4) Time complexity O(n); space complexity O(1)
        """