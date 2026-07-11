class MyHashSet:

    def __init__(self):
        self.size = 10009
        self.buckets = [[] for _ in range(self.size)]        

    def add(self, key: int) -> None:
        i = key % self.size
        bucket = self.buckets[i]

        for j in range(len(bucket)):
            if bucket[j] == key:
                return

        bucket.append(key)
        
    def remove(self, key: int) -> None:
        i = key % self.size
        bucket = self.buckets[i]

        for j in range(len(bucket)):
            if bucket[j] == key:
                bucket[j] = bucket[-1]
                bucket.pop()        

    def contains(self, key: int) -> bool:
        i = key % self.size
        bucket = self.buckets[i]

        for j in range(len(bucket)):
            if bucket[j] == key:
                return True

        return False        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)