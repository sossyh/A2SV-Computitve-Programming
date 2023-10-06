class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.is_end = False
        self.char_count = 0
    

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.childrens:
                curr.childrens[c] = TrieNode()
            
            curr.char_count += 1
            curr = curr.childrens[c]
        curr.is_end = True
        
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for i in words:
            trie.insert(i)
        
        possible_ans = []
        
        def dfs(curr, word):
            if not curr.childrens:
                possible_ans.append(word)
                return
            
            for i in curr.childrens:
                if curr.childrens[i].is_end:
                    word += i
                    dfs(curr.childrens[i], word)
                    word = word[:-1]
                    
            possible_ans.append(word)
        
        dfs(trie.root, "")
        
        longest_word = possible_ans[0]
        
        for i in range(1, len(possible_ans)):
            if len(possible_ans[i]) == len(longest_word):
                longest_word = possible_ans[i] if possible_ans[i] < longest_word else longest_word
                
            if len(possible_ans[i]) > len(longest_word):
                longest_word = possible_ans[i]
            
        
       
        
        return longest_word
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        