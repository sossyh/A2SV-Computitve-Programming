class Solution:
    def devisors(self, n):
        
        i = (n // 2) 
        
        while i > 1:
            if n % i == 0:
                return i
            
            i -= 1
        
        return "prime"
    
    def minSteps(self, n: int) -> int:
        
        keyboard = [i for i in range(n+1)]
        
        for i in range(n+1):
            if i == 1:
                keyboard[i] = 0
            elif i == 2:
                keyboard[i] = 2
            
            elif self.devisors(i) == "prime":
                keyboard[i] = i
            
            else:
                a = self.devisors(i)
                b = i // a
                keyboard[i] = keyboard[a] + b
        
        
        return keyboard[n]
        