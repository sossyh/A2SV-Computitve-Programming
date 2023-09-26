class TrieNode:
    def __init__(self):
        self.childrens = [None for i in range(26)]
        self.is_end = False
    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.childrens[idx]:
                curr.childrens[idx] = TrieNode()
            curr = curr.childrens[idx]
        curr.is_end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.childrens[idx]:
                return False
            
            curr = curr.childrens[idx]
        
        return True if curr.is_end else False            
        
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.childrens[idx]:
                return False
            
            curr = curr.childrens[idx]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)