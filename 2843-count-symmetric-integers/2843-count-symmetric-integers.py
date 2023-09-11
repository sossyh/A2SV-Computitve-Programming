class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high+1):
            n = len(str(i))
            if n % 2 == 0:
                num = [int(k) for k in str(i)]
                
                if sum(num[:n//2]) == sum(num[n//2:n]):
                    count += 1

        return count