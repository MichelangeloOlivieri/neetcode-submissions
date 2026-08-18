class MyHashMap:

    def __init__(self):
        self.hash_map = [[] for _ in range(117)]

    def put(self, key: int, value: int) -> None:
        index = key % 117
        arr = self.hash_map[index]

        insert = True
        for i in range(len(arr)):
            arr_key, arr_value = arr[i]
            if arr_key == key:
                arr[i][1] = value
                insert = False

        if insert:
            arr.append([key, value])

    def get(self, key: int) -> int:
        index = key % 117
        arr = self.hash_map[index]

        for i in range(len(arr)):
            arr_key, arr_value = arr[i]
            if arr_key == key:
                return arr_value

        return -1        

    def remove(self, key: int) -> None:
        index = key % 117
        arr = self.hash_map[index]

        for i in range(len(arr)):
            arr_key, arr_value = arr[i]
            if arr_key == key:
                arr[i][0] = arr[-1][0]
                arr[i][1] = arr[-1][1]
                arr.pop()

    """
    obj = MyHashMap()
    obj.put(3, 5)
    obj.put(3, 6)
    obj.put(4, 10)
    
    x = obj.get(18)
    y = obj.get(3)
    obj.remove(4)

    obj = [..., [[3, 6]], [] ...]
    x = -1 
    y = 6
    """

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)