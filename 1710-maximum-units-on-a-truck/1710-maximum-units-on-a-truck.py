class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box = sorted(boxTypes, key = lambda x:x[1], reverse = True)
        total = 0
        sums = 0
        
        for i, j in box:
            if truckSize - total >= i:
                sums += i * j
                total += i
                    
            elif (truckSize - total) < i:
                sums += (truckSize - total) * j
                total += (truckSize - total)
                
            if total == truckSize:
                break
        
        return sums
                