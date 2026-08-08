class StockSpanner:

    def __init__(self):
        self.stack = []     

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append([price, span])
        return span        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
Time complexity O(n), where n is the number of stock prices inserted; space complexity O(n)
"""