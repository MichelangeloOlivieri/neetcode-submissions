class Solution:
    def reverseBits(self, n: int) -> int:
        
        """
        1) Empty input; example: ...000101 -> 101000...
        2) Use some new operators
        """

        if not n:
            return 0

        res = 0
        for _ in range(32):
            res = res << 1
            res = res | (n & 1)
            n = n >> 1
        
        return res

        """
        3) Ok
        4) Time complexity O(1); space complexity O(1)
        """