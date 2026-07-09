class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_val = {}
        self.freq_map = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1

        val, freq = self.key_val[key]
        del self.freq_map[freq][key]

        if not self.freq_map[freq] and freq == self.min_freq:
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

            if not self.freq_map[freq] and freq == self.min_freq:
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



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)