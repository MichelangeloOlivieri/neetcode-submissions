class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber > 0:
            columnNumber -= 1
            res.append(chr((columnNumber % 26) + ord('A')))
            columnNumber //= 26
            
        res.reverse()
        return "".join(res)

        """
        - Time complexity O(log_26(n)), where n = columnNumber
        - Space complexity O(log_26(n))
        """