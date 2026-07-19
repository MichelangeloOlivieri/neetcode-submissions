from collections import defaultdict

class FreqStack:
    # ==========================================
    # Clarifying Questions (Implicit):
    # 1. Can we push 0 or negative values? (Yes, standard integers. No truthy/falsy guard clauses on values).
    # 2. Can pop() be called on an empty stack? (Defensive programming implemented to raise IndexError).
    #
    # Algorithm Description:
    # Hash Map of Stacks. Instead of an O(log N) heap, we map each frequency integer 
    # to a Stack (array) of elements that have reached that exact frequency. We track the global 
    # maximum frequency. This achieves pure O(1) time complexity for both push and pop.
    # ==========================================

    def __init__(self):
        self.freqs = defaultdict(int)
        self.group_stacks = defaultdict(list)
        self.max_freq: int = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        current_freq = self.freqs[val]

        self.group_stacks[current_freq].append(val)

        if current_freq > self.max_freq:
            self.max_freq = current_freq

    def pop(self) -> int:
        if self.max_freq == 0:
            raise IndexError("pop from empty FreqStack")
            
        val = self.group_stacks[self.max_freq].pop()
        self.freqs[val] -= 1
        
        if not self.group_stacks[self.max_freq]:
            self.max_freq -= 1
            
        return val

    # ==========================================
    # Time Complexity: O(1) for both push and pop. Hash map lookups, integer arithmetic, and list appends/pops are strictly O(1).
    # Space Complexity: O(N) where N is the total number of elements pushed, bounded by the space of the two dictionaries.
    # ==========================================