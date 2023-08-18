class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        low, high = 0, x//2
        best = x//2
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if mid ** 2 <= x:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best
                