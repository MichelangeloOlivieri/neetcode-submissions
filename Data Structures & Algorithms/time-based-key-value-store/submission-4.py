class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        l = 0
        r = len(arr) - 1
        res = ""

        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res
        
    """
    - Time complexity: O(1) for "set", O(log(n)) for "get", where n = #{values for the particular key}
    - Space complexity O(m) where m = #{all values}
    """
