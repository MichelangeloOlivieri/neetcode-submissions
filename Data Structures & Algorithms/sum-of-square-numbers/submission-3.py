class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        l = 0
        r = int(math.sqrt(c))

        while l <= r:
            total = l**2 + r**2
            if total == c:
                return True
            elif total > c:
                r -= 1
            else:
                l += 1

        return False

        """
        - Time complexity O(sqrt(c))
        - Space complexity O(1)
        """