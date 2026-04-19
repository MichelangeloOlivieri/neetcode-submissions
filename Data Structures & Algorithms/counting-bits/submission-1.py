class Solution:
    def countBits(self, n: int) -> List[int]:

        """
        1) Empty input
        2) Same exercise as the previous one
        """
        
        if not n:
            return [0]

        output = [0] * (n + 1)
        for i in range(0, n + 1):
            j = i
            while j:
                if j & 1:
                    output[i] += 1
                j = j >> 1

        return output

        """
        3) Ok
        4) Time complexity O(n); space complexity O(1)
        """