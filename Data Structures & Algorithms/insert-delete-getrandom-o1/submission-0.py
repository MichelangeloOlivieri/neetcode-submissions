class RandomizedSet:
    def __init__(self):
        self.buckets = [[] for _ in range(97)]

    def insert(self, val: int) -> bool:
        index = val % len(self.buckets)
        bucket = self.buckets[index]

        for n in bucket:
            if n == val:
                return False
        
        bucket.append(val)
        return True

    def remove(self, val: int) -> bool:
        index = val % len(self.buckets)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i] == val:
                bucket[i] = bucket[-1]
                bucket.pop()
                return True

        return False                

    def getRandom(self) -> int:
        bucket = None
        while not bucket:
            bucket_index = random.randint(0, len(self.buckets) - 1)
            bucket = self.buckets[bucket_index]
        element_index = random.randint(0, len(bucket) - 1)
        return bucket[element_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()