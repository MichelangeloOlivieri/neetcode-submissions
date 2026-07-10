class MyHashSet:

    def __init__(self):
        self.size = 10009
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        h = key % self.size
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = key % self.size
        for i, val in enumerate(self.buckets[h]):
            if val == key:
                self.buckets[h][i] = self.buckets[h][-1]
                self.buckets[h].pop()   

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % self.size]        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)