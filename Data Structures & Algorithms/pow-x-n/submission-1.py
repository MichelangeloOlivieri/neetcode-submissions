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

        if n > 0:
            if n % 2 == 0:
                first = self.myPow(x, n // 2)
                second = first
                return first * second
            else:
                first = self.myPow(x, (n - 1) // 2)
                second = first
                return first * second * x
        else:
            m = -n
            if n % 2 == 0:
                first = self.myPow(1/x, m // 2)
                second = first
                return first * second
            else:
                first = self.myPow(1/x, (m - 1) // 2)
                second = first
                return first * second * 1/x

        """
        3) Ok
        4) Time complexity O(log(n)); space complexity O(log(n))
        """