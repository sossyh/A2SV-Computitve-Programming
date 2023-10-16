class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.last = Node()
        self.first = Node(next = self.last)
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            prev_node = node.prev
            next_node1 = node.next
            prev_node.next = next_node1
            next_node1.prev = prev_node


            next_node = self.first.next
            self.first.next = node
            node.prev = self.first
            node.next = next_node
            next_node.prev = node
            self.cache[key] = node

            return node.val
        else:
            return -1
        
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            prev_node = node.prev
            next_node1 = node.next
            prev_node.next = next_node1
            next_node1.prev = prev_node


            next_node = self.first.next
            self.first.next = node
            node.prev = self.first
            node.next = next_node
            next_node.prev = node
            self.cache[key] = node
            
        else:
            if len(self.cache) == self.capacity:
                key_to_be_deleted = self.last.prev.key
                self.last.prev = self.last.prev.prev
                prev_last = self.last.prev
                prev_last.next = self.last
                del self.cache[key_to_be_deleted]

            before = self.first.next        
            node = Node(key, value, self.first, before)
            self.first.next = node
            before.prev = node
            self.cache[key] = node
            # print(self.cache)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)