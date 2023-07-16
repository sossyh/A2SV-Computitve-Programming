class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        for i in range(1, n):
            for j in range(1, n):
                a = math.sqrt(i**2 + j ** 2)
                rounded = round(a)
                if a == rounded and a <= n:
                    count += 1
        
        return count
        