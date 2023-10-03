class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0
    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
            curr.count += 1
            
        curr.is_end = True
        
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        total = 0
        
        for c in prefix:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
            total += curr.count
        
        return total


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        
        result = []
        for word in words:
            a = trie.startsWith(word)
            result.append(a)
        
        return result
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        