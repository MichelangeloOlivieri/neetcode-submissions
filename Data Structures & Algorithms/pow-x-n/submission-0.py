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
                return self.myPow(x, n // 2) * self.myPow(x, n // 2)
            else:
                return self.myPow(x, (n - 1) // 2) * self.myPow(x, (n - 1) // 2) * x
        else:
            m = -n
            if n % 2 == 0:
                return self.myPow(1/x, m // 2) * self.myPow(1/x, m // 2)
            else:
                return self.myPow(1/x, (m - 1) // 2) * self.myPow(1/x, (m - 1) // 2) * 1/x
