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
        # 10009 is a prime number. Prime modulo heavily mitigates collision clustering.
        self.size = 10009 
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        h = key % self.size
        # "in" on a small Python list delegates to a heavily optimized C loop
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = key % self.size
        bucket = self.buckets[h]
        
        for i, val in enumerate(bucket):
            if val == key:
                # SOTA Optimization: Swap with the last element and pop.
                # Avoids the O(K) memory shift caused by standard list.remove()
                bucket[i] = bucket[-1]
                bucket.pop()
                return

    def contains(self, key: int) -> bool:
        return key in self.buckets[key % self.size]

    # ==========================================
    # Time Complexity: O(1) average for all operations. O(K) worst case where K is the bucket size (heavily minimized by the prime modulo).
    # Space Complexity: O(N + M) where N is the number of elements and M is the base size (10009). No dummy object overhead.
    # ==========================================