class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        visited = []
        
        for i in range(len(words)):
            visited.append(set(words[i]))
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(visited[i].intersection(visited[j])) == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
                
        
       
        return ans
        