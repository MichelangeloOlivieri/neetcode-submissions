"""
1) If stack = [1, 1, 2] and you call stack.pop(), then stack = [2]
2) stack = [], freq = {val : freq}, max_heap = [(freq, time)]
"""

class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)
        self.max_heap = []   
        self.time = 0    

    def push(self, val: int) -> None:
        if val is None:
            return None

        self.stack.append(val)
        self.time += 1
        self.freq[val] += 1

        frequency = self.freq[val]
        time = self.time
        heapq.heappush(self.max_heap, (-frequency, -time, val))

    def pop(self) -> int:
        if not self.max_heap:
            return -1

        _, _, val = heapq.heappop(self.max_heap)
        self.freq[val] -= 1
    
        return val

"""
3) stack = FreqStack(); 
- stack.push(17) -> self.stack = [17], self.freq = {17 : 1}, self.max_heap = [(-1, 0)]
- stack.push(25) -> self.stack = [17, 25], self.freq = {17 : 1, 25 : 1},
self.max_heap = [(-1, -1), (-1, 0)]
"""

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()