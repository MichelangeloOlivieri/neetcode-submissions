class MyHashSet:
    # ==========================================
    # Clarifying Questions:
    # 1. What is the maximum number of operations? (Determines initial bucket size to avoid rehashing).
    # 2. Are we allowed to use dynamic arrays (lists) for buckets? (Standard is yes, as long as we don't use hash-based sets/dicts).
    #
    # Algorithm Description:
    # Implement a Hash Set using an Array of Arrays (chaining) for optimal CPU cache locality, utilizing a prime number modulo for uniform distribution and a swap-and-pop technique for O(1) removals within buckets.
    # ==========================================

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
                return        

    def contains(self, key: int) -> bool:
        i = key % self.size
        bucket = self.buckets[i]

        for j in range(len(bucket)):
            if bucket[j] == key:
                return True

        return False 

    # ==========================================
    # Time Complexity: O(1) average for all operations. O(K) worst case where K is the bucket size (heavily minimized by the prime modulo).
    # Space Complexity: O(N + M) where N is the number of elements and M is the base size (10009). No dummy object overhead.
    # ==========================================