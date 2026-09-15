class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0

        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:
                cmin -= 1
                cmax += 1

            if cmax < 0:
                return False
            if cmin < 0:
                cmin = 0

        return cmin == 0

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(1)
        """