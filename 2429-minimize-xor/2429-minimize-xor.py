class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2bitcount = 0
        # print(bin(num2), bin(24))
        while num2:
            if num2 & 1:
                num2bitcount += 1
            num2 >>= 1
                
        
        x = 0
        # print(num2bitcount)
        
        for i in range(31, -1, -1):
            if num2bitcount and num1 & (1 << i):
                x |= (1 << i)
                num2bitcount -= 1
        
    
        
        
        for i in range(32):
            if num2bitcount and not (x & (1 << i)):
                x |= (1 << i)
                num2bitcount -= 1
        
        return x