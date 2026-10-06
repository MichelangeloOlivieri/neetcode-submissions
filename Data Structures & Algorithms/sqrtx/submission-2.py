class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        l = 1
        r = x
        res = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            square = mid ** 2
            if square == x:
                return mid
            elif square < x:
                l = mid + 1
                res = mid
            else:
                r = mid - 1

        return res  

        """
        - Time complexity O(log(x))
        - Space complexity O(1)
        """