class Solution:
    def minEnd(self, n: int, x: int) -> int:
        rem = n - 1
        res = x
        position = 0
        
        while rem:
            while (x >> position) & 1:
                position += 1
            
            bit_from_rem = rem & 1
            res |= (bit_from_rem << position)
            rem >>= 1
            position += 1
            
        return res

        """
        - Time complexity O(1)
        - Space complexity O(1)
        """