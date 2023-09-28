class Trienode:
    def __init__(self) -> None:
        self.children = {}
        self.isend = False
        
class Trie:
    def __init__(self) -> None:
        self.root = Trienode()
    
    def insert(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trienode()
            curr = curr.children[c]
        curr.isend = True
            
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        trie = Trie()
        commonpre = ""
        
        for i in strs:
            trie.insert(i)
        
        root = trie.root
        
        while root and len(root.children) == 1 and not root.isend:
            for i in root.children:
                commonpre += i
                root = root.children[i]
        
        return commonpre
            
            