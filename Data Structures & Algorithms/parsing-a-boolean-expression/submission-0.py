class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for c in expression:
            if c == ',':
                continue

            if c != ')':
                stack.append(c)
            else:
                inner_bools = set()
                while stack[-1] != '(':
                    inner_bools.add(stack.pop())

                stack.pop()
                operator = stack.pop()

                if operator == '&':
                    res = 'f' if 'f' in inner_bools else 't'
                elif operator == '|':
                    res = 't' if 't' in inner_bools else 'f'
                elif operator == '!':
                    res = 'f' if 't' in inner_bools else 't'

                stack.append(res)

        return stack[0] == 't'

        """
        - Time complexity O(n), where n = len(expression)
        - Space complexity O(n)
        """