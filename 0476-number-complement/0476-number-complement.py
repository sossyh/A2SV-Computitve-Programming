class Solution:
    def findComplement(self, num: int) -> int:
        ans = ""
    
        while num > 0:
            a = (num & 1) ^ 1
            ans = str(a) + ans
            num >>= 1
     
        return int(ans,2)
        