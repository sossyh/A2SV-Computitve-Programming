class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return str(0)
        
        if num < 0:
            num = (1<<32) + num
            
        
        res = ""
        
        while num > 0:
            rem = num % 16
            
            if rem <= 9:
                res += str(rem)
            else:
                
                res += chr(87+rem)
            
            num //= 16
        
        
        return res[::-1]