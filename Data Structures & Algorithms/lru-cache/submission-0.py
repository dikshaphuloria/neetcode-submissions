class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.LRUCache = {}
        self.cap = capacity

        #Left = least recently used, Right = most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    #remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    #insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
            self.insert(self.LRUCache[key])
            return self.LRUCache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])

        self.LRUCache[key] = Node(key, value)
        self.insert(self.LRUCache[key])

        if len(self.LRUCache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.LRUCache[lru.key]
            

        
