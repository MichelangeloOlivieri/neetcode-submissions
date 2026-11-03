class Solution:
    def removeStars(self, s: str) -> str:
        
        if not s:
            return ""

        stack = []

        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(n)
        """