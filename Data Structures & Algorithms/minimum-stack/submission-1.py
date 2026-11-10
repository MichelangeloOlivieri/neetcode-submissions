class MinStack:
    def __init__(self):
        self.stack = []   

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return

        curr_min = min(self.stack[-1][1], val)
        self.stack.append((val, curr_min))        

    def pop(self) -> None:
        if not self.stack:
            raise ValueError("popping from empty stack")

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]        

    def getMin(self) -> int:
        return self.stack[-1][1]

    """
    - Time complexity O(1) for each function
    - Space complexity O(n) where n = #{total elements}
    """
        
