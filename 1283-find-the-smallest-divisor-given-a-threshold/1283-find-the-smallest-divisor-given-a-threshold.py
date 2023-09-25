class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        bestmin = max(nums)
        
        while low <= high:
            mid = low + (high - low) // 2
            
            total = 0
            for i in nums:
                total += math.ceil(i / mid)
            
            if total <= threshold:
                bestmin = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return bestmin