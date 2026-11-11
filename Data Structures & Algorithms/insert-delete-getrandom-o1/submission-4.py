class RandomizedSet:
    def __init__(self):
        self.index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False

        i = self.index[val]
        last = self.nums[-1]
        self.nums[i] = last
        self.index[last] = i
        self.nums.pop()
        del self.index[val]
        return True                

    def getRandom(self) -> int:
        return random.choice(self.nums)

    """
    - Time complexity O(1) for each function
    - Space complexity O(n), where n = #{values}
    """

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()