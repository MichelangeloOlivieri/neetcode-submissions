class RandomizedSet:
    def __init__(self):
        self.nums = set()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False

        self.nums.add(val)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False

        self.nums.add(val)
        for i in range(len(self.arr) - 1, -1, -1):
            if self.arr[i] == val:
                self.arr[i] = self.arr[-1]
                self.arr.pop()
                break

        return True                

    def getRandom(self) -> int:
        index = random.randint(0, len(self.arr) - 1)
        return self.arr[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()