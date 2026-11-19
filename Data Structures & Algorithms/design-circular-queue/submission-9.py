class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.size = 0
        self.left = 0
        self.right = -1     

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.right = (self.right + 1) % self.capacity
        self.queue[self.right] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.left = (self.left + 1) % self.capacity
        self.size -= 1
        return True     

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.left]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.right]

    def isEmpty(self) -> bool:
        return self.size == 0      

    def isFull(self) -> bool:
        return self.size == self.capacity

    """
    - Time complexity: O(1) for each function.
    - Space complexity: O(n), where n = #{values}
    """


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()