class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return 0
        
        stack = []
        operations = {'+', '-', '*', '/'}

        for s in tokens:
            if s not in operations:
                stack.append(int(s))
            else: 
                b = stack.pop()
                a = stack.pop()

                if s == '+':
                    res = a + b
                elif s == '-':
                    res = a - b
                elif s == '*':
                    res = a * b
                elif s == '/':
                    res = int(a / b)
                
                stack.append(res)

        return stack[0]

        """
        - Space complexity O(n), where n = len(tokens)
        - Time complexity O(n)
        """

