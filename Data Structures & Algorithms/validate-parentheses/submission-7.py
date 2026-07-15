class Solution:
    def isValid(self, s: str) -> bool:

        """
        1) Only two options: "(())" or "()()" (and their variants with other types of
        parenthesis)
        2) Graph to distinguish parenthesis types, and a stack to process the whole 
        thing
        """

        if not s:
            return False
        
        graph = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []

        for c in s:
            if c in graph:
                stack.append(c)
            elif stack and c == graph[stack[-1]]:
                stack.pop()
            else:
                return False            

        return not stack