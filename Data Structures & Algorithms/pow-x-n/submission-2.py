class Solution:
    def myPow(self, x: float, n: int) -> float:

        """
        1) Problem well defined
        2) Divide n by 2 every time
        """

        if n == 0:
            return 1
        if n == 1:
            return x

        if n < 0:
            n = -n
            x = 1/x

        res = 1
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2

        return res

        """
        3) Ok
        4) Time complexity O(log(n)); space complexity O(log(n))
        """