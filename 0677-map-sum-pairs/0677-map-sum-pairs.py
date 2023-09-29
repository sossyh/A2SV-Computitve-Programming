class TrieNode:
    def __init__(self):
        self.childrens = [None for i in range(26)]
        self.isend = 0
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()        
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        
        for c in key:
            idx = ord(c) - ord('a')
            if not curr.childrens[idx]:
                curr.childrens[idx] = TrieNode()
            curr = curr.childrens[idx]
        
        curr.isend = val 
    
    def val(self, curr):
        if not curr:
            return 0
        
        total = 0
        
        for i in curr.childrens:
            if i:
                total += self.val(i) 
        
        return total + curr.isend
        
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        total = 0
        
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr:
                return 0
            curr = curr.childrens[idx]
        
        total = self.val(curr)
            

        return total
                
            
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)