import collections

class LFUCache:
    # ==========================================
    # Clarifying Questions:
    # 1. Can the capacity be initialized to 0? (Yes, handled).
    # 2. Are updates to existing keys counted as a use for frequency? (Yes).
    # 3. How to break frequency ties? (Least Recently Used among the LFU).
    #
    # Algorithm Description:
    # Maintain a map of key to value/frequency pairs and a frequency map linking to an OrderedDict (acting as an O(1) LRU cache per frequency), updating the global minimum frequency dynamically.
    # ==========================================

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_val = {}
        self.freq_map = collections.defaultdict(collections.OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        
        val, freq = self.key_val[key]
        
        del self.freq_map[freq][key]
        if not self.freq_map[freq] and self.min_freq == freq:
            self.min_freq += 1
            
        self.key_val[key] = (val, freq + 1)
        self.freq_map[freq + 1][key] = None
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_val:
            _, freq = self.key_val[key]
            
            del self.freq_map[freq][key]
            if not self.freq_map[freq] and self.min_freq == freq:
                self.min_freq += 1
                
            self.key_val[key] = (value, freq + 1)
            self.freq_map[freq + 1][key] = None
            return
            
        if len(self.key_val) == self.capacity:
            lru_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_val[lru_key]
            
        self.key_val[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1

    # ==========================================
    # Time Complexity: O(1) for both get and put.
    # Space Complexity: O(C) where C is the capacity.
    # ==========================================