class Solution:
    def hammingWeight(self, n: int) -> int:

        if not n:
            return 0

        res = 0
        while n > 0:
            if n & 1:
                res += 1
            n = n >> 1

        return res

        


                