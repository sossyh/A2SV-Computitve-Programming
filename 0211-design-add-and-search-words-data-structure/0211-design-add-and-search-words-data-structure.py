class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isend = False
      
          
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            curr = curr.childrens[c]
            
        curr.isend = True
        

    def search(self, word: str) -> bool:
        
        def helper(idx, curr):
            if idx == len(word) -1 and word[idx] == '.':
                for i in curr.childrens:
                    if curr.childrens[i].isend:
                        return True
                return False
            
            for j in range(idx, len(word)):
                if word[j] == '.':
                    for i in curr.childrens:
                        if helper(j+1, curr.childrens[i]):
                            return True
                    return False
                else:
                    # idx = ord(word[j]) - ord('a')
                    if word[j] not in curr.childrens:
                        return False
                    curr = curr.childrens[word[j]]
                    
            return curr.isend  
        
        return helper(0, self.root)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)