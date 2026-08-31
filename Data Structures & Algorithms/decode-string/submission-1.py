class Solution:
    def decodeString(self, s: str) -> str:

        if not s:
            return ""

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)

        """
        - Time complexity O(N * K^D), where N = len(s), K = max_integer, D = max_parenthesis_depth
        - Space complexity O(N * K^D)
        """