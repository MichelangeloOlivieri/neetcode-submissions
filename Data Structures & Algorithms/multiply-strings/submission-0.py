class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        """
        1) Empty input; example seen
        2) 
        """

        if not num1 or not num2:
            return "0"

        num1 = int(num1)
        num2 = int(num2)

        return str(num1 * num2)
        