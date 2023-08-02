class Solution:
    def power(self, x, exp):
        if exp == 0:
            return 1
        
        if exp % 2 == 0:
            return self.power((x*x)% self.mod, exp // 2)
        else:
            return (x * self.power((x*x) % self.mod, exp // 2)) 
            
            
        
        
    def countGoodNumbers(self, n: int) -> int:
        self.mod = (pow(10,9) + 7)
        nume, numo = 0, 0
        
        nume = n // 2 + (n % 2)
        numo = n // 2 
        
        ans = (((self.power(4, numo)) % self.mod) * ((self.power(5, nume)) % self.mod)
        ) % self.mod
        
        return ans 