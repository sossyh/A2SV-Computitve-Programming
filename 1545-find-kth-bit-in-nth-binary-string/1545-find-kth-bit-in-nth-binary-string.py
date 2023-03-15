class Solution:        
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        half = ((pow(2,n)-1) // 2) + 1
        if k < half:
            return self.findKthBit(n-1, k)
        elif k > half:
            newk = (pow(2, n)) - k
            return  str(1 - int(self.findKthBit(n-1, newk)))
        else:
            return "1"