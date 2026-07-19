"""
1) If stack = [1, 1, 2] and you call stack.pop(), then stack = [2]
2) stack = [], freq = {val : freq}, max_heap = [(freq, time)]
"""

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)        # {val : freq}
        self.stacks = defaultdict(list)     # {freq : []}
        self.max_freq = 0   

    def push(self, val: int) -> None:
        if val is None:
            return None

        self.freq[val] += 1
        cur_freq = self.freq[val]
        self.stacks[cur_freq].append(val)
        if cur_freq > self.max_freq:
            self.max_freq += 1

    def pop(self) -> int:
        if not self.stacks:
            raise ValueError("Insert a value first.")

        val = self.stacks[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1
    
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