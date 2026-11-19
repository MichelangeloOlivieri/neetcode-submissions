class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Binary Exponentiation (Iterative)

        if n == 0:
            return 1
        if n == 1:
            return x

        res = 1
        power = abs(n)

        while power:
            if power % 2:
                res *= x
            x *= x
            power //= 2

        return res if n >= 0 else 1 / res

"""
- Time complexity: O(log(n)).
- Space complexity: O(1).
"""