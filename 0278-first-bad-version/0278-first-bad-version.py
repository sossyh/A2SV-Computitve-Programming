# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 1
        best = n
        
        while left <= right:
            mid = left + (right - left )//2
            if isBadVersion(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
                
        return best
                
                
            