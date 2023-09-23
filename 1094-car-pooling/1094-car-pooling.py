class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = 0
        for npass, fro, to in trips:
            n = max(n, to)
     
        prefixarray = [0] * (n+1)
        
        for npass, fro, to in trips:
            prefixarray[fro] += npass
            
            if to  < n + 1:
                prefixarray[to] -= npass
        
        summ = prefixarray[0]
        
        for i in range(1, len(prefixarray)):
            summ += prefixarray[i]
            prefixarray[i] = summ
        
     
        for i in prefixarray:
            if i > capacity:
                return False
        
        return True