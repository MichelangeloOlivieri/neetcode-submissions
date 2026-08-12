class MyQueue:

    def __init__(self):
        self.back = []
        self.front = []
        self.index = 0

    def push(self, x: int) -> None:
        if self.empty():
            self.front.append(x)

        self.back.append(x)

    def pop(self) -> int:
        if self.empty():
            raise ValueError("Queue is empty.")
        else:
            x = self.front.pop()
            self.index += 1
            if not self.empty():
                self.front.append(self.back[self.index])
            return x

    def peek(self) -> int:
        if self.empty():
            raise ValueError("Queue is empty.")
        else:
            return self.front[0]

    def empty(self) -> bool:
        return (self.index >= len(self.back))
        
"""
self.back = []
self.front = []
self.index = 0

obj = MyQueue()
obj.push(1) -> self.back = [1], self.front = [1], self.index = 0
obj.push(2) -> self.back = [1, 2], self.front = [1], self.index = 0
obj.peek()) -> self.back = [1, 2], self.front = [1], self.index = 0
obj.pop() -> x = 1, self.back = [1, 2], self.front = [2], self.index = 1
obj.empty() -> False
"""

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()