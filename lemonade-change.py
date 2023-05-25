class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)

        if bills[0] > 5:
            return False

        for i in bills:
                        
            if i == 10:
                if d[5] <= 0:
                    return False
                
                d[5] -= 1
            
            if i == 20:
                if d[5] <= 0:
                    return False
                
                if d[10] <= 0 and d[5] <= 2:
                    return False
                
                if d[10]:
                    d[10] -= 1
                    d[5] -= 1
                
                else:
                    d[5] -= 3
                
            d[i] += 1
        
        return True