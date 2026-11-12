class Node:
    def __init__(self, key: int, val: int, prev: "Node", next: "Node"):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.max_capacity = capacity
        self.curr_capacity = 0

        if self.max_capacity == 0:
            raise ValueError("invalid capacity")

        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, self.head, None)
        self.head.next = self.tail
    
    def _update(self, node) -> None:
        # remove old pointers to node
        node.prev.next = node.next
        node.next.prev = node.prev
        # put new pointers to node
        self.tail.prev.next = node
        temp = self.tail.prev
        self.tail.prev = node
        # change pointers from node
        node.prev = temp
        node.next = self.tail

    def _delete(self, node) -> None:
        # delete pointers to node
        self.head.next = node.next
        node.next.prev = self.head
        # delete pointers from node
        node.prev = None
        node.next = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key][0]
        self._update(node)
        return self.cache[key][1]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key][0]
            self._update(node)
            self.cache[key][0] = node
            self.cache[key][1] = value
            return

        if self.curr_capacity == self.max_capacity:
            lru_node = self.head.next
            k = lru_node.key
            del self.cache[k]
            self._delete(lru_node)
            self.curr_capacity -= 1

        # create node with the right pointers
        node = Node(key, value, self.tail.prev, self.tail)
        # update pointers near tail
        self.tail.prev.next = node
        self.tail.prev = node

        self.cache[key] = [node, value]
        self.curr_capacity += 1

"""
cache = {2 : 2, 3 : 3}, capacity = 2
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
"""
        
