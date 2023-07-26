class Solution:
    def bitmask(self, word):
        mask = 0
        for c in word:
            mask |= (1 << (ord(c) - ord('a')))
        
        return mask
    
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        visited = [self.bitmask(word) for word in words]
        
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if (visited[i] & visited[j]) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
                
        
       
        return ans
        