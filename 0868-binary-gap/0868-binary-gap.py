class Solution:
    def binaryGap(self, n: int) -> int:
        m = n.bit_length()
        d = 0
        p1 = -1 
        flag = 0
        
        for i in range(m):
            if n & (1 << i):
                if not flag:
                    p1 = i
                    flag = 1
                else:
                    d = max(d, i - p1)
                    p1 = i
        
        return d