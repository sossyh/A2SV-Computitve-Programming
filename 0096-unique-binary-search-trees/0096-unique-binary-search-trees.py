class Solution:
    def numTrees(self, n: int) -> int:
        
        cache = [1] * (n+1)
        
        for node in range(2, n+1):
            summ = 0
            
            for root in range(1, node+1):
                left = root - 1
                right = node - root
                summ += cache[left] * cache[right]
            
            cache[node] = summ
        
        return cache[-1]
            