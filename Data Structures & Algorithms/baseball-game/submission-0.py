class Solution:
    def calPoints(self, operations: List[str]) -> int:

        if not operations:
            return 0

        stack = []
        for op in operations: 
            if op == "+":
                if len(stack) >= 2:
                    stack.append(stack[-2] + stack[-1])
                elif stack:
                    stack.append(stack[-1])
            elif op == "D":
                if stack:
                    stack.append(2 * stack[-1])
            elif op == "C":
                if stack:
                    stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)

        """
        - Time complexity O(n), where n = len(operations)
        - Space complexity O(n)
        """    