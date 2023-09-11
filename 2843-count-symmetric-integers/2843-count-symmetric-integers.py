class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high+1):
            n = len(str(i))
            if n % 2 == 0:
                b = 0
                a = 0
                num = str(i)
                for k in range(n//2):
                    a += int(num[k])
                for l in range(n//2, n):
                    b += int(num[l])
                
                if b == a:
                    count += 1

        return count