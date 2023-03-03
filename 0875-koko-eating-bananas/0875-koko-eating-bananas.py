class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = max(piles)
        
        while low <= high:
            mid = low + (high - low)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours > h:
                low = mid + 1
            else:
                result = mid
                high = mid - 1
                
        return result
        