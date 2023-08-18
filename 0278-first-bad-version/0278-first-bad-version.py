# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        best = None
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if isBadVersion(mid):
                best = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        
        return best
                
            
        