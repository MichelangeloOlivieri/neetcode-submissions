class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        res = 0
        position = 0
        while position < 32:
            first = (left >> position) & 1
            second = (right >> position) & 1
            if first & second and abs(right - left) <= 1 << position:
                res = res | (((res >> position) | 1) << position)

            position += 1

        return res

        """
        - Time complexity O(1)
        - Space complexity O(1)
        """