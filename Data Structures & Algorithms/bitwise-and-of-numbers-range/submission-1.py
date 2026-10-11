class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        """
        left = 3
        right = 15
        0011
        0100
        0101
        0110
        0111
        1000
        1001
        1010
        1011
        1100
        1101
        1110
        1111
        
        left = 8
        rigth = 10
        1000
        1001
        1010
        """

        res = 0
        position = 0
        while position < 32:
            first = (left >> position) & 1
            second = (right >> position) & 1
            if first & second and abs(right - left) <= 2 ** position:
                res = res | (((res >> position) | 1) << position)

            position += 1

        return res

        """
        - Time complexity O(1)
        - Space complexity O(1)
        """